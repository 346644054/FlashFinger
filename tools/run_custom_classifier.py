#!/usr/bin/env python
"""
Run a custom classifier that was obtained via the train_classifier script.

Usage:
  run_custom_classifier.py --custom_classifier=PATH
                           [--camera_id=CAMERA_ID]
                           [--path_in=FILENAME]
                           [--path_out=FILENAME]
                           [--title=TITLE]
                           [--use_gpu]
  run_custom_classifier.py (-h | --help)

Options:
  --custom_classifier=PATH   Path to the custom classifier to use
  --path_in=FILENAME         Video file to stream from
  --path_out=FILENAME        Video file to stream to
  --title=TITLE              This adds a title to the window display
"""
import os
import json

from docopt import docopt
import torch

import sense.display
from sense.controller import Controller
from sense.downstream_tasks.nn_utils import LogisticRegression
from sense.downstream_tasks.nn_utils import Pipe
from sense.downstream_tasks.postprocess import PostprocessClassificationOutput
from sense.loading import build_backbone_network
from sense.loading import load_backbone_model_from_config
from sense.loading import update_backbone_weights
from demo.testserver import mymain
import threading
#from demo.main import mymymain
#if __name__ == "__main__":
    # Parse arguments
    #args = docopt(__doc__)
def run_my_claasfier(flagMode=0):

    camera_id = int( 0)
    path_in =  None
    path_out =  None
    custom_classifier = "D:\\sense\\newSense\\newsense_1\\checkpoints\\best1"
    title =  None
    use_gpu = True

    # Load backbone network according to config file
    backbone_model_config, backbone_weights = load_backbone_model_from_config(custom_classifier)

    # Load custom classifier
    checkpoint_classifier = torch.load(os.path.join(custom_classifier, 'best_classifier.checkpoint'))

    # Update original weights in case some intermediate layers have been finetuned
    update_backbone_weights(backbone_weights, checkpoint_classifier)

    # Create backbone network
    backbone_network = build_backbone_network(backbone_model_config, backbone_weights)

    with open(os.path.join(custom_classifier, 'label2int.json')) as file:
        class2int = json.load(file)
    INT2LAB = {value: key for key, value in class2int.items()}

    gesture_classifier = LogisticRegression(num_in=backbone_network.feature_dim,
                                            num_out=len(INT2LAB))
    gesture_classifier.load_state_dict(checkpoint_classifier)
    gesture_classifier.eval()

    # Concatenate feature extractor and met converter
    net = Pipe(backbone_network, gesture_classifier)

    postprocessor = [
        PostprocessClassificationOutput(INT2LAB, smoothing=4)
    ]

    display_ops = [
        sense.display.DisplayFPS(expected_camera_fps=net.fps,
                                 expected_inference_fps=net.fps / net.step_size),
        sense.display.DisplayTopKClassificationOutputs(top_k=1, threshold=0.1),
    ]
    display_results = sense.display.DisplayResults(title=title, display_ops=display_ops)

    # Run live inference
    controller = Controller(
        neural_network=net,
        post_processors=postprocessor,
        results_display=display_results,
        callbacks=[],
        camera_id=camera_id,
        path_in=path_in,
        path_out=path_out,
        use_gpu=use_gpu
    )
    # global presult
    # presult = {'prediction': None, 'sorted_predictions': [('do_other_thing', 0), ('scatch', 0), ('up', 0), ('left', 0), ('narrow', 0), ('ear', 0), ('down', 0), ('point', 0), ('handup', 0), ('thumup', 0), ('right', 0), ('roll', 0)]}
    t4=threading.Thread(target=mymain)
    t4.start()
    # t2 = threading.Thread(target=mymymain)
    # t2.start()
    controller.run_inference(flagMode)


#run_my_claasfier()