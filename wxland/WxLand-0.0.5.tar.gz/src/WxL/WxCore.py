import wx

# Id
AnyID = wx.ID_ANY

# Postion
DefaultPostion = wx.DefaultPosition

# Size
DefaultSize = wx.DefaultSize
DefaultCoord = wx.DefaultCoord

# Sizer
Top = wx.TOP
Bottom = wx.BOTTOM
Left = wx.LEFT
Right = wx.RIGHT
All = wx.ALL

Expand = wx.EXPAND
Shaped = wx.SHAPED

AlignCenter = wx.ALIGN_CENTER
AlignLeft = wx.ALIGN_LEFT
AlignRight = wx.ALIGN_RIGHT
AlignTop = wx.ALIGN_TOP
AlignBottom = wx.ALIGN_BOTTOM
AlignVertical = wx.ALIGN_CENTER_VERTICAL
AlignHorizontal = wx.ALIGN_CENTER_HORIZONTAL

# Style
DefaultFrameStyle = wx.DEFAULT_FRAME_STYLE
TabTraversal = wx.TAB_TRAVERSAL
VScroll = wx.VSCROLL
HScroll = wx.HSCROLL

# orient
Horizontal = wx.HORIZONTAL
Vertical = wx.VERTICAL

# Button
Centre = wx.CENTRE
Ok = wx.OK
No = wx.NO

# MessgaeBox
MessageBoxCaptionStr = wx.MessageBoxCaptionStr

# WindowStyleColour
AppWorkSpace = wx.SYS_COLOUR_APPWORKSPACE
ActiveBorder = wx.SYS_COLOUR_ACTIVEBORDER
ActiveCaption = wx.SYS_COLOUR_ACTIVECAPTION
HighlightText = wx.SYS_COLOUR_HIGHLIGHTTEXT
ButtonFace = wx.SYS_COLOUR_BTNFACE
ButtonHighlightText = wx.SYS_COLOUR_BTNHIGHLIGHT
ButtonShadow = wx.SYS_COLOUR_BTNSHADOW
Button = wx.SYS_COLOUR_BTNTEXT
Window = wx.SYS_COLOUR_WINDOW
WindowText = wx.SYS_COLOUR_WINDOWTEXT
WindowFrame = wx.SYS_COLOUR_WINDOWFRAME
ScrollBar = wx.SYS_COLOUR_SCROLLBAR
Menu = wx.SYS_COLOUR_MENU
InactiveBorder = wx.SYS_COLOUR_INACTIVEBORDER
InactiveCaption = wx.SYS_COLOUR_INACTIVECAPTION
InactiveCaptionText = wx.SYS_COLOUR_INACTIVECAPTIONTEXT
ToolBarText = wx.ROLE_SYSTEM_TOOLBAR
CaptionText = wx.SYS_COLOUR_CAPTIONTEXT

# IconType
BitmapTypeIcon = wx.BITMAP_TYPE_ICON

# TextCtrl
TextTypeAny = wx.TEXT_TYPE_ANY

TextStyle_Center = wx.TE_CENTER
TextStyle_Left = wx.TE_LEFT
TextStyle_Right = wx.TE_RIGHT
TextStyle_ReadOnly = wx.TE_READONLY
TextStyle_PassWord = wx.TE_PASSWORD

# Event
## WxWindow KeyEvent
OnChar = wx.EVT_CHAR
OnCharHook = wx.EVT_CHAR_HOOK
OnKeyDown = wx.EVT_KEY_DOWN
OnKeyUp = wx.EVT_KEY_UP
## WxWindow MouseEvent
OnEnterWindow = wx.EVT_ENTER_WINDOW
OnLeaveWindow = wx.EVT_LEAVE_WINDOW
OnLeftDownClick = wx.EVT_LEFT_DCLICK
OnLeftDown = wx.EVT_LEFT_DOWN
OnLeftUp = wx.EVT_LEFT_UP
OnMiddleDownClick = wx.EVT_MIDDLE_DCLICK
OnMiddleDown = wx.EVT_MIDDLE_DOWN
OnMiddleUp = wx.EVT_MIDDLE_UP
OnRightDownClick = wx.EVT_RIGHT_DCLICK
OnRightDown = wx.EVT_RIGHT_DOWN
OnRightUp = wx.EVT_RIGHT_UP
OnMotion = wx.EVT_MOTION
## WxToplevelWindow
OnActivate = wx.EVT_ACTIVATE
OnActivateApp = wx.EVT_ACTIVATE_APP
OnClose = wx.EVT_CLOSE
OnShow = wx.EVT_SHOW
OnMaximize = wx.EVT_MAXIMIZE
OnMove = wx.EVT_MOVE
OnMoving = wx.EVT_MOVING
OnMoveStart = wx.EVT_MOVE_START
OnMoveEnd = wx.EVT_MOVE_END
OnIdle = wx.EVT_IDLE
## WxButton
OnButtonClick = wx.EVT_BUTTON
## WxText
OnText = wx.EVT_TEXT
OnTextEnter = wx.EVT_TEXT_ENTER


def Colour(Colour):
    Colour = wx.Colour(Colour)

def Postion(X, Y):
    Postion = wx.Point(X, Y)
    return Postion

def Icon(IconFile):
    Icon = wx.Icon(name=IconFile, type=BitmapTypeIcon)