import dataclasses
from dataclasses import field
from enum import Enum, IntFlag
from typing import List, Optional, Union

from flet_core.control import OptionalNumber
from flet_core.painting import Paint
from flet_core.shadow import BoxShadow
from flet_core.types import FontWeight


class TextDecoration(IntFlag):
    NONE = 0
    UNDERLINE = 1
    OVERLINE = 2
    LINE_THROUGH = 4


class TextDecorationStyle(Enum):
    SOLID = "solid"
    DOUBLE = "double"
    DOTTED = "dotted"
    DASHED = "dashed"
    WAVY = "wavy"


@dataclasses.dataclass
class TextStyle:
    size: Union[None, int, float] = field(default=None)
    height: Union[None, int, float] = field(default=None)
    weight: Optional[FontWeight] = field(default=None)
    italic: Optional[bool] = field(default=None)
    decoration: Optional[TextDecoration] = field(default=None)
    decoration_color: Optional[str] = field(default=None)
    decoration_thickness: OptionalNumber = field(default=None)
    decoration_style: Optional[TextDecorationStyle] = field(default=None)
    font_family: Optional[str] = field(default=None)
    color: Optional[str] = field(default=None)
    bgcolor: Optional[str] = field(default=None)
    shadow: Union[None, BoxShadow, List[BoxShadow]] = field(default=None)
    foreground: Optional[Paint] = field(default=None)
    letter_spacing: OptionalNumber = field(default=None)

    def copy_with(
        self,
        size: Union[None, int, float] = None,
        height: Union[None, int, float] = None,
        weight: Optional[FontWeight] = None,
        italic: Optional[bool] = None,
        decoration: Optional[TextDecoration] = None,
        decoration_color: Optional[str] = None,
        decoration_thickness: OptionalNumber = None,
        decoration_style: Optional[TextDecorationStyle] = None,
        font_family: Optional[str] = None,
        color: Optional[str] = None,
        bgcolor: Optional[str] = None,
        shadow: Union[None, BoxShadow, List[BoxShadow]] = None,
        foreground: Optional[Paint] = None,
        letter_spacing: OptionalNumber = None,
    ):
        return TextStyle(
            size if size is not None else self.size,
            height if height is not None else self.height,
            weight if weight is not None else self.weight,
            italic if italic is not None else self.italic,
            decoration if decoration is not None else self.decoration,
            decoration_color if decoration_color is not None else self.decoration_color,
            (
                decoration_thickness
                if decoration_thickness is not None
                else self.decoration_thickness
            ),
            decoration_style if decoration_style is not None else self.decoration_style,
            font_family if font_family is not None else self.font_family,
            color if color is not None else self.color,
            bgcolor if bgcolor is not None else self.bgcolor,
            shadow if shadow is not None else self.shadow,
            foreground if foreground is not None else self.foreground,
            letter_spacing if letter_spacing is not None else self.letter_spacing,
        )
