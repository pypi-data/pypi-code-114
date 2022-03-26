import wx
import WxCore


class WxWindow(object):
    def __init__(self, Title: str = "WFrame", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=-1):
        # 所有组件的父组件,Title标题，Pos为窗口位置，需要用WxCore里面的DefaultPostion,或者Postion设置位置。Size为窗口大小
        self.Widget = wx.Window()

    def SetBackgroundColour(self, Colour):
        self.Widget.SetBackgroundColour(Colour)

    def SetForegroundColour(self, Colour):
        self.Widget.SetForegroundColour(Colour)

    def SetBackgroundStyle(self, Style):
        self.Widget.SetBackgroundColour(wx.SystemSettings.GetColour(Style))

    def SetForegroundStyle(self, Style):
        self.Widget.SetForegroundColour(wx.SystemSettings.GetColour(Style))

    def SetToolTip(self, ToolTip: str):
        self.Widget.SetToolTip(ToolTip)

    def SetEnable(self, Enable: bool):
        self.Widget.Enable(Enable)

    def Click(self, Header):
        self.Bind(WxCore.OnLeftDown, Header)

    def DoubleClick(self, Header):
        self.Bind(WxCore.OnLeftDownClick, Header)

    def Bind(self, Event, Header):
        self.Widget.Bind(Event, Header)

    def Hide(self):
        self.Widget.Hide()

    def Show(self):
        self.Widget.Show()

class WxApplication(object):
    def __init__(self):
        self.Widget = wx.App()

    def Run(self):
        self.Widget.MainLoop()

class WxFrame(WxWindow):
    def __init__(self, Title: str = "WFrame", Pos=wx.DefaultPosition, Size=wx.DefaultSize,
                 Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=-1):
        super().__init__(Title, Pos, Size, Style, Parent, Id)
        self.Widget = wx.Frame(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)

    def SetTitle(self, Title: str):
        self.Widget.SetTitle(Title)
