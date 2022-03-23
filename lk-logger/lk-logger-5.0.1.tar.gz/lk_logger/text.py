"""
TODO: WIP (for 5.0.2)
"""
from pytermgui.parser import RE_MARKUP
import re


class RichText:
    _ptg_mark_pattern = re.compile(r'\[[-/@_a-z! ():]+]')
    _text: str
    
    def __init__(self):
        self._text = ''
    
    def __add__(self, other):
        self._text += other
        return self
    
    def __radd__(self, other):
        self._text = other + self._text
        return self
    
    def __str__(self) -> str:
        out = ''
        for seg in self._text.split('['):
            seg = '[' + seg
            if self._ptg_mark_pattern.match(seg):
                pass
