"""Stub file for reflex/components/radix/themes/components/spinner.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixLoadingProp, RadixThemesComponent

LiteralSpinnerSize = Literal["1", "2", "3"]

class Spinner(RadixLoadingProp, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3"]],
                Literal["1", "2", "3"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
            ]
        ] = None,
        loading: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[]]] = None,
        on_click: Optional[EventType[[]]] = None,
        on_context_menu: Optional[EventType[[]]] = None,
        on_double_click: Optional[EventType[[]]] = None,
        on_focus: Optional[EventType[[]]] = None,
        on_mount: Optional[EventType[[]]] = None,
        on_mouse_down: Optional[EventType[[]]] = None,
        on_mouse_enter: Optional[EventType[[]]] = None,
        on_mouse_leave: Optional[EventType[[]]] = None,
        on_mouse_move: Optional[EventType[[]]] = None,
        on_mouse_out: Optional[EventType[[]]] = None,
        on_mouse_over: Optional[EventType[[]]] = None,
        on_mouse_up: Optional[EventType[[]]] = None,
        on_scroll: Optional[EventType[[]]] = None,
        on_unmount: Optional[EventType[[]]] = None,
        **props,
    ) -> "Spinner":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: The size of the spinner.
            loading: If set, show an rx.spinner instead of the component children.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

spinner = Spinner.create
