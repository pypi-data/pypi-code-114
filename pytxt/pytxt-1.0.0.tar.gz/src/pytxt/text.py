from typing import Any, List, Optional, Union

from . import Color, TextFormat

class TextConfig:

    def __init__(self, color: Optional[Color] = None, color_bg: Optional[Color] = None, attrs: Optional[List[TextFormat]] = None) -> None:
        self.color = color
        self.color_bg = color_bg
        self.attrs = attrs or []

    def formatter(self) -> str:
        fmtr: List[str] = []
        if self.attrs:
            fmtr.extend(str(attr.value) for attr in self.attrs)
        if self.color is not None and self.color != Color.NONE:
            fmtr.append("%d" % self.color)
        if self.color_bg is not None and self.color_bg != Color.NONE:
            fmtr.append("%d" % (self.color_bg + 10))
        fmt = f"\033[{';'.join(fmtr)}m"
        return "\033[m" + fmt

    def append(self, other: "TextConfig") -> "TextConfig":
        new_attrs = self.attrs + other.attrs
        color = other.color if other.color is not None else self.color
        color_bg = other.color_bg if other.color_bg is not None else self.color_bg
        return TextConfig(color, color_bg, new_attrs)

    def is_empty(self) -> bool:
        return not self.color and not self.color_bg and not self.attrs

class Text:

    def __init__(self, *snippets: Union["Text", str], color: Optional[Color] = None, color_bg: Optional[Color] = None, attrs: Optional[List[TextFormat]] = None, config: Optional[TextConfig] = None) -> None:
        self.snippets = snippets
        self.config = TextConfig(color, color_bg, attrs)
        if config:
            assert self.config.is_empty()
            self.config = config

    def parse(self, *args: Any, **kwargs: Any) -> str:
        return self._parse(TextConfig(), *args, **kwargs)

    @property
    def unformatted(self) -> str:
        return "".join(snip.unformatted if isinstance(snip, Text) else str(snip) for snip in self.snippets)

    def _parse(self, config: TextConfig, *args: Any, **kwargs: Any) -> str:
        full_config = config.append(self.config)
        fmt = full_config.formatter()
        output: str = fmt
        for snip in self.snippets:
            if isinstance(snip, Text):
                output += snip._parse(full_config, *args, **kwargs)
                output += fmt
            else:
                output += str(snip)
        return output + config.formatter()

    def __str__(self) -> str:
        return self.parse()

