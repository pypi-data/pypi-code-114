"""Utilities related to default service configurations."""

from .services import Service


_CARBON = {
    "paddingVertical": "56px",
    "paddingHorizontal": "56px",
    "backgroundColor": "rgba(171, 184, 195, 1)",
    "dropShadow": True,
    "dropShadowOffsetY": "20px",
    "dropShadowBlurRadius": "68px",
    "theme": "synthwave84",
    "windowTheme": "none",
    "language": "auto",
    "fontFamily": "Hack",
    "fontSize": "14px",
    "lineHeight": "133%",
    "windowControls": True,
    "widthAdjustment": True,
    "lineNumbers": False,
    "firstLineNumber": 1,
    "exportSize": "2x",
    "watermark": False,
    "hiddenCharacters": False,
    "name": "",
    "width": 680,
}


_SNAPPIFY = {
    "fileName": "",
    "theme": "github-dark-dimmed",
    "background": "linear-gradient(354deg,  #FF75B5, #FFB86C)",
    "paddingLeft": 60,
    "paddingRight": 60,
    "paddingTop": 40,
    "paddingBottom": 100,
    "profileInfo": {
        "showFullname": True,
        "showUsername": True,
        "showAvatar": True,
        "position": "bottom-center",
    },
    "aspectRatio": {"width": 16, "height": 9},
}


CONFIGS = {
    Service.CARBON: _CARBON.copy(),
    Service.SNAPPIFY: _SNAPPIFY.copy(),
}
