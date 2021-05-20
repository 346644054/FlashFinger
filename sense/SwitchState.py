import win32gui
import fnmatch
hwnd_title = dict()

def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

def switchSt():
    win32gui.EnumWindows(get_all_hwnd, 0)

    for h, t in hwnd_title.items():
        if t is not "":
            if fnmatch.fnmatch(t, '* - PowerPoint'):
                return 0
            if fnmatch.fnmatch(t, '* - Word'):
                return 1
            if fnmatch.fnmatch(t, '迅雷影音') or fnmatch.fnmatch(t, '电影和电视') or fnmatch.fnmatch(t, 'Windows Media Player'):
                return 2
            if fnmatch.fnmatch(t, '*地图 - Google Chrome') or fnmatch.fnmatch(t, '*地图 - Microsoft​ Edge'):
                return 3
            if fnmatch.fnmatch(t, '* - SolidWorks') or fnmatch.fnmatch(t, '*平台 - Google Chrome'):
                return 4
            if fnmatch.fnmatch(t, 'Focusky'):
                return 5






