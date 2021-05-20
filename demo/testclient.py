
import asyncio
import websockets
import time
import random


# 向服务器端发送认证后的消息
async def send_msg(websocket):
    # while True:
        # _text = input("please enter your context: ")
        # if _text == "exit":
        #     print(f'you have enter "exit", goodbye')
        #     await websocket.close(reason="user exit")
        #     return False
    while 1:

        time.sleep(0.1)
        _text = ""
        for i in range(1,11):
            global presult
            prediction=presult
            _text+=str(prediction["sorted_predictions"][i][1])
            _text+="$"
        _text += str(prediction["sorted_predictions"][11][1])
        _text+="0.8"
        await websocket.send(_text)
        recv_text = await websocket.recv()
        print(f"{recv_text}")



# 客户端主逻辑
async def main_logic():
    async with websockets.connect('ws://127.0.0.1:8081') as websocket:
        await send_msg(websocket)
def mmymain():
    # new_loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(new_loop)
    asyncio.get_event_loop().run_until_complete(main_logic())