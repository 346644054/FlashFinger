import pyautogui
import time

width, height = pyautogui.size()


def pris(pre, swi, mode,flagMode=0):
    if flagMode:
        dothis = False
        preResult = pre['sorted_predictions'][0][0]
        try:
            if (preResult == "roll"):
                if swi["roll"] == 0:
                    swi["roll"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["roll"] > 2):
                        dothis = True
                        swi["roll"] = time.time()
            if (preResult == "Covering ears"):
                if swi["Covering ears"] == 0:
                    swi["Covering ears"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Covering ears"] > 2):
                        dothis = True
                        swi["Covering ears"] = time.time()
            if (preResult == "Covering eyes"):
                if swi["Covering eyes"] == 0:
                    swi["Covering eyes"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Covering eyes"] > 2):
                        dothis = True
                        swi["Covering eyes"] = time.time()
            if (preResult == "Pointing to the camera"):
                if swi["Pointing to the camera"] == 0:
                    swi["Pointing to the camera"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Pointing to the camera"] > 2):
                        dothis = True
                        swi["Pointing to the camera"] = time.time()
            if (preResult == "Putting finger to mouth"):
                if swi["Putting finger to mouth"] == 0:
                    swi["Putting finger to mouth"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Putting finger to mouth"] > 2):
                        dothis = True
                        swi["Putting finger to mouth"] = time.time()
            if (preResult == "Rolling hand"):
                if swi["Rolling hand"] == 0:
                    swi["Rolling hand"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Rolling hand"] > 2):
                        dothis = True
                        swi["Rolling hand"] = time.time()
            if (preResult == "Scratching"):
                if swi["Scratching"] == 0:
                    swi["Scratching"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Scratching"] > 2):
                        dothis = True
                        swi["Scratching"] = time.time()
            if (preResult == "Shaking head"):
                if swi["Shaking head"] == 0:
                    swi["Shaking head"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Shaking head"] > 2):
                        dothis = True
                        swi["Shaking head"] = time.time()
            if (preResult == "left"):
                if swi["left"] == 0:
                    swi["left"] = time.time()
                    dothis = True
                else:
                    if ((time.time() - swi["right"] > 4)
                            and (time.time() - swi["left"] > 4)):
                        dothis = True
                        swi["left"] = time.time()
            if (preResult == "right"):
                if swi["right"] == 0:
                    swi["right"] = time.time()
                    dothis = True
                else:
                    if ((time.time() - swi["right"] > 4)
                            and (time.time() - swi["left"] > 4)):
                        dothis = True
                        swi["right"] = time.time()
            if (preResult == "Swiping up"):
                if swi["Swiping up"] == 0:
                    swi["Swiping up"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Swiping up"] > 2):
                        dothis = True
                        swi["Swiping up"] = time.time()
            if (preResult == "up"):
                if swi["up"] == 0:
                    swi["up"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["up"] > 2):
                        dothis = True
                        swi["up"] = time.time()
            if (preResult == "Waving"):
                if swi["Waving"] == 0:
                    swi["Waving"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Waving"] > 2):
                        dothis = True
                        swi["Waving"] = time.time()
            if (preResult == "down"):
                if swi["down"] == 0:
                    swi["down"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["down"] > 2):
                        dothis = True
                        swi["down"] = time.time()
            if (preResult == "Nodding"):
                if swi["Nodding"] == 0:
                    swi["Nodding"] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi["Nodding"] > 2):
                        dothis = True
                        swi["Nodding"] = time.time()
            if (preResult == 'point'):
                if swi['point'] == 0:
                    swi['point'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['point'] > 2):
                        dothis = True
                        swi['point'] = time.time()
            if (preResult == 'Thumup'):
                if swi['Thumup'] == 0:
                    swi['Thumup'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['Thumup'] > 2):
                        dothis = True
                        swi['Thumup'] = time.time()

            if (preResult == 'scatch'):
                if swi['scatch'] == 0:
                    swi['scatch'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['scatch'] > 2):
                        dothis = True
                        swi['scatch'] = time.time()

            if (preResult == 'narrow'):
                if swi['narrow'] == 0:
                    swi['narrow'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['narrow'] > 2):
                        dothis = True
                        swi['narrow'] = time.time()

            if (preResult == 'left'):
                if swi['left'] == 0:
                    swi['left'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['left'] > 0.5):
                        dothis = True
                        swi['left'] = time.time()

            if (preResult == 'right'):
                if swi['right'] == 0:
                    swi['right'] = time.time()
                    dothis = True
                else:
                    if (time.time() - swi['right'] > 0.5):
                        dothis = True
                        swi['right'] = time.time()

            #mode = 0 PPT
            if mode == 0:


                if (preResult == 'Pointing to the camera' and dothis):
                    pyautogui.click(10, 10, button='left')

                if (preResult == 'down' and dothis):
                    pyautogui.hotkey('volumedown')

                if (preResult == 'up' and dothis):
                    pyautogui.hotkey('volumeup')

                if (preResult == 'Putting finger to mouth' and dothis):
                    pyautogui.hotkey('volumemute')

                if (preResult == 'left' and dothis):
                    pyautogui.hotkey('left')


                if (preResult == 'right' and dothis):
                    pyautogui.hotkey('right')


                if (preResult == 'point' and dothis):
                    pyautogui.hotkey('shift', 'F5')

                if (preResult == 'scatch' and dothis):
                    pyautogui.hotkey('ctrlleft', '-')

                if (preResult == 'narrow' and dothis):
                    pyautogui.hotkey('ctrlleft', '=')

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')
                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')
            #mode = 1 Word
            if mode == 1:

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')

                if (preResult == 'scatch' and dothis):
                    pyautogui.keyDown('ctrl')  # 按下shift
                    pyautogui.scroll(10)
                    pyautogui.keyUp('ctrl')  # 释放 shift

                if (preResult == 'narrow' and dothis):
                    pyautogui.keyDown('ctrl')  # 按下shift
                    pyautogui.scroll(-10)
                    pyautogui.keyUp('ctrl')  # 释放 shift

                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')

            #mode = 2 视频
            if mode == 2:
                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')

                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')

                if (preResult == 'right' and dothis):
                    pyautogui.hotkey('right')

                if (preResult == 'left' and dothis):
                    pyautogui.hotkey('left')

                if (preResult == 'Pointing to the camera' and dothis):
                    pyautogui.hotkey('space')

                if (preResult == 'down' and dothis):
                    pyautogui.hotkey('volumedown')

                if (preResult == 'up' and dothis):
                    pyautogui.hotkey('volumeup')
                if (preResult == 'Putting finger to mouth' and dothis):
                    pyautogui.hotkey('volumemute')

                # if (preResult == 'left' and dothis):
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #
                # if (preResult == 'right' and dothis):
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                if (preResult == 'point' and dothis):
                    im = pyautogui.screenshot()

                    im.save('屏幕截图.png')

            #mode = 3 地图
            if mode == 3:
                if (preResult == 'right' and dothis):
                    pyautogui.hotkey('right')

                if (preResult == 'left' and dothis):
                    pyautogui.hotkey('left')
                if (preResult == 'point' and dothis):
                    im = pyautogui.screenshot()

                    im.save('屏幕截图.png')

                if (preResult == 'down' and dothis):
                    pyautogui.hotkey('down')

                if (preResult == 'up' and dothis):
                    pyautogui.hotkey('up')

                if (preResult == 'left' and dothis):
                    pyautogui.hotkey('left')

                if (preResult == 'right' and dothis):
                    pyautogui.hotkey('right')

                if (preResult == 'scatch' and dothis):
                    pyautogui.hotkey('-')

                if (preResult == 'narrow' and dothis):
                    pyautogui.hotkey('=')

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')
                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')
            #mode = 4 3D模型
            if mode == 4:
                # if (preResult == 'right' and dothis):
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')
                #
                # if (preResult == 'left' and dothis):
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')


                if (preResult == 'down' and dothis):
                    pyautogui.dragRel(xOffset=0, yOffset=-100, button='left', mouseDownUp=False)

                if (preResult == 'up' and dothis):
                    pyautogui.dragRel(xOffset=0, yOffset=100, button='left', mouseDownUp=False)


                if (preResult == 'left' and dothis):
                    pyautogui.dragRel(xOffset=100, yOffset=0, button='left', mouseDownUp=False)

                if (preResult == 'right' and dothis):
                    pyautogui.dragRel(xOffset=-100, yOffset=0, button='left', mouseDownUp=False)

                if (preResult == 'scatch' and dothis):
                    pyautogui.scroll(-10)

                if (preResult == 'narrow' and dothis):
                    pyautogui.scroll(10)

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')
                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')
            #mode = 5 focusky
            if mode == 5:
                if (preResult == 'right' and dothis):
                    pyautogui.hotkey('right')

                if (preResult == 'left' and dothis):
                    pyautogui.hotkey('left')

                if (preResult == 'Pointing to the camera' and dothis):
                    pyautogui.click(10, 10, button='left')

                if (preResult == 'down' and dothis):
                    pyautogui.hotkey('volumedown')

                if (preResult == 'up' and dothis):
                    pyautogui.hotkey('volumeup')

                if (preResult == 'Putting finger to mouth' and dothis):
                    pyautogui.hotkey('volumemute')

                # if (preResult == 'left' and dothis):
                #     pyautogui.hotkey('left')
                #     pyautogui.hotkey('left')
                #
                # if (preResult == 'right' and dothis):
                #     pyautogui.hotkey('right')
                #     pyautogui.hotkey('right')

                if (preResult == 'point' and dothis):
                    pyautogui.hotkey('shift', 'F5')

                if (preResult == 'scatch' and dothis):
                    pyautogui.hotkey('ctrlleft', '-')

                if (preResult == 'narrow' and dothis):
                    pyautogui.hotkey('ctrlleft', '=')

                if (preResult == 'roll' and dothis):
                    pyautogui.hotkey('altleft', 'tab')
                if (preResult == 'Thumup' and dothis):
                    pyautogui.hotkey('altleft', 'F4')

        except:
            pass
    else:
        pass