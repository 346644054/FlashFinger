import wx
import telnetlib
from time import sleep
import _thread as thread
import random
import threading

from wx.core import Position
import Mywxpython

global meetingnum
from tools.run_custom_classifier import run_my_claasfier
import pyautogui as gui
from sense.SwitchState import get_all_hwnd
import win32gui
import fnmatch
import win32con
import sense.functin_real as fun
import sense.SwitchState as switch
import time
global state
state = 0
global votetimer
import webbrowser
from selenium import webdriver
import os
class MainPanel(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(15, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")


        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.userName = wx.TextCtrl(self, pos=(
            922, 400), size=(280, 22), style=wx.NO_BORDER)

        self.userName.SetFont(font1)
        self.userName.SetDefaultStyle(wx.TextAttr("#CDCBCA"))
        self.userName.SetBackgroundColour("#FDFCF9")
        # 服务器地址框
        self.serverAddress = wx.TextCtrl(self, pos=(922, 470), size=(
            280, 22), style=wx.NO_BORDER | wx.TE_PROCESS_ENTER)
        self.serverAddress.SetFont(font1)
        self.serverAddress.SetDefaultStyle(wx.TextAttr("#CDCBCA"))
        self.serverAddress.SetBackgroundColour("#FDFCF9")
        self.serverAddress.Bind(wx.EVT_TEXT_ENTER, self.login)
        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/register ture.png', wx.BITMAP_TYPE_PNG)
        self.Create_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(187, 53), pos=(1040, 580))
        self.Create_Button.SetBackgroundColour("#FDFCF9")
        self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.create, self.Create_Button)

        bmp = wx.Bitmap('image/lo_true.png', wx.BITMAP_TYPE_PNG)
        self.Login_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(187, 53), pos=(836, 580))
        self.Login_Button.SetBackgroundColour("#FDFCF9")
        self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.login, self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/login_true.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)

    def create(self, event):
         # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()
            if str(self.userName.GetLineText(0)) == "":
                self.showDialog('Error', '用户名不能为空!', (200, 100))
            if str(self.serverAddress.GetLineText(0)) == "":
                self.showDialog('Error', '密码不能为空!', (200, 100))
            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('create ' + str(self.userName.GetLineText(0))+"$$" +
                       str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            # self.showDialog("ajfidj", response, (800, 100))
            if response == '用户名重复'.encode('utf-8'):
                self.showDialog('Error', '用户名重复!', (200, 100))
            # elif response == '用户名已存在':
            #     self.showDialog('Error', '用户名已存在!', (200, 100))
            else:
                self.showDialog('Congratulation', '注册成功!', (195, 120))
                self.frame.Close()
                self.Destroy()
                MainPageFrame()

        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def login(self, event):
        # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()

            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('login ' + str(self.userName.GetLineText(0))+"$$" +
                       str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()

            if response == '密码不正确'.encode('utf-8'):
                self.showDialog('Error', '密码不正确!', (200, 100))
            elif response == '无此用户名'.encode('utf-8'):
                self.showDialog('Error', '无此用户!', (200, 100))
            else:
                self.frame.Close()
                self.Destroy()
                MainPageFrame()

                # ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()


class LoginFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 816))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = MainPanel(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()


class MainPage(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")
        # #服务器地址框
    #     self.serverAddress = wx.TextCtrl(self, pos=(922,460), size=(280, 42),style = wx.NO_BORDER)
    #     self.serverAddress.SetFont(font1)
    #     self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.BLACK))
    #     self.serverAddress.SetBackgroundColour("#FDFCF9")

        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.userName = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.userName.SetFont(font1)
        self.userName.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.userName.SetBackgroundColour("#FFFFFF")

        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/create.png', wx.BITMAP_TYPE_PNG)
        self.CreateRoom_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(135, 33), pos=(190, 379))
        self.CreateRoom_Button.SetBackgroundColour("#FFFFFF")
        self.CreateRoom_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.createpagebutton, self.CreateRoom_Button)
        bmp = wx.Bitmap('image/join.png', wx.BITMAP_TYPE_PNG)
        self.JoinRoom_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(135, 33), pos=(738, 379))
        self.JoinRoom_Button.SetBackgroundColour("#FFFFFF")
        self.JoinRoom_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.joinpagebutton, self.JoinRoom_Button)
        bmp = wx.Bitmap('image/test.png', wx.BITMAP_TYPE_PNG)
        self.Test_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(137, 33), pos=(190, 690))
        self.Test_Button.SetBackgroundColour("#FFFFFF")
        self.Test_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.opentest,self.Test_Button)
        bmp = wx.Bitmap('image/custom.png', wx.BITMAP_TYPE_PNG)
        self.Custom_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 34), pos=(738, 690))
        self.Custom_Button.SetBackgroundColour("#FFFFFF")
        self.Custom_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.custom,self.Custom_Button)

        bmp = wx.Bitmap('image/meettime.png', wx.BITMAP_TYPE_PNG)
        self.MeetTime_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(99, 15), pos=(190, 450))
        self.MeetTime_Button.SetBackgroundColour("#FFFFFF")
        self.MeetTime_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.MeetTime_Button)
        bmp = wx.Bitmap('image/upload.png', wx.BITMAP_TYPE_PNG)
        self.UpLoad_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(66, 15), pos=(370, 450))
        self.UpLoad_Button.SetBackgroundColour("#FFFFFF")
        self.UpLoad_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.UpLoad_Button)
        bmp = wx.Bitmap('image/roomnum.png', wx.BITMAP_TYPE_PNG)
        self.RoomNum_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(49, 15), pos=(550, 450))
        self.RoomNum_Button.SetBackgroundColour("#FFFFFF")
        self.RoomNum_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.RoomNum_Button)
        bmp = wx.Bitmap('image/roomnum.png', wx.BITMAP_TYPE_PNG)
        self.RoomNum_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(49, 15), pos=(768, 450))
        self.RoomNum_Button1.SetBackgroundColour("#FFFFFF")
        self.RoomNum_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.RoomNum_Button1)
        bmp = wx.Bitmap('image/upload.png', wx.BITMAP_TYPE_PNG)
        self.UpLoad_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(66, 15), pos=(920, 450))
        self.UpLoad_Button2.SetBackgroundColour("#FFFFFF")
        self.UpLoad_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.UpLoad_Button2)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/mainpage.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)
    def custom(self,event):
        SelfPageFrame1()
        self.frame.Close()
    def opentest(self,event):

        current_path = os.path.abspath(__file__)
        # webbrowser.open(current_path+"demo/index.html")
        webbrowser.open(".\\demo\\index.html")
        t2 = threading.Thread(target=run_my_claasfier)
        #
        t2.start()


    def createpagebutton(self, event):

        CreateRoomPageFrame()
        self.frame.Close()
    def joinpagebutton(self, event):

        JoinRoomPageFrame()
        self.frame.Close()
    def create(self, event):
         # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()

            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('create ' + str(self.userName.GetLineText(0))+"$$" +
                       str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            # self.showDialog("ajfidj", response, (800, 100))
            if response == '用户名重复'.encode('utf-8'):
                self.showDialog('Error', '用户名重复!', (200, 100))
            # elif response == '用户名已存在':
            #     self.showDialog('Error', '用户名已存在!', (200, 100))
            else:
                self.showDialog('Congratulation', '注册成功!', (195, 120))
                
                MainPageFrame()
                self.frame.Close()
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def login(self, event):
        # 登录处理
        try:
            Address = "47.98.40.28:8000"
            serverAddress = Address.split(':')
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)
            response = con.read_some()

            if response != '连接成功'.encode('utf-8'):
                self.showDialog('Error', '连接失败!', (200, 100))
                return
            con.write(('login ' + str(self.userName.GetLineText(0))+"$$" +
                       str(self.serverAddress.GetLineText(0)) + '\n').encode("utf-8"))
            response = con.read_some()
            # self.showDialog('Error', response, (800, 100))
            if response == '密码不正确'.encode('utf-8'):
                self.showDialog('Error', '密码不正确!', (200, 100))
            elif response == '无此用户名'.encode('utf-8'):
                self.showDialog('Error', '无此用户!', (200, 100))
            else:
                
                MainPageFrame()
                self.frame.Close()
                # ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()


class MainPageFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = MainPage(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()


class CreateRoomPage(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")
        # #服务器地址框
    #     self.serverAddress = wx.TextCtrl(self, pos=(922,460), size=(280, 42),style = wx.NO_BORDER)
    #     self.serverAddress.SetFont(font1)
    #     self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.BLACK))
    #     self.serverAddress.SetBackgroundColour("#FDFCF9")

        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.Search = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.Search.SetFont(font1)
        self.Search.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.Search.SetBackgroundColour("#FFFFFF")
    # 会议名称地址框
        self.MeetName = wx.TextCtrl(self, pos=(
            560, 385), size=(280, 27), style=wx.NO_BORDER)
        self.MeetName.SetFont(font1)
        self.MeetName.SetDefaultStyle(wx.TextAttr("#CDCBCA"))
        self.MeetName.SetBackgroundColour("#FAFCFD")

        # self.MeetName.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 会议编码框
        self.MeetNum = wx.TextCtrl(self, pos=(560, 455), size=(
            280, 27), style=wx.NO_BORDER | wx.TE_PROCESS_ENTER)

        self.MeetNum.SetFont(font1)
        self.MeetNum.SetDefaultStyle(wx.TextAttr("#CDCBCA"))
        self.MeetNum.SetBackgroundColour("#FAFCFD")
        self.MeetNum.Bind(wx.EVT_TEXT_ENTER, self.createmeeting)

        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/return.png', wx.BITMAP_TYPE_PNG)
        self.Return_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(56,20), pos=(163, 178))
        self.Return_Button.SetBackgroundColour("#FFFFFF")
        self.Return_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.returnto,self.Return_Button)


        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/createroom2.png', wx.BITMAP_TYPE_PNG)
        self.CreateRoom_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(250, 59), pos=(560, 580))
        self.CreateRoom_Button.SetBackgroundColour("#FFFFFF")
        self.CreateRoom_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.createmeeting, self.CreateRoom_Button)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/createroom.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)

    def createmeeting(self, event):
        # 登录处理
        try:
            global meetingnum
            con.write(
                ('creatm ' + str(self.MeetNum.GetLineText(0)) + '\n').encode("utf-8"))
            meetingnum = str(self.MeetNum.GetLineText(0))
            response = con.read_some()
            response = con.read_some()
            response = con.read_some()

# 测试##########
        # self.showDialog('Error', response, (800, 100))
# 测试##########
            if response == '会议号已存在'.encode('utf-8'):
                self.showDialog('Error', '会议号已存在!', (200, 100))
            elif response == '用户名已存在':
                self.showDialog('Error', '用户名已存在!', (200, 100))
            else:

                # ChatFrame(None, 2, title='QT聊天室', size=(500, 400))

                self.frame.OnClose(self)
                ToolFrameS()

                t5 = threading.Thread(target=run_my_claasfier,args=(1,))
                #
                t5.start()

                win32gui.EnumWindows(get_all_hwnd, 0)
                hwnd_title = dict()
                time.sleep(0.7)
                hld = win32gui.FindWindow(None, u'Real-time SenseNet')
                print(hld)
                win32gui.ShowWindow(hld, win32con.SW_HIDE)
        except Exception:
            self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()
    def returnto(self,event):
        self.frame.OnClose(self)
        MainPageFrame()


class CreateRoomPageFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = CreateRoomPage(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()


class JoinRoomPage(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")
        # #服务器地址框
    #     self.serverAddress = wx.TextCtrl(self, pos=(922,460), size=(280, 42),style = wx.NO_BORDER)
    #     self.serverAddress.SetFont(font1)
    #     self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.BLACK))
    #     self.serverAddress.SetBackgroundColour("#FDFCF9")

        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.Search = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.Search.SetFont(font1)
        self.Search.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.Search.SetBackgroundColour("#FFFFFF")

        # 会议编码框
        self.MeetNum = wx.TextCtrl(self, pos=(560, 445), size=(
            280, 27), style=wx.NO_BORDER | wx.TE_PROCESS_ENTER)

        self.MeetNum.SetFont(font1)
        self.MeetNum.SetDefaultStyle(wx.TextAttr("#CDCBCA"))
        self.MeetNum.SetBackgroundColour("#FAFCFD")
        self.MeetNum.Bind(wx.EVT_TEXT_ENTER, self.joinmeeting)

        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/return.png', wx.BITMAP_TYPE_PNG)
        self.Return_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(56,20), pos=(163, 178))
        self.Return_Button.SetBackgroundColour("#FFFFFF")
        self.Return_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.returnto,self.Return_Button)

        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/joinroom2.png', wx.BITMAP_TYPE_PNG)
        self.JoinRoom_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(250, 59), pos=(560, 580))
        self.JoinRoom_Button.SetBackgroundColour("#FFFFFF")
        self.JoinRoom_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.joinmeeting, self.JoinRoom_Button)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/joinroompage.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)
    def returnto(self,event):
        self.frame.OnClose(self)
        MainPageFrame()
    def joinmeeting(self, event):
        # 登录处理
        # try:
        global meetingnum
        con.write(
            ('join ' + str(self.MeetNum.GetLineText(0)) + '\n').encode("utf-8"))
        response = con.read_some()
        response = con.read_some()
        response = con.read_some()
        meetingnum = str(self.MeetNum.GetLineText(0))
# 测试##########
        # self.showDialog('Error', response, (800, 100))
# 测试##########
#         self.showDialog('Error', response.decode("utf-8"), (800, 100))
        if response == '会议号不存在'.encode('utf-8'):
            self.showDialog('Error', '会议号不存在!', (200, 100))
        elif response == '奇怪问题':
            self.showDialog('Error', '奇怪问题!', (200, 100))
        else:
           
            # ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
            ToolFrameL()
            self.frame.Close()
        # except Exception:
            # self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()


class JoinRoomPageFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = JoinRoomPage(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()

class SelfPage1(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
    
        # 用户名框
        self.Search = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.Search.SetFont(font1)
        self.Search.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.Search.SetBackgroundColour("#FFFFFF")



        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/return1.png', wx.BITMAP_TYPE_PNG)
        self.Return_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(56,20), pos=(163, 178))
        self.Return_Button.SetBackgroundColour("#FFFFFF")
        self.Return_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.returnto,self.Return_Button)


        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/saveas.png', wx.BITMAP_TYPE_PNG)
        self.Save_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=( 889,794))
        self.Save_Button.SetBackgroundColour("#FFFFFF")
        self.Save_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.joinmeeting, self.Save_Button)

        bmp = wx.Bitmap('image/next.png', wx.BITMAP_TYPE_PNG)
        self.Next_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=(1066,794))
        self.Next_Button.SetBackgroundColour("#FFFFFF")
        self.Next_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.next, self.Next_Button)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/self1.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)
    def next(self,event):
        SelfPageFrame2()
        self.frame.OnClose(self)

    def returnto(self,event):
        self.frame.OnClose(self)
        MainPageFrame()

  


class SelfPageFrame1(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = SelfPage1(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()

class SelfPage2(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")
        # #服务器地址框
    #     self.serverAddress = wx.TextCtrl(self, pos=(922,460), size=(280, 42),style = wx.NO_BORDER)
    #     self.serverAddress.SetFont(font1)
    #     self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.BLACK))
    #     self.serverAddress.SetBackgroundColour("#FDFCF9")

        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.Search = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.Search.SetFont(font1)
        self.Search.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.Search.SetBackgroundColour("#FFFFFF")


        bmp = wx.Bitmap('image/return1.png', wx.BITMAP_TYPE_PNG)
        self.Return_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(56,20), pos=(163, 178))
        self.Return_Button.SetBackgroundColour("#FFFFFF")
        self.Return_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.returnto,self.Return_Button)

        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/saveas.png', wx.BITMAP_TYPE_PNG)
        self.Save_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=( 889,794))
        self.Save_Button.SetBackgroundColour("#FFFFFF")
        self.Save_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.joinmeeting, self.Save_Button)

        bmp = wx.Bitmap('image/next.png', wx.BITMAP_TYPE_PNG)
        self.Next_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=(1066,794))
        self.Next_Button.SetBackgroundColour("#FFFFFF")
        self.Next_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.next, self.Next_Button)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/self2.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)
    def next(self,event):
        self.frame.OnClose(self)
        SelfPageFrame3()
    def returnto(self,event):
        self.frame.OnClose(self)
        MainPageFrame()
  


class SelfPageFrame2(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = SelfPage2(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()
class SelfPage3(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
    # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # #服务器地址框标签
    #     self.serverAddressLabel = Mywxpython.TransparentStaticText(self, label="密码", pos=(130, 155), size=(120, 25))
    #     self.serverAddressLabel.SetFont(labelfont)
    #     self.serverAddressLabel.SetForegroundColour("#ffffff")
        # #用户名框标签
    #     self.userNameLabel = Mywxpython.TransparentStaticText(self, label="用户名", pos=(120, 105), size=(120, 25))
    #     self.userNameLabel.SetFont(labelfont)
    #     self.userNameLabel.SetForegroundColour("#ffffff")
        # #服务器地址框
    #     self.serverAddress = wx.TextCtrl(self, pos=(922,460), size=(280, 42),style = wx.NO_BORDER)
    #     self.serverAddress.SetFont(font1)
    #     self.serverAddress.SetDefaultStyle(wx.TextAttr(wx.BLACK))
    #     self.serverAddress.SetBackgroundColour("#FDFCF9")

        # self.serverAddress.Bind(wx.EVT_TEXT_ENTER,self.create)
        # 用户名框
        self.Search = wx.TextCtrl(self, pos=(
            55, 100), size=(500, 22), style=wx.NO_BORDER)

        self.Search.SetFont(font1)
        self.Search.SetDefaultStyle(wx.TextAttr(wx.BLACK))
        self.Search.SetBackgroundColour("#FFFFFF")



        # #登录按钮
    #     self.createButton = wx.Button(self, label='注册', pos=(100, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.createButton.Bind(wx.EVT_BUTTON, self.create)

        # #登录按钮
    #     self.loginButton = wx.Button(self, label='登录', pos=(170, 155), size=(60, 30))
    #     #登录按钮上绑定登录方法
    #     self.loginButton.Bind(wx.EVT_BUTTON, self.login)

        bmp = wx.Bitmap('image/return1.png', wx.BITMAP_TYPE_PNG)
        self.Return_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(56,20), pos=(163, 178))
        self.Return_Button.SetBackgroundColour("#FFFFFF")
        self.Return_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.returnto,self.Return_Button)

        bmp = wx.Bitmap('image/aboutus.png', wx.BITMAP_TYPE_PNG)
        self.About_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(138, 55), pos=(1140, 14))
        self.About_Button.SetBackgroundColour("#FFFFFF")
        self.About_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button)

        bmp = wx.Bitmap('image/menu1.png', wx.BITMAP_TYPE_PNG)
        self.About_Button1 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1160, 90))
        self.About_Button1.SetBackgroundColour("#FFFFFF")
        self.About_Button1.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button1)
        bmp = wx.Bitmap('image/menu2.png', wx.BITMAP_TYPE_PNG)
        self.About_Button2 = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(1210, 90))
        self.About_Button2.SetBackgroundColour("#FFFFFF")
        self.About_Button2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.About_Button2)
        bmp = wx.Bitmap('image/search.png', wx.BITMAP_TYPE_PNG)
        self.Search_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(41, 41), pos=(10, 90))
        self.Search_Button.SetBackgroundColour("#FFFFFF")
        self.Search_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Search_Button)

        bmp = wx.Bitmap('image/leftbar1.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar1_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 73), pos=(0, 140))
        self.Leftbar1_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar1_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar1_Button)
        bmp = wx.Bitmap('image/leftbar2.png', wx.BITMAP_TYPE_PNG)
        self.Leftbar2_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(80, 65), pos=(0, 215))
        self.Leftbar2_Button.SetBackgroundColour("#FFFFFF")
        self.Leftbar2_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.about,self.Leftbar2_Button)

        bmp = wx.Bitmap('image/saveas.png', wx.BITMAP_TYPE_PNG)
        self.Save_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=( 889,794))
        self.Save_Button.SetBackgroundColour("#FFFFFF")
        self.Save_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.joinmeeting, self.Save_Button)

        bmp = wx.Bitmap('image/close.png', wx.BITMAP_TYPE_PNG)
        self.Next_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(152, 33), pos=(1066,794))
        self.Next_Button.SetBackgroundColour("#FFFFFF")
        self.Next_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.next, self.Next_Button)

        # bmp = wx.Bitmap('register ture.png', wx.BITMAP_TYPE_PNG)
        # self.Create_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(1040, 580))
        # self.Create_Button.SetBackgroundColour("#FFFFFF")
        # self.Create_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.create,self.Create_Button)

        # bmp = wx.Bitmap('lo_true.png', wx.BITMAP_TYPE_PNG)
        # self.Login_Button = wx.BitmapButton(self, -1, bmp ,style = wx.NO_BORDER,size = (187,53),pos=(836, 580))
        # self.Login_Button.SetBackgroundColour("#FFFFFF")
        # self.Login_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        # self.Bind(wx.EVT_BUTTON, self.login,self.Login_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/self3.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)
    def next(self,event):
        MainPageFrame()
        self.frame.OnClose(self)
    def returnto(self,event):
        self.frame.OnClose(self)
        MainPageFrame()

  


class SelfPageFrame3(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        wx.Frame.__init__(self, None, -1, "Flash Finger", size=(1280, 886))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        panel = SelfPage3(self)
        # 图案按钮！！！！！！！！！！！！！！！
        # bmp = wx.Bitmap('close.png', wx.BITMAP_TYPE_PNG)
        # self.Close_Button = wx.BitmapButton(panel, -1, bmp ,size = (30,26),pos=(450,0))
        # self.Close_Button.SetBackgroundColour("#3D485A")
        # self.Bind(wx.EVT_BUTTON, self.OnClose,self.Close_Button)

        self.Center()

        self.Show()

    def OnClose(self, event):
        self.Destroy()


class ToolPage(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent, size=(300, 79))

        self.frame = parent

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font1 = wx.Font(16, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        bmp = wx.Bitmap('image/change.png', wx.BITMAP_TYPE_PNG)
        self.Change_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(39, 39), pos=(0, 0))
        self.Change_Button.SetBackgroundColour("#FFFFFF")
        self.Change_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.Change_Button)

    # ----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/toolbar.png")
        dc.DrawBitmap(bmp, 0, 0)

    # 显示组件

    # def OnEraseBack(self,event):
    #     dc = event.GetDC()
    #     if not dc:
    #         dc = wx.ClientDC(self)
    #         rect = self.GetUpdateRegion().GetBox()
    #         dc.SetClippingRect(rect)
    #     dc.Clear()
    #     bmp = wx.Bitmap("shangwu.png")

    #     dc.DrawBitmap(bmp, 0, 0)

    def joinmeeting(self, event):
        # 登录处理
        # try:
        global meetingnum
        con.write(
            ('join ' + str(self.MeetNum.GetLineText(0)) + '\n').encode("utf-8"))
        meetingnum = str(self.MeetNum.GetLineText(0))
        response = con.read_some()
# 测试##########
        # self.showDialog('Error', response, (800, 100))
# 测试##########
        if response == '会议号不存在'.encode('utf-8'):
            self.showDialog('Error', '会议号不存在!', (200, 100))
        elif response == '奇怪问题':
            self.showDialog('Error', '奇怪问题!', (200, 100))
        else:
            
            ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
            self.frame.Close()
        # except Exception:
            # self.showDialog('Error', '连接失败!', (195, 120))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()

    def OnClose(self, event):
        self.frame.Destroy()


class ToolFrameS(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        super().__init__(parent=None, style=wx.STAY_ON_TOP | wx.FRAME_SHAPED, size=(300, 79))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        font1 = wx.Font(14, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        global mode
        mode = 0
        global controller
        controller = ""

        self.bg = wx.Bitmap("image/toolbar.png", wx.BITMAP_TYPE_PNG)
        region = wx.Region(self.bg)
        self.SetShape(region)

        bmp = wx.Bitmap('image/change.png', wx.BITMAP_TYPE_PNG)
        Vote_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(37, 37), pos=(240, 8))
        Vote_Button.SetBackgroundColour("#FFFFFF")
        Vote_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.OnVote, Vote_Button)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.ModeText = Mywxpython.TransparentStaticText(
            self, label="演讲者模式", pos=(120, 16))
        self.ModeText.SetFont(font1)
        self.ModeText.SetForegroundColour("#ffffff")
        self.ModeText.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.ModeText.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.ModeText.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        thread.start_new_thread(self.receive, ())

        self.Center()
        self.Show()

    def OnVote(self,event):
        global meetingnum
        global votetimer
        con.write(('vote ' + str(meetingnum) + '\n').encode("utf-8"))
        self.ModeText.SetLabel("投票进行中")
        votetimer = time.time()

    def receive(self):
        # 接受服务器的消息
        global meetingnum
        global votetimer
        while True:
            sleep(0.6)
            # 在I/O中读取数据，存在result变量中
            result = con.read_very_eager()
            result = result.decode("utf-8")

            result = result.split("\n")
            speakmode = str(self.ModeText.GetLabel())
            nowtime = time.time()
            if "投票进行中" in speakmode:
                if (nowtime - votetimer) > 60:
                    self.ModeText.SetLabel("演讲者模式")
            if speakmode == "演讲者模式":
                if result[0] == "controlrequest:":
                    if meetingnum == result[2]:
                        controller = result[1]
                        self.ModeText.SetLabel("受控模式")
                        win32gui.EnumWindows(get_all_hwnd, 0)
                        hwnd_title = dict()
                        hld = win32gui.FindWindow(None, u'Real-time SenseNet')
                        print(hld)
                        if win32gui.IsIconic(hld):
                            win32gui.ShowWindow(hld, win32con.SW_SHOWMAXIMIZED)
                        win32gui.SetForegroundWindow(hld)
                        gui.hotkey('esc')
                        print("here")
                

            if speakmode == "受控模式":
                if result[0] == "controlaction:":
                    if result[1] == controller:

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
                            "Thumb up": 0,
                            "Waving": 0,
                            "Zooming in": 0,
                            "Zooming out": 0,
                            "byebye": 0,
                            "down": 0,
                            "do_other_thing": 0,
                            "left": 0,
                            "narrow": 0,
                            "point": 0,
                            "right": 0,
                            "roll": 0,
                            "scatch": 0,
                            "up": 0
                        }
                        # 调用检测当前窗口函数，返回值为mode
                        # mode = 0 PPT
                        # mode = 1 Word
                        # mode = 2 视频
                        # mode = 3 地图
                        # mode = 4 3D模型
                        # mode = 5 focusky
                        mode = switch.switchSt()
                        fun.pris(result[2], swi, mode)
            if "票" in speakmode:
                if result[0] == "voteresult:":
                    if meetingnum == result[2]:
                        self.ModeText.SetLabel("票数为"+result[1])
    def OnRightClickEvent(self, event):
        state = 1  ####################################################################
        '''win32gui.EnumWindows(get_all_hwnd, 0)
        hwnd_title = dict()
        hld = win32gui.FindWindow(None, u'Real-time SenseNet')
        print(hld)
        win32gui.SetForegroundWindow(hld)
        win32gui.SetForegroundWindow(hld)
        print("here")
        gui.press('esc')'''

        self.OnClose(self)
        # print(threading.current_thread().__class__.__name__)
        # gui.hotkey('Esc')
        win32gui.EnumWindows(get_all_hwnd, 0)
        hwnd_title = dict()
        hld = win32gui.FindWindow(None, u'Real-time SenseNet')
        print(hld)
        if win32gui.IsIconic(hld):
            win32gui.ShowWindow(hld, win32con.SW_SHOWMAXIMIZED)
        win32gui.SetForegroundWindow(hld)
        gui.hotkey('esc')
        print("here")

        MainPageFrame()

    def OnPaint(self, event):
        mydc = wx.PaintDC(self)
        mydc.DrawBitmap(self.bg, 0, 0, True)

    def OnLeftClickDown(self, event):
        self.pt = event.GetPosition()

    def OnClose(self, event):
        self.Destroy()

    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            self.Move((pos.x-self.pt.x, pos.y-self.pt.y))


class ToolFrameL(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        # real_resolution = zoom.get_real_resolution()
        # screen_size = zoom.get_screen_size()

        # screen_scale_rate = round(screen_size[0] / 1950, 2)
        # screen_scale_rate1 = round(screen_size[1] / 1060, 2)

        super().__init__(parent=None, style=wx.STAY_ON_TOP | wx.FRAME_SHAPED, size=(300, 79))
        self.icon = wx.Icon("image/logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        font1 = wx.Font(14, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD,
                        underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        mode = 0

        self.bg = wx.Bitmap("image/toolbar.png", wx.BITMAP_TYPE_PNG)
        region = wx.Region(self.bg)
        self.SetShape(region)

        #测试##########################################################################
        bmp = wx.Bitmap('image/change.png', wx.BITMAP_TYPE_PNG)
        Change_Button = wx.BitmapButton(
            self, -1, bmp, style=wx.NO_BORDER, size=(37, 37), pos=(235, 8))
        Change_Button.SetBackgroundColour("#FFFFFF")
        Change_Button.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.Bind(wx.EVT_BUTTON, self.test, Change_Button)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.ModeText = Mywxpython.TransparentStaticText(
            self, label="听讲者模式", pos=(120, 16))
        self.ModeText.SetFont(font1)
        self.ModeText.SetForegroundColour("#ffffff")
        self.ModeText.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.ModeText.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.ModeText.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.ModeText.Bind(wx.EVT_LEFT_DCLICK, self.ChangeMode)
        self.ModeText.Bind(wx.EVT_MIDDLE_DCLICK, self.JoinVote)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.Bind(wx.EVT_LEFT_DCLICK, self.ChangeMode)
        self.Bind(wx.EVT_MIDDLE_DCLICK, self.JoinVote)
        thread.start_new_thread(self.receive, ())

        self.Center()
        self.Show()
    def test(self,event):
        con.write(
            ('docontrol ' + "xixi" + '\n').encode("utf-8"))
    def ChangeMode(self, event):
        global meetingnum
        if str(self.ModeText.GetLabel()) == "听讲者模式":
            con.write(('control ' + str(meetingnum) + '\n').encode("utf-8"))
            self.ModeText.SetLabel("控制模式")

            t2 = threading.Thread\
                (target=run_my_claasfier)
            #
            t2.start()

            win32gui.EnumWindows(get_all_hwnd, 0)
            hwnd_title = dict()
            time.sleep(0.7)
            hld = win32gui.FindWindow(None, u'Real-time SenseNet')
            print(hld)
            win32gui.ShowWindow(hld, win32con.SW_HIDE)
    def JoinVote(self, event):
        global meetingnum
        con.write(('agree ' + str(meetingnum) + '\n').encode("utf-8"))
    def receive(self):
        # 接受服务器的消息
        global meetingnum
        while True:
            sleep(0.6)
            # 在I/O中读取数据，存在result变量中
            result = con.read_very_eager()
            result = result.decode("utf-8")

            result = result.split("\n")

            if result[0] == "voterequest:":
                if meetingnum == result[2]:
                    self.ModeText.SetLabel("举手投票")
                    sleep(3)
                    self.ModeText.SetLabel("听讲者模式")
                        

    def OnRightClickEvent(self, event):
        if str(self.ModeText.GetLabel()) == "控制模式":
            self.OnClose(self)
            # print(threading.current_thread().__class__.__name__)
            # gui.hotkey('Esc')
            win32gui.EnumWindows(get_all_hwnd, 0)
            hwnd_title = dict()
            hld = win32gui.FindWindow(None, u'Real-time SenseNet')
            print(hld)
            if win32gui.IsIconic(hld):
                win32gui.ShowWindow(hld, win32con.SW_SHOWMAXIMIZED)
            win32gui.SetForegroundWindow(hld)
            gui.hotkey('esc')
            print("here")

            MainPageFrame()
        else:
            self.OnClose(self)

            MainPageFrame()

    def OnPaint(self, event):
        mydc = wx.PaintDC(self)
        mydc.DrawBitmap(self.bg, 0, 0, True)

    def OnLeftClickDown(self, event):
        self.pt = event.GetPosition()

    def OnClose(self, event):
        self.Destroy()

    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            self.Move((pos.x-self.pt.x, pos.y-self.pt.y))


class MainPanelS(wx.Panel):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer((hSizer))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # self.SetTransparent(1000)  # 设置透明
        # self.SetMaxSize((480, 353))
        # self.SetMinSize((480, 353))
     # 字体对象
        labelfont = wx.Font(18, family=wx.SWISS, style=wx.NORMAL, weight=wx.LIGHT,
                            underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        # 放置正中央

        # self.logo = Mywxpython.TransparentStaticText(self, label="闪指", pos=(155, 20), size=(240, 50),style=wx.ALIGN_CENTRE_HORIZONTAL)
        # self.logo.SetForegroundColour("#ffffff")

        # 会议号标签
        self.meetingNumberLabel = Mywxpython.TransparentStaticText(
            self, label="会议号", pos=(40, 70), size=(120, 25))
        self.meetingNumberLabel.SetFont(labelfont)
        self.meetingNumberLabel.SetForegroundColour("#ffffff")

        # 会议号框
        self.meetingNumber = wx.TextCtrl(self, pos=(120, 67), size=(150, 25))
        self.meetingNumber.SetDefaultStyle(wx.TextAttr(wx.WHITE))

        # 创建会议按钮
        self.createButton = wx.Button(
            self, label='创建会议', pos=(80, 155), size=(80, 30))
        # 登录按钮上绑定登录方法
        self.createButton.Bind(wx.EVT_BUTTON, self.createmeeting)
        # 加入会议按钮
        self.joinButton = wx.Button(
            self, label='加入会议', pos=(190, 155), size=(80, 30))
        # 登录按钮上绑定登录方法
        self.joinButton.Bind(wx.EVT_BUTTON, self.joinmeeting)

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image/shangwu.png")
        dc.DrawBitmap(bmp, 0, 0)

    def createmeeting(self, event):
        global meetingnum
        # 登录处理
        # try:
        con.write(
            ('creatm ' + str(self.meetingNumber.GetLineText(0)) + '\n').encode("utf-8"))
        response = con.read_some()
        if response == '会议号已存在'.encode('utf-8'):
            self.showDialog('Error', '会议号已存在!', (200, 100))
        elif response == '用户名已存在':
            self.showDialog('Error', '用户名已存在!', (200, 100))
        else:
            
            ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
            self.frame.Close()
        # except Exception:
            # self.showDialog('Error', '连接失败!', (195, 120))

    def joinmeeting(self, event):
        # 登录处理
        con.write(
            ('join ' + str(self.userName.GetLineText(0)) + '\n').encode("utf-8"))
        response = con.read_some()
        if response == '会议号不存在'.encode('utf-8'):
            self.showDialog('Error', '会议号不存在!', (200, 100))
        elif response == '奇怪错误':
            self.showDialog('Error', '奇怪错误', (200, 100))
        else:
            
            ChatFrame(None, 2, title='QT聊天室', size=(500, 400))
            self.frame.Close()

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        # 显示对话窗口
        dialog.ShowModal()


class ServerFrame(wx.Frame):
    """
    登录窗口类，继承wx.Frame类
    """
    # 初始化，添加控件

    def __init__(self):
        wx.Frame.__init__(self, None, 1, "Meeting", size=(
            480, 353), style=wx.DEFAULT_FRAME_STYLE)

        # self.SetTransparent(1000)  # 设置透明
        self.SetMaxSize((480, 353))
        self.SetMinSize((480, 353))
        panel = MainPanelS(self)
        self.Center()
        # 显示组件
        self.Show()


class ChatFrame(wx.Frame):
    """
    聊天窗口类，继承wx.Frame类
    """

    def __init__(self, parent, id, title, size):
        # 初始化，添加控件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        # 显示对话文本框，style设置其文本高亮显示和只读
        self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(
            490, 310), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))
        self.sendButton = wx.Button(
            self, label="Send", pos=(310, 320), size=(58, 25))
        self.usersButton = wx.Button(
            self, label="Users", pos=(373, 320), size=(58, 25))
        self.closeButton = wx.Button(
            self, label="Close", pos=(436, 320), size=(58, 25))
        # 发送按钮绑定发送消息方法
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        # Users按钮绑定获取在线用户数量方法
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        # 关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
        # 调用thread模块中的start_new_thread()来产生新线程负责接收服务器信息
        # 第一个参数为线程要执行函数的函数名，第二个参数为需要传递给函数的实参，为tuple，若该函数不需要参数也要传入空tuple
        thread.start_new_thread(self.receive, ())
        self.Show()

    def send(self, event):
        # 发送消息
        message = str(self.message.GetLineText(0)).strip()
        if message != '':
            # 这里的'say '不可随意变动，为呼应server.py中命令处理类定义的handle(),实现文字聊天协议而存在
            con.write(('say ' + message + '\n').encode("utf-8"))
            self.message.Clear()

    def lookUsers(self, event):
        # 查看当前在线用户
        con.write(b'look\n')

    def close(self, event):
        # 关闭窗口
        con.write(b'logout\n')
        con.close()
        self.Close()

    def receive(self):
        # 接受服务器的消息
        while True:
            sleep(0.6)
            # 在I/O中读取数据，存在result变量中
            result = con.read_very_eager()
            if result != '':
                self.chatFrame.AppendText(result)


if __name__ == '__main__':
    # 应用程序对象
    app = wx.App()
    # 客户端使用telnetlib连接目标主机
    con = telnetlib.Telnet()
    # 顶级窗口对象
    LoginFrame()
    # 进入应用程序的主事件循环
    app.MainLoop()
