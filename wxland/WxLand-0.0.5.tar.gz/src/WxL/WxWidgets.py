import wx
import wx.ribbon
import wx.core
import wx.adv
from WxL import WxCore


class WxEvent(object):
    def Bind(self, Event, Headler, Sourse=None, Id1: int = WxCore.AnyID, Id2: int = WxCore.AnyID):
        self.Widget.Bind(event=Event, handler=Headler, source=Sourse, id=Id1, id2=Id2)


class WxWindow(WxEvent):
    def __init__(self, Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=0, Parent=None, Id=WxCore.AnyID):
        # 所有组件的父组件,Title标题，Pos为窗口位置，需要用WxCore里面的DefaultPostion,或者Postion设置位置。Size为窗口大小
        super().__init__()
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

    def SetPosition(self, Position):
        self.Widget.SetPosition(Position)

    def GetPosition(self):
        return self.Widget.GetPosition()

    def OnMotion(self, Headler, Widget=None):
        self.Widget.Bind(WxCore.OnMotion, Headler, Widget)

    def OnClick(self, Headler, Widget=None):
        self.Bind(WxCore.OnLeftDown, Headler, Widget)

    def OnDoubleClick(self, Headler, Widget=None):
        self.Bind(WxCore.OnLeftDownClick, Headler, Widget)

    def OnEnter(self, Headler, Widget=None):
        self.Bind(WxCore.OnEnterWindow, Headler, Widget)

    def OnLeave(self, Headler, Widget=None):
        self.Bind(WxCore.OnLeaveWindow, Headler, Widget)

    def OnNoClick(self, Headler, Widget=None):
        self.Bind(WxCore.OnLeftUp, Headler, Widget)

    def OnClick2(self, Headler, Widget=None):
        self.Bind(WxCore.OnRightDown, Headler, Widget)

    def OnDoubleClick2(self, Headler, Widget=None):
        self.Bind(WxCore.OnRightDownClick, Headler, Widget)

    def OnNoClick2(self, Headler, Widget=None):
        self.Bind(WxCore.OnRightUp, Headler, Widget)

    def OnClick3(self, Headler, Widget=None):
        self.Bind(WxCore.OnMiddleDownn, Headler, Widget)

    def OnDoubleClick3(self, Headler, Widget=None):
        self.Bind(WxCore.OnMiddleDownClick, Headler, Widget)

    def OnNoClick3(self, Headler, Widget=None):
        self.Bind(WxCore.OnMiddleUp, Headler, Widget)

    def Hide(self):
        self.Widget.Hide()

    def Close(self):
        self.Widget.Close()

    def Show(self):
        self.Widget.Show()


class WxApplication(object):
    def __init__(self):
        self.Widget = wx.App()

    def SetTopWindow(self, Frame):
        self.Widget.SetTopWindow(Frame)

    def Run(self):
        self.Widget.MainLoop()


class WxToplevel(WxWindow):
    def __init__(self, Title: str = "WFrame", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=0, Id=WxCore.AnyID, Parent=None):
        super().__init__(Pos, Size, Style, Parent, Id)

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

    def OnActivate(self, Headler, Widget=None):
        self.Bind(WxCore.OnActivate, Headler, Widget)

    def OnActivateApplication(self, Headler, Widget=None):
        self.Bind(WxCore.OnActivateApp, Headler, Widget)

    def OnClose(self, Headler, Widget=None):
        self.Bind(WxCore.OnClose, Headler, Widget)

    def OnShow(self, Headler, Widget=None):
        self.Bind(WxCore.OnShow, Headler, Widget)

    def OnMove(self, Headler, Widget=None):
        self.Bind(WxCore.OnMove, Headler, WxL)

    def OnMoving(self, Headler, Widget=None):
        self.Bind(WxCore.OnMoving, Headler, Widget)

    def OnMoveStart(self, Headler, Widget=None):
        self.Bind(WxCore.OnMoveStart, Headler, Widget)

    def OnMoveEnd(self, Headler, Widget=None):
        self.Bind(WxCore.OnMoveEnd, Headler, Widget)


class WxFrame(WxToplevel):
    def __init__(self, Title: str = "WFrame", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=WxCore.DefaultFrameStyle, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.Frame(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)


class WxMDIFrame(WxFrame):
    def __init__(self, Title: str = "WFrame", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=WxCore.DefaultFrameStyle | WxCore.HScroll | WxCore.VScroll, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.MDIParentFrame(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)

    def ActivateNext(self):
        # 激活当前活动的 MDI 子项之后的子项。
        self.Widget.ActivateNext()

    def ActivatePrevious(self):
        # 激活当前活动的 MDI 子项之前的子项。
        self.Widget.ActivatePrevious()

    def ArrangeIcons(self):
        # 排列任何图标化（最小化）的 MDI 子窗口。
        self.Widget.ArrangeIcons()

    def Cascade(self):
        # 以级联方式排列 MDI 子窗口。
        self.Widget.Cascade()


class WxMDIFrameChild(WxMDIFrame):
    def __init__(self, Title: str = "WFrame", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=WxCore.DefaultFrameStyle | WxCore.HScroll | WxCore.VScroll, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.MDIParentFrame(parent=Parent, id=Id, title=Title, pos=Pos, size=Size, style=Style)

    def Maximize(self):
        # 最大化此 MDI 子框架。
        self.Widget.Maximize()

    def Restore(self):
        # 恢复此 MDI 子框架（取消最大化）。
        self.Widget.Restore()


class WxPanel(WxWindow):
    def __init__(self, Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize,
                 Style=WxCore.TabTraversal, Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.Panel(parent=Parent, id=Id, pos=Pos, size=Size, style=Style)


class WxSizer(WxWindow):
    def __init__(self, Orient=WxCore.Horizontal):
        super().__init__()
        self.Widget = wx.BoxSizer(orient=Orient)

    def Add(self, Window, Flag=WxCore.All | WxCore.Expand | WxCore.AlignLeft, Border: int = 0,
            Width: int = 0, Height: int = 0):
        self.Widget.Add(window=Window, flag=Flag, border=Border, width=Width, height=Height)

    def Clear(self, DeleteWindows: bool = False):
        self.Widget.Clear(DeleteWindows)

    def Insert(self, Index, Window, Flag=WxCore.All | WxCore.Expand | WxCore.AlignLeft, Border: int = 0,
               Width: int = 0, Height: int = 0):
        self.Widget.Insert(index=Index, window=Window, flag=Flag, border=Border, width=Width, height=Height)

    def GetChild(self):
        return self.Widget.GetChildren()

    def GetItem(self, Sizer):
        return self.Widget.GetItem(sizer=Sizer)

    def Detach(self, Sizer: bool):
        self.Widget.Detach(sizer=Sizer)


class WxBoxSizer(WxSizer):
    def __init__(self, Orient=WxCore.Horizontal):
        super().__init__()
        self.Widget = wx.BoxSizer(orient=Orient)

    def SetOrientation(self, Orient):
        self.Widget.SetOrientation(Orient)

    def GetOrientation(self):
        return self.Widget.GetOrientation()


class WxEntry(object):
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


class WxButton(WxWindow):
    def __init__(self, Label: str = "", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=0, Parent=None,
                 Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.Button(label=Label, parent=Parent, id=Id, pos=Pos, size=Size, style=Style)

    def SetDefault(self):
        self.Widget.SetDefault()

    def SetLabel(self, Label):
        self.Widget.SetLabel(Label)

    def GetLabel(self):
        return self.Widget.GetLabel()

    def OnButtonClick(self, Headler, Widget=None):
        self.Bind(WxCore.OnButtonClick, Headler, Widget)


class WxLabel(WxWindow):
    def __init__(self, Label: str = "", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=0, Parent=None,
                 Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.StaticText(label=Label, parent=Parent, id=Id, pos=Pos, size=Size, style=Style)

    def SetLabel(self, Label):
        self.Widget.SetLabel(Label)

    def GetLabel(self):
        return self.Widget.GetLabel()


class WxText(WxWindow, WxEntry):
    def __init__(self, Text: str = "", Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=WxCore.TextStyle_Left,
                 Parent=None,
                 Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.TextCtrl(parent=Parent, id=Id, pos=Pos, size=Size, style=Style, value=Text)

    def Write(self, Text: str):
        self.Widget.write(text=Text)

    def OnText(self, Headler, Widget=None):
        self.Bind(WxCore.OnText, Headler, Widget)

    def OnTextEnter(self, Headler, Widget=None):
        self.Bind(WxCore.OnTextEnter, Headler, Widget)


class WxCheckListBox(WxWindow):
    def __init__(self, List: list = [], Pos=WxCore.DefaultPostion, Size=WxCore.DefaultSize, Style=WxCore.TextStyle_Left,
                 Parent=None, Id=WxCore.AnyID):
        super().__init__(Pos, Size, Style, Parent, Id)
        self.Widget = wx.CheckListBox(parent=Parent, id=Id, pos=Pos, size=Size, style=Style, choices=List)

    def SetCheckStrings(self, Strings: str):
        self.Widget.SetChecked(strings=String)

    def Check(self, Item: int, Check: bool = True):
        self.Widget.Check(item=Item, check=Check)


class WxMessageBox(object):
    def __init__(self, Message: str, Title: str = WxCore.MessageBoxCaptionStr, Style: int = WxCore.Centre | WxCore.Ok,
                 Parent=None, X=WxCore.DefaultCoord, Y=WxCore.DefaultCoord):
        self.Widget = wx.MessageBox(message=Message, caption=Title, style=Style, parent=Parent, x=X, y=Y)
