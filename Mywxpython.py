import wx


class MyTextCtrl:
    """自定义文本框"""
    def __init__(self, parent, pos, size=(80, 36), readOnly=False):
        self.defaultFontSize = 13  #默认字体大小
        self.TextCtrlColor = '#2B323C'  #文本框的背景色
        self.defaultBorderColoe = '#EAEAEA'  #默认边框颜色

        self.textCtrl, self.border, self.bg = self.__CreateTextCtrl(
            parent, pos, size, self.defaultBorderColoe, readOnly)

    def __CreateTextCtrl(self,
                         parent,
                         pos,
                         size,
                         borderColor,
                         readOnly=True,
                         borderSize=1):
        """创建文本框"""
        border = wx.StaticText(parent, -1, '', size=size, pos=pos)  #创建边框
        border.SetBackgroundColour(borderColor)  #设置边框要展现的颜色
        bg = wx.StaticText(border,
                           -1,
                           '',
                           size=((size[0] - borderSize * 2),
                                 (size[1] - borderSize * 2)),
                           pos=(borderSize, borderSize))
        if readOnly:  #设置文本框是否只读，还有去自带的边框
            style = wx.TE_READONLY | wx.NO_BORDER
        else:
            style = wx.NO_BORDER

        textCtrl = wx.TextCtrl(
            bg,
            -1,
            size=((size[0]), self.defaultFontSize * 2),
            pos=(0, (size[1] - 2 * self.defaultFontSize - borderSize * 2) / 2),
            style=style)
        font = wx.Font(self.defaultFontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL,
                       False, '微软雅黑')
        textCtrl.SetFont(font)

        if readOnly:
            bg.SetBackgroundColour('rgb(240,240,240)')
            self.TextCtrlColor = 'rgb(240,240,240)'
        else:
            bg.SetBackgroundColour(textCtrl.GetBackgroundColour())
            self.TextCtrlColor = textCtrl.GetBackgroundColour()
        bg.Bind(wx.EVT_LEFT_UP, self.__ClickEvent)
        return textCtrl, border, bg

    def __ClickEvent(self, evt):
        """点击时焦点设置在文本框上"""
        self.textCtrl.SetFocus()

    def SetValue(self, value):
        if not value:
            value = ''
        self.textCtrl.SetValue(value)

    def GetValue(self):
        return self.textCtrl.GetValue()

    def SetBorderColor(self, color):
        self.border.SetBackgroundColour(color)
        self.border.Refresh()

    def SetFontColor(self, color):
        self.textCtrl.SetForegroundColour(color)
        self.textCtrl.SetBackgroundColour(self.TextCtrlColor)

    def SetFont(self, font):
        self.textCtrl.SetFont(font)

    def SetBackgroundColour(self, color):
        self.bg.SetBackgroundColour(color)
        self.textCtrl.SetBackgroundColour(color)
        self.textCtrl.Refresh()


class TransparentStaticText(wx.StaticText):
    """
    重写StaticText控件
    """
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 label='',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.TRANSPARENT_WINDOW,
                 name='TransparentStaticText'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)

    def OnSize(self, event):
        self.Refresh()
        event.Skip()



class MyText:
    """自定义文本框"""
    def __init__(self, parent, pos, size=(80, 36), readOnly=False):
        self.defaultFontSize = 10  #默认字体大小
        self.TextCtrlColor = 'white'  #文本框的背景色
        self.defaultBorderColoe = '#EAEAEA'  #默认边框颜色

        self.textCtrl, self.border, self.bg = self.__CreateTextCtrl(
            parent, pos, size, self.defaultBorderColoe, readOnly)

    def __CreateTextCtrl(self,
                         parent,
                         pos,
                         size,
                         borderColor,
                         readOnly=True,
                         borderSize=1):
        """创建文本框"""
        border = wx.StaticText(parent, -1, '', size=size, pos=pos)  #创建边框
        border.SetBackgroundColour(borderColor)  #设置边框要展现的颜色
        bg = wx.StaticText(border,
                           -1,
                           '',
                           size=((size[0] - borderSize * 2),
                                 (size[1] - borderSize * 2)),
                           pos=(borderSize, borderSize))
        if readOnly:  #设置文本框是否只读，还有去自带的边框
            style = wx.TE_READONLY | wx.NO_BORDER
        else:
            style = wx.NO_BORDER

        textCtrl = wx.TextCtrl(
            bg,
            -1,
            size=((size[0] - 10), self.defaultFontSize * 2),
            pos=(5, (size[1] - 2 * self.defaultFontSize - borderSize * 2) / 2),
            style=style)
        font = wx.Font(self.defaultFontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL,
                       False, '微软雅黑')
        textCtrl.SetFont(font)

        if readOnly:
            bg.SetBackgroundColour('rgb(240,240,240)')
            self.TextCtrlColor = 'rgb(240,240,240)'
        else:
            bg.SetBackgroundColour(textCtrl.GetBackgroundColour())
            self.TextCtrlColor = textCtrl.GetBackgroundColour()
        bg.Bind(wx.EVT_LEFT_UP, self.__ClickEvent)
        return textCtrl, border, bg

    def __ClickEvent(self, evt):
        """点击时焦点设置在文本框上"""
        self.textCtrl.SetFocus()

    def SetValue(self, value):
        if not value:
            value = ''
        self.textCtrl.SetValue(value)

    def GetValue(self):
        return self.textCtrl.GetValue()

    def SetBorderColor(self, color):
        self.border.SetBackgroundColour(color)
        self.border.Refresh()

    def SetFontColor(self, color):
        self.textCtrl.SetForegroundColour(color)
        self.textCtrl.SetBackgroundColour(self.TextCtrlColor)

    def SetFont(self, font):
        self.textCtrl.SetFont(font)

    def SetBackgroundColour(self, color):
        self.bg.SetBackgroundColour(color)
        self.textCtrl.SetBackgroundColour(color)
        self.textCtrl.Refresh()

#自动提示文本框
# class SuggestionsPopup(wx.Frame):
#     def __init__(self, parent):
#         wx.Frame.__init__(
#             self, parent,
#             style=wx.FRAME_NO_TASKBAR|wx.FRAME_FLOAT_ON_PARENT|wx.STAY_ON_TOP
#         )
#         self._suggestions = self._listbox(self)
#         self._suggestions.SetItemCount(0)
#         self._unformated_suggestions = None
    
#     def SetSuggestions(self, suggestions, unformated_suggestions):
#         self._suggestions.items = suggestions
#         self._suggestions.SetItemCount(len(suggestions))
#         self._suggestions.SetSelection(0)
#         self._suggestions.Refresh()
#         self._unformated_suggestions = unformated_suggestions
#     def CursorUp(self):
#         selection = self._suggestions.GetSelection()
#         if selection > 0:
#             self._suggestions.SetSelection(selection - 1)
#     def CursorDown(self):
#         selection = self._suggestions.GetSelection()
#         last = self._suggestions.GetItemCount() - 1
#         if selection < last:
#             self._suggestions.SetSelection(selection + 1)
#     def CursorHome(self):
#         if self.IsShown():
#             self._suggestions.SetSelection(0)
#     def CursorEnd(self):
#         if self.IsShown():
#             self._suggestions.SetSelection(self._suggestions.GetItemCount() - 1)
#     def GetSelectedSuggestion(self):
#         return self._unformated_suggestions[self._suggestions.GetSelection()]
#     def GetSuggestion(self, n):
#         return self._unformated_suggestions[n]
# class AutocompleteTextCtrl(wx.TextCtrl):
#     def __init__(
#         self, parent,
#         height=300, completer=None,
#         multiline=False, frequency=250
#     ):
#         style = wx.TE_PROCESS_ENTER
#         if multiline:
#             style = style | wx.TE_MULTILINE
#         wx.TextCtrl.__init__(self, parent, style=style)
#         self.height = height
#         self.frequency = frequency
#         if completer:
#             self.SetCompleter(completer)
#         self.queued_popup = False
#         self.skip_event = False
#     def SetCompleter(self, completer):
#         """
#         Initializes the autocompletion. The 'completer' has to be a function
#         with one argument (the current value of the control, ie. the query)
#         and it has to return two lists: formated (html) and unformated
#         suggestions.
#         """
#         self.completer = completer
#         frame = self.Parent
#         while not isinstance(frame, wx.Frame):
#             frame = frame.Parent
#         self.popup = SuggestionsPopup(frame)
#         frame.Bind(wx.EVT_MOVE, self.OnMove)
#         self.Bind(wx.EVT_TEXT, self.OnTextUpdate)
#         self.Bind(wx.EVT_SIZE, self.OnSizeChange)
#         self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
#         self.popup._suggestions.Bind(wx.EVT_LEFT_DOWN, self.OnSuggestionClicked)
#         self.popup._suggestions.Bind(wx.EVT_KEY_DOWN, self.OnSuggestionKeyDown)
#     def AdjustPopupPosition(self):
#         self.popup.Position = self.ClientToScreen((0, self.Size.height)).Get()
#     def OnMove(self, event):
#         self.AdjustPopupPosition()
#         event.Skip()
#     def OnTextUpdate(self, event):
#         if self.skip_event:
#             self.skip_event = False
#         elif not self.queued_popup:
#             wx.CallLater(self.frequency, self.AutoComplete)
#             self.queued_popup = True
#         event.Skip()
#     def AutoComplete(self):
#         self.queued_popup = False
#         if self.Value != "":
#             formated, unformated = self.completer(self.Value)
#             if len(formated) > 0:
#                 self.popup.SetSuggestions(formated, unformated)
#                 self.AdjustPopupPosition()
#                 self.Unbind(wx.EVT_KILL_FOCUS)
#                 self.popup.ShowWithoutActivating()
#                 self.SetFocus()
#                 self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
#             else:
#                 self.popup.Hide()
#         else:
#             self.popup.Hide()
#     def OnSizeChange(self, event):
#         self.popup.Size = (self.Size[0], self.height)
#         event.Skip()
#     def OnKeyDown(self, event):
#         key = event.GetKeyCode()
#         if key == wx.WXK_UP:
#             self.popup.CursorUp()
#             return
#         elif key == wx.WXK_DOWN:
#             self.popup.CursorDown()
#             return
#         elif key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER) and self.popup.Shown:
#             self.skip_event = True
#             self.SetValue(self.popup.GetSelectedSuggestion())
#             self.SetInsertionPointEnd()
#             self.popup.Hide()
#             return
#         elif key == wx.WXK_HOME:
#             self.popup.CursorHome()
#         elif key == wx.WXK_END:
#             self.popup.CursorEnd()
#         elif event.ControlDown() and unichr(key).lower() == "a":
#             self.SelectAll()
#         elif key == wx.WXK_ESCAPE:
#             self.popup.Hide()
#             return
#         event.Skip()
#     def OnSuggestionClicked(self, event):
#         self.skip_event = True
#         n = self.popup._suggestions.HitTest(event.Position)
#         self.Value = self.popup.GetSuggestion(n)
#         self.SetInsertionPointEnd()
#         wx.CallAfter(self.SetFocus)
#         event.Skip()
#     def OnSuggestionKeyDown(self, event):
#         key = event.GetKeyCode()
#         if key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
#             self.skip_event = True
#             self.SetValue(self.popup.GetSelectedSuggestion())
#             self.SetInsertionPointEnd()
#             self.popup.Hide()
#         event.Skip()
#     def OnKillFocus(self, event):
#         if not self.popup.IsActive():
#             self.popup.Hide()
#         event.Skip()

# #自动提示文本框