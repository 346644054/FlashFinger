from collections import Callable
from typing import List
from typing import Optional
from typing import Union

from sense.camera import VideoSource
from sense.camera import VideoStream
from sense.display import DisplayResults
from sense.engine import InferenceEngine
from sense.downstream_tasks.nn_utils import RealtimeNeuralNet
from sense.downstream_tasks.postprocess import PostProcessor

import cv2
import numpy as np
import sense.functin_real as fun
import sense.SwitchState as switch
import asyncio
import websockets
import threading
import time
import telnetlib
import time
#from demo.testclient import *

class Controller:
    def __init__(
            self,
            neural_network: RealtimeNeuralNet,
            post_processors: Union[PostProcessor, List[PostProcessor]],
            results_display: DisplayResults,
            callbacks: Optional[List[Callable]] = None,
            camera_id: int = 0,
            path_in: str = Optional[None],
            path_out: str = Optional[None],
            use_gpu: bool = True):
        """
        :param neural_network:
            The neural network that produces the predictions for the camera image.
        :param post_processors:
            Post processors that are applied to the generated predictions to filter or manipulate the data.
            Refer to the PostProcessor class for more information.
        :param callbacks:
            A list of functions that are called in each loop iteration once the inference is started.
            The input dict always contains the key 'prediction' under which an np.ndarray with the raw predictions is
            stored. The presence of other keys depend on the choice of post processors.
            The callbacks should return True if the inference should continue, False otherwise.
        :param results_display:
            A display window which shows the current camera image as well as the prediction with the highest
            probability
        :param camera_id:
            The index of the webcam that is used. Default id is 0.
        :param path_in:
            If provided, use a video file located at the path as the input to the model
        :param path_out:
            If provided, store the captured video in a file in this location
        :param use_gpu:
            If True, run the model on the GPU
        """
        self.inference_engine = InferenceEngine(neural_network, use_gpu=use_gpu)
        video_source = VideoSource(
            camera_id=camera_id,
            size=self.inference_engine.expected_frame_size,
            filename=path_in
        )

        self.video_stream = VideoStream(video_source, self.inference_engine.fps)


        if isinstance(post_processors, list):
            self.postprocessors = post_processors
        else:
            self.postprocessors = [post_processors]

        self.callbacks = callbacks or []

        self.frame_index = None
        self.clip = None

        self.results_display = results_display
        self.path_out = path_out
        self.video_recorder = None  # created in `display_prediction`
        self.video_recorder_raw = None  # created in `display_prediction`


    def run_inference(self,flagMode):
        runtime_error = None

        self._start_inference()
        swi = {
            "Calling someone closer": 0,
            "Covering ears": 0,
            "Covering eyes": 0,
            "Nodding": 0,
            "Pointing left": 0,
            "Pointing right": 0,
            "Pointing to the camera": 0,
            "Putting finger to mouth": 0,
            "Scratching": 0,
            "Shaking head": 0,
            "Swiping down (with two hands)": 0,
            "left": 0,
            "right": 0,
            "Swiping up": 0,
            "Swiping up (with two hands)": 0,
            "Thumb down": 0,

            "Waving": 0,
            "Zooming in": 0,
            "Zooming out": 0,
            "Thumup": 0,
            "down": 0,
            "do_other_thing": 0,
            "left": 0,
            "narrow": 0,
            "point": 0,
            "right": 0,
            "roll": 0,
            "scatch": 0,
            "up": 0,
            "handup":0,
            "ear":0,

        }
        # 调用检测当前窗口函数，返回值为mode
        # mode = 0 PPT
        # mode = 1 Word
        # mode = 2 视频
        # mode = 3 地图
        # mode = 4 3D模型
        # mode = 5 focusky
        mode = switch.switchSt()
        cnt=0

        '''con = telnetlib.Telnet()
        Address = "47.98.40.28:8000"
        serverAddress = Address.split(':')
        con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
        response = con.read_some()
        print(response.decode("utf-8"))



        con.write(('login ' + "alex" + "$$" +
                   "123" + '\n').encode("utf-8"))
        response = con.read_some()
        print(response.decode("utf-8"))
        con.write(
            ('join ' + "012" + '\n').encode("utf-8"))
        response = con.read_some()
        print(response.decode("utf-8"))'''


        cnt=0
        while True:
            try:
                '''from clientM import state
                if state==1:
                    self._stop_inference()'''
                self.frame_index += 1

                # Grab frame if possible
                img_tuple = self.video_stream.get_image()
                # If not possible, stop
                if img_tuple is None:
                    break

                # Unpack
                img, numpy_img = img_tuple

                self.clip = np.roll(self.clip, -1, 1)
                self.clip[:, -1, :, :, :] = numpy_img

                if self.frame_index == self.inference_engine.step_size:
                    # A new clip is ready
                    self.inference_engine.put_nowait(self.clip)

                self.frame_index = self.frame_index % self.inference_engine.step_size

                # Get predictions
                prediction = self.inference_engine.get_nowait()

                prediction_postprocessed = self.postprocess_prediction(prediction)

                presult1 = prediction_postprocessed
                #cnt=2
                ##if divmod(cnt,1)[1]==0:
                loop1 = asyncio.new_event_loop()
                asyncio.set_event_loop(loop1)
                asyncio.get_event_loop().run_until_complete(self.main_logic(presult1))
                # asyncio.get_event_loop().run_until_complete(main_logic(prediction_postprocessed))
                print(prediction_postprocessed)
                presult  = prediction_postprocessed['sorted_predictions'][0][0]

                #cnt+=1
                #if divmod(cnt,4)[1]==0:


                '''print("0000000")
                con.write(
                    ('docontrol ' + presult + '\n').encode("utf-8"))
                print("1111111")'''
                fun.pris(prediction_postprocessed, swi, mode,flagMode)
                self.display_prediction(img, prediction_postprocessed)

                # Apply callbacks
                if not all(callback(prediction_postprocessed) for callback in self.callbacks):
                    break

            except Exception as e:
                runtime_error = e
                break

            # Press escape to exit
            if cv2.waitKey(1) == 27:
                break

        self._stop_inference()

        if runtime_error:
            raise runtime_error

    async def main_logic(self,presult):
        async with websockets.connect('ws://127.0.0.1:8081') as websocket:
            await self.send_msg(websocket,presult)
    async def send_msg(self,websocket,presult):
        # while True:
        # _text = input("please enter your context: ")
        # if _text == "exit":
        #     print(f'you have enter "exit", goodbye')
        #     await websocket.close(reason="user exit")
        #     return False

        _text = ""

        prediction ={'scatch':  0, 'up': 0, 'left':  0, 'narrow': 0, 'ear': 0, 'down': 0, 'point': 0, 'handup': 0, 'thumup':0, 'right': 0, 'roll':0}
        for elem in presult["sorted_predictions"]:
            for k,v in prediction.items():
                if k == elem[0]:
                    prediction[k] = elem[1]

        for i in prediction.values():
            _text += str(i)
            _text += "$"
        _text += str(prediction.get('roll'))
        await websocket.send(_text)
        recv_text = await websocket.recv()
        print(f"{recv_text}")

    def postprocess_prediction(self, prediction):
        post_processed_data = {}
        for post_processor in self.postprocessors:
            post_processed_data.update(post_processor(prediction))
        return {'prediction': prediction, **post_processed_data}



    def display_prediction(self, img: np.ndarray, prediction_postprocessed: dict):
        # Live display
        img_augmented = self.results_display.show(img, prediction_postprocessed)

        # Recording
        if self.path_out:
            if self.video_recorder is None or self.video_recorder_raw is None:
                self._instantiate_video_recorders(img_augmented, img)

            self.video_recorder.write(img_augmented)
            self.video_recorder_raw.write(img)

    def _start_inference(self):
        print("Starting inference")
        self.clip = np.random.randn(
            1,
            self.inference_engine.step_size,
            self.inference_engine.expected_frame_size[0],
            self.inference_engine.expected_frame_size[1],
            3
        )
        self.frame_index = 0
        self.inference_engine.start()
        self.video_stream.start()

    def _stop_inference(self):

        print("Stopping inference")
        cv2.destroyAllWindows()
        self.video_stream.stop()
        self.inference_engine.stop()

        if self.video_recorder is not None:
            self.video_recorder.release()

        if self.video_recorder_raw is not None:
            self.video_recorder_raw.release()

    def _instantiate_video_recorders(self, img_augmented, img_raw):
        self.video_recorder = cv2.VideoWriter(self.path_out, 0x7634706d, self.inference_engine.fps,
                                              (img_augmented.shape[1], img_augmented.shape[0]))

        path_raw = self.path_out.replace('.mp4', '_raw.mp4')
        self.video_recorder_raw = cv2.VideoWriter(path_raw, 0x7634706d, self.inference_engine.fps,
                                                  (img_raw.shape[1], img_raw.shape[0]))
