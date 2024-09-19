"""Wrappers for the state manager."""

from typing import Any

from reflex.state import _split_substate_key, _substate_key, get_state_manager


async def get_state(token, state_cls: Any | None = None):
    """Get the instance of a state for a token.

    Args:
        token: The token for the state.
        state_cls: The class of the state.

    Returns:
        The state instance.
    """
    mng = get_state_manager()
    if state_cls is not None:
        root_state = await mng.get_state(_substate_key(token, state_cls))
    else:
        root_state = await mng.get_state(token)
        _, state_path = _split_substate_key(token)
        state_cls = root_state.get_class_substate(tuple(state_path.split(".")))
    return await root_state.get_state(state_cls)
