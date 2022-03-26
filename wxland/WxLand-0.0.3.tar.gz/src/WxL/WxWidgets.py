import wx
import WxCore
import wx.ribbon


class WxWindow(object):
    def __init__(self, Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=WxCore.AnyID):
        # 所有组件的父组件,Title标题，Pos为窗口位置，需要用WxCore里面的DefaultPostion,或者Postion设置位置。Size为窗口大小
        self.Widget = wx.Window()

    def Destroy(self):
        self.Widget.Destroy()

    def Move(self, X, Y):
        self.Widget.Move(X, Y)

    def ReSize(self, Width, Height):
        self.Widget.SetSizeWH()

    def SetId(self, ID):
        self.Widget.SetId(ID)

    def GetId(self):
        return self.Widget.GetId()

    def SetSize(self, X, Y, Width, Height):
        self.Widget.SetSize(X, Y, Width, Height)

    def GetSize(self):
        return self.Widget.GetSize()

    def SetBackgroundColour(self, Colour):
        self.Widget.SetBackgroundColour(Colour)

    def GetBackgroundColour(self):
        return self.Widget.GetBackgroundColour()

    def SetForegroundColour(self, Colour):
        self.Widget.SetForegroundColour(Colour)

    def GetForegroundColour(self):
        return self.Widget.GetForegroundColour()

    def SetBackgroundStyle(self, Style):
        self.Widget.SetBackgroundColour(wx.SystemSettings.GetColour(Style))

    def SetForegroundStyle(self, Style):
        self.Widget.SetForegroundColour(wx.SystemSettings.GetColour(Style))

    def SetToolTip(self, ToolTip: str):
        self.Widget.SetToolTip(ToolTip)

    def GetToolTip(self):
        return self.Widget.GetToolTip()

    def SetEnable(self, Enable: bool):
        self.Widget.Enable(Enable)

    def GetEnable(self):
        return self.Widget.IsEnabled()

    def Click(self, Header):
        self.Bind(WxCore.OnLeftDown, Header)

    def DoubleClick(self, Header):
        self.Bind(WxCore.OnLeftDownClick, Header)

    def Bind(self, Event, Headler, Sourse=None, Id1: int = WxCore.AnyID, Id2: int = WxCore.AnyID):
        self.Widget.Bind(event=Event, handler=Headler, source=Sourse, id=Id1, id2=Id2)

    def Hide(self):
        self.Widget.Hide()

    def Close(self):
        self.Widget.Close()

    def Show(self):
        self.Widget.Show()


class WxApplication(object):
    def __init__(self):
        self.Widget = wx.App()

    def Run(self):
        self.Widget.MainLoop()


class WxToplevel(WxWindow):
    def __init__(self, Title: str = "WFrame", Pos=wx.DefaultPosition, Size=wx.DefaultSize,
                 Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.TopLevelWindow(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)

    def SetIocn(self, Icon):
        self.Widget.SetIcon(icon=Icon)

    def GetIcon(self):
        return self.Widget.GetIcon()

    def SetTitle(self, Title: str):
        self.Widget.SetTitle(Title)

    def GetTitle(self):
        return self.Widget.GetTitle()

    def SetEnableCloseButton(self, Enable: bool):
        self.Widget.EnableCloseButton(enable=Enable)

    def SetEnableMaximizeButton(self, Enable: bool):
        self.Widget.EnableMaximizeButton(enable=Enable)

    def SetEnableMinimizeButton(self, Enable: bool):
        self.Widget.EnableMinimizeButton(enable=Enable)


class WxFrame(WxToplevel):
    def __init__(self, Title: str = "WFrame", Pos=wx.DefaultPosition, Size=wx.DefaultSize,
                 Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.Frame(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)

class WxPanel(WxWindow):
    def __init__(self, Pos=wx.DefaultPosition, Size=wx.DefaultSize,
                 Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None, Id=WxCore.AnyID):
        super().__init__(Title, Pos, Size, Style, Parent, Id)
        self.Widget = wx.Panel(parent=Parent, id=Id, pos=Pos, size=Size, style=Style)


class WxEntry(object):
    def __init__(self):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.TextEntry()

    def GetEmpty(self):
        return self.Widget.IsEmpty()

    def GetEditable(self):
        return self.Widget.IsEditable()

    def Clear(self):
        self.Widget.Clear()

    def LoadFile(self, FileName, Type: int = WxCore.TextTypeAny):
        self.Widget.LoadFile(FileName)

    def Copy(self):
        self.Widget.Copy()

    def Cut(self):
        self.Widget.Cut()

    def Paste(self):
        self.Widget.Paste()

    def Undo(self):
        self.Widget.Undo()

    def Redo(self):
        self.Widget.Redo()

    def CanCopy(self):
        self.Widget.CanCopy()

    def CanCut(self):
        self.Widget.CanCut()

    def CanPaste(self):
        self.Widget.CanPaste()

    def CanUndo(self):
        self.Widget.CanUndo()

    def CanRedo(self):
        self.Widget.CanRedo()

    def WriteText(self, Text):
        self.Widget.WriteText(Text)

    def AppendText(self, Text):
        self.Widget.AppendText(Text)

    def SetText(self, Text: str):
        self.Widget.SetValue(value=Text)

    def GetText(self):
        return self.Widget.GetValue()


class WxText(WxWindow, WxEntry):
    def __init__(self, Text: str = "", Pos=wx.DefaultPosition, Size=wx.DefaultSize, Style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL, Parent=None,
                 Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.TextCtrl(parent=Parent, id=Id, pos=Pos, size=Size, style=Style, value=Text)

    def Write(self, Text: str):
        self.Widget.write(text=Text)


class WxMessageBox(object):
    def __init__(self, Message: str, Title: str = WxCore.MessageBoxCaptionStr, Style: int = WxCore.Centre | WxCore.Ok,
                 Parent=None, X=WxCore.DefaultCoord, Y=WxCore.DefaultCoord):
        self.Widget = wx.MessageBox(message=Message, caption=Title, style=Style, parent=Parent, x=X, y=Y)
