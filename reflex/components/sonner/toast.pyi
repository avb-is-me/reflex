"""Stub file for reflex/components/sonner/toast.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, ClassVar, Dict, Literal, Optional, Union, overload

from reflex.base import Base
from reflex.components.component import Component, ComponentNamespace
from reflex.components.lucide.icon import Icon
from reflex.components.props import PropsBase
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.utils.serializers import serializer
from reflex.vars import BaseVar, Var

try:
    from pydantic.v1.error_wrappers import ValidationError
except ModuleNotFoundError:
    pass
LiteralPosition = Literal[
    "top-left",
    "top-center",
    "top-right",
    "bottom-left",
    "bottom-center",
    "bottom-right",
]
toast_ref = Var.create_safe("refs['__toast']", _var_is_string=False)

class ToastAction(Base):
    label: str
    on_click: Any

@serializer
def serialize_action(action: ToastAction) -> dict: ...

class ToastProps(PropsBase):
    description: Optional[Union[str, Var]]
    close_button: Optional[bool]
    invert: Optional[bool]
    important: Optional[bool]
    duration: Optional[int]
    position: Optional[LiteralPosition]
    dismissible: Optional[bool]
    action: Optional[ToastAction]
    cancel: Optional[ToastAction]
    id: Optional[Union[str, Var]]
    unstyled: Optional[bool]
    style: Optional[Style]
    action_button_styles: Optional[Style]
    cancel_button_styles: Optional[Style]
    on_dismiss: Optional[Any]
    on_auto_close: Optional[Any]

    def dict(self, *args, **kwargs) -> dict[str, Any]: ...

    class Config:
        arbitrary_types_allowed = True
        use_enum_values = True
        extra = "forbid"

class Toaster(Component):
    is_used: ClassVar[bool] = False

    def add_hooks(self) -> list[Var | str]: ...
    @staticmethod
    def send_toast(
        message: str = "", level: str | None = None, **props
    ) -> EventSpec: ...
    @staticmethod
    def toast_info(message: str, **kwargs): ...
    @staticmethod
    def toast_warning(message: str, **kwargs): ...
    @staticmethod
    def toast_error(message: str, **kwargs): ...
    @staticmethod
    def toast_success(message: str, **kwargs): ...
    @staticmethod
    def toast_dismiss(id: Var | str | None = None): ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        theme: Optional[Union[Var[str], str]] = None,
        rich_colors: Optional[Union[Var[bool], bool]] = None,
        expand: Optional[Union[Var[bool], bool]] = None,
        visible_toasts: Optional[Union[Var[int], int]] = None,
        position: Optional[
            Union[
                Var[
                    Literal[
                        "top-left",
                        "top-center",
                        "top-right",
                        "bottom-left",
                        "bottom-center",
                        "bottom-right",
                    ]
                ],
                Literal[
                    "top-left",
                    "top-center",
                    "top-right",
                    "bottom-left",
                    "bottom-center",
                    "bottom-right",
                ],
            ]
        ] = None,
        close_button: Optional[Union[Var[bool], bool]] = None,
        offset: Optional[Union[Var[str], str]] = None,
        dir: Optional[Union[Var[str], str]] = None,
        hotkey: Optional[Union[Var[str], str]] = None,
        invert: Optional[Union[Var[bool], bool]] = None,
        toast_options: Optional[Union[Var[ToastProps], ToastProps]] = None,
        gap: Optional[Union[Var[int], int]] = None,
        loading_icon: Optional[Union[Var[Icon], Icon]] = None,
        pause_when_page_is_hidden: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "Toaster":
        """Create a toaster component.

        Args:
            *children: The children of the toaster.
            theme: the theme of the toast
            rich_colors: whether to show rich colors
            expand: whether to expand the toast
            visible_toasts: the number of toasts that are currently visible
            position: the position of the toast
            close_button: whether to show the close button
            offset: offset of the toast
            dir: directionality of the toast (default: ltr)
            hotkey: Keyboard shortcut that will move focus to the toaster area.
            invert: Dark toasts in light mode and vice versa.
            toast_options: These will act as default options for all toasts. See toast() for all available options.
            gap: Gap between toasts when expanded
            loading_icon: Changes the default loading icon
            pause_when_page_is_hidden: Pauses toast timers when the page is hidden, e.g., when the tab is backgrounded, the browser is minimized, or the OS is locked.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the toaster.

        Returns:
            The toaster component.
        """
        ...

class ToastNamespace(ComponentNamespace):
    provider = staticmethod(Toaster.create)
    options = staticmethod(ToastProps)
    info = staticmethod(Toaster.toast_info)
    warning = staticmethod(Toaster.toast_warning)
    error = staticmethod(Toaster.toast_error)
    success = staticmethod(Toaster.toast_success)
    dismiss = staticmethod(Toaster.toast_dismiss)

    @staticmethod
    def __call__(
        message: str = "", level: Optional[str] = None, **props
    ) -> "Optional[EventSpec]":
        """Send a toast message.

        Args:
            message: The message to display.
            level: The level of the toast.
            **props: The options for the toast.

        Raises:
            ValueError: If the Toaster component is not created.

        Returns:
            The toast event.
        """
        ...

toast = ToastNamespace()
