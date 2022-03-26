import wx

# Id
AnyID = wx.ID_ANY

# Postion
DefaultPostion = wx.DefaultPosition

# Size
DefaultSize = wx.DefaultSize
DefaultCoord = wx.DefaultCoord

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

# Event
## KeyEvent
OnChar = wx.EVT_CHAR
OnCharHook = wx.EVT_CHAR_HOOK
OnKeyDown = wx.EVT_KEY_DOWN
OnKeyUp = wx.EVT_KEY_UP
## MouseEvent
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

def Colour(Colour):
    Colour = wx.Colour(Colour)

def Postion(X, Y):
    Postion = wx.Point(X, Y)
    return Postion

def Icon(IconFile):
    Icon = wx.Icon(name=IconFile, type=BitmapTypeIcon)