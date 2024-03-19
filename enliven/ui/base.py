from abc import ABC, abstractmethod
from pygame import Surface

# Includes define, field, FunctionType and all of the base_classes
from constants import *

@define
class WidgetBase(ABC):
    on_change: FunctionType = field()
    size: IntVec = field(default=IntVec((0, 0)))
    pos: IntVec = field(default=IntVec((0, 0)))
    disabled: bool = field(default=False)

    @abstractmethod
    def draw(self, surface: Surface, scheme: ColorScheme, state: InteractionState) -> None:
        pass

    @abstractmethod
    def compute(self, mouse_pos: IntVec, mouse_state: bool) -> bool:
        pass



class WidgetStack:

    @define
    class DisplayOptions:
        color_scheme: ColorScheme = DEFAULT_SCHEME
        panel_color: ColorScheme = DEFAULT_SCHEME
        padding: Padding = Padding.round(5)
        spacing: int = 3
        override_panel_alpha: float = 1.1 # Set to > 1 to disable

    _max_inner_size: IntVec # DO NOT TOUCH, DEFINED USING DIMENSIONS OF WIDGETS IN STACK
    _locked_widget: WidgetBase
    _mouse_pressed: bool

    def __init__(self, surface: Surface, pos = IntVec(0, 0), widgets: list[WidgetBase] = None):
        self.pos: IntVec = pos
        if surface is None:
            raise ValueError("Surface cannot be None")
        self.surface: Surface = surface
        self.widgets: list[WidgetBase] = widgets or []
        self.display_options = self.DisplayOptions()
        self.update_size()

    def update_widget_pos(self):
        prev_y: int = self.display_options.padding.top - self.display_options.spacing
        for i in self.widgets:
            i.pos.x = self.pos.x + self.display_options.padding.left
            i.pos.y = prev_y + self.display_options.spacing


    def update_size(self):
        max_size_x: int = 0
        max_size_y: int = 0
        for i in self.widgets:

            _x: int = i.size.x
            if _x > max_size_x:
                max_size_x = _x

            max_size_y += i.size.y + self.display_options.spacing

        self._max_inner_size = IntVec(max_size_x + self.display_options.padding.right, max_size_y + self.display_options.padding.bottom)


    def draw(self):
        pass

    def process(self, _mouse_pos: tuple[int, int], mouse_pressed: bool) -> None:
        self.draw()

        mouse_pos: IntVec = IntVec(_mouse_pos)

        if self._locked_widget:
            if not mouse_pressed:
                self._locked_widget = None
                return
            self._locked_widget.compute(mouse_pos, True)
            for i in self.widgets:
                i.draw(self.surface, self.display_options.color_scheme, InteractionState.INTERACTING if i is self._locked_widget else InteractionState.NOT_INTERACTING)
            return

        if mouse_pos.is_inbounds(self.pos, self._max_inner_size):
            for i in self.widgets:
                state: int = InteractionState.NOT_INTERACTING
                if mouse_pos.is_inbounds(i.pos, i.size):
                    state = InteractionState.HOVERING
                    i.compute(mouse_pos, mouse_pressed)
                    if mouse_pressed:
                        self._locked_widget = i
                i.draw(self.pos, self.surface, self.display_options.color_scheme, state)

