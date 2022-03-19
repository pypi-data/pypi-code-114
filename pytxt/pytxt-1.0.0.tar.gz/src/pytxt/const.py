from enum import Enum


class Color(int, Enum):
    NONE            = -1
    DARK_GRAY       = 30
    DARK_RED        = 31
    GREEN           = 32
    ORANGE          = 33
    BLUE            = 34
    PURPLE          = 35
    DARK_TURQUOISE  = 36
    LIGHT_GRAY      = 37
    GRAY            = 90
    RED             = 91
    LIME            = 92
    YELLOW          = 93
    LIGHT_BLUE      = 94
    PINK            = 95
    TURQUOISE       = 96
    WHITE           = 97


class TextFormat(int, Enum):
    NONE               = 0
    BOLD               = 1
    DARK               = 2
    ITALIC             = 3
    UNDERLINE          = 4
    BLINK              = 5
    INVERSE_BACKGROUND = 7
    INVISIBLE          = 8
    CROSSED            = 9

