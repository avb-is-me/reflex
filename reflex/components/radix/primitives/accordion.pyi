"""Stub file for reflex/components/radix/primitives/accordion.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, List, Literal, Optional, Tuple, Union, overload

from reflex.components.component import Component, ComponentNamespace
from reflex.components.lucide.icon import Icon
from reflex.components.radix.primitives.base import RadixPrimitiveComponent
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

LiteralAccordionType = Literal["single", "multiple"]
LiteralAccordionDir = Literal["ltr", "rtl"]
LiteralAccordionOrientation = Literal["vertical", "horizontal"]
LiteralAccordionVariant = Literal["classic", "soft", "surface", "outline", "ghost"]
DEFAULT_ANIMATION_DURATION = 250
DEFAULT_ANIMATION_EASING = "cubic-bezier(0.87, 0, 0.13, 1)"

class AccordionComponent(RadixPrimitiveComponent):
    def add_style(self): ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "AccordionComponent":
        """Create the component.

        Args:
            *children: The children of the component.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

def on_value_change(value: Var[str | List[str]]) -> Tuple[Var[str | List[str]]]: ...

class AccordionRoot(AccordionComponent):
    def add_style(self): ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        type: Optional[
            Union[Literal["multiple", "single"], Var[Literal["multiple", "single"]]]
        ] = None,
        value: Optional[Union[List[str], Var[Union[List[str], str]], str]] = None,
        default_value: Optional[
            Union[List[str], Var[Union[List[str], str]], str]
        ] = None,
        collapsible: Optional[Union[Var[bool], bool]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        dir: Optional[Union[Literal["ltr", "rtl"], Var[Literal["ltr", "rtl"]]]] = None,
        orientation: Optional[
            Union[
                Literal["horizontal", "vertical"],
                Var[Literal["horizontal", "vertical"]],
            ]
        ] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        duration: Optional[Union[Var[int], int]] = None,
        easing: Optional[Union[Var[str], str]] = None,
        show_dividers: Optional[Union[Var[bool], bool]] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
        on_value_change: Optional[EventType[str | List[str]]] = None,
        **props,
    ) -> "AccordionRoot":
        """Create the component.

        Args:
            *children: The children of the component.
            type: The type of accordion (single or multiple).
            value: The value of the item to expand.
            default_value: The default value of the item to expand.
            collapsible: Whether or not the accordion is collapsible.
            disabled: Whether or not the accordion is disabled.
            dir: The reading direction of the accordion when applicable.
            orientation: The orientation of the accordion.
            radius: The radius of the accordion corners.
            duration: The time in milliseconds to animate open and close
            easing: The easing function to use for the animation.
            show_dividers: Whether to show divider lines between items.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class AccordionItem(AccordionComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        header: Optional[
            Union[Component, Var[Optional[Union[Component, str]]], str]
        ] = None,
        content: Optional[
            Union[Component, Var[Optional[Union[Component, str]]], str]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "AccordionItem":
        """Create an accordion item.

        Args:
            *children: The list of children to use if header and content are not provided.
            value: A unique identifier for the item.
            disabled: When true, prevents the user from interacting with the item.
            header: The header of the accordion item.
            content: The content of the accordion item.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the accordion item.

        Returns:
            The accordion item.
        """
        ...

    def add_style(self) -> dict[str, Any] | None: ...

class AccordionHeader(AccordionComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "AccordionHeader":
        """Create the Accordion header component.

        Args:
            *children: The children of the component.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Accordion header Component.
        """
        ...

    def add_style(self) -> dict[str, Any] | None: ...

class AccordionTrigger(AccordionComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "AccordionTrigger":
        """Create the Accordion trigger component.

        Args:
            *children: The children of the component.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Accordion trigger Component.
        """
        ...

    def add_style(self) -> dict[str, Any] | None: ...

class AccordionIcon(Icon):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[Union[Var[int], int]] = None,
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
    ) -> "AccordionIcon":
        """Create the Accordion icon component.

        Args:
            *children: The children of the component.
            size: The size of the icon in pixels.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Accordion icon Component.
        """
        ...

class AccordionContent(AccordionComponent):
    def add_imports(self) -> dict: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "surface"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "AccordionContent":
        """Create the Accordion content component.

        Args:
            *children: The children of the component.
            color_scheme: The color scheme of the component.
            variant: The variant of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Accordion content Component.
        """
        ...

    def add_custom_code(self) -> list[str]: ...
    def add_style(self) -> dict[str, Any] | None: ...

class Accordion(ComponentNamespace):
    content = staticmethod(AccordionContent.create)
    header = staticmethod(AccordionHeader.create)
    item = staticmethod(AccordionItem.create)
    icon = staticmethod(AccordionIcon.create)
    root = staticmethod(AccordionRoot.create)
    trigger = staticmethod(AccordionTrigger.create)

accordion = Accordion()
