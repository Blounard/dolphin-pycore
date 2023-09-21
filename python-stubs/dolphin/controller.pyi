"""
Module for programmatic inputs.
"""
from typing import TypedDict


class GCInputs(TypedDict, total=False):
    """
    Dictionary describing the state of a GameCube controller.
    Boolean keys (buttons): True means pressed, False means released.
    Float keys for triggers: 0 means fully released, 1 means fully pressed.
    Float keys for sticks: 0 means neutral, ranges from -1 to 1.
    """
    A: bool
    B: bool
    X: bool
    Y: bool
    Z: bool
    Start: bool
    Up: bool
    Down: bool
    Left: bool
    Right: bool
    L: bool
    R: bool
    StickX: float
    StickY: float
    CStickX: float
    CStickY: float
    TriggerLeft: float
    TriggerRight: float


class WiimoteInputs(TypedDict, total=False):
    """
    Dictionary describing the state of a Wii Remote controller.
    Boolean keys (buttons): True means pressed, False means released.
    """
    A: bool
    B: bool
    One: bool
    Two: bool
    Plus: bool
    Minus: bool
    Home: bool
    Up: bool
    Down: bool
    Left: bool
    Right: bool


class WiiClassicInputs(TypedDict, total=False):
    """
    Dictionary describing the state of a Wii Classic controller.
    Boolean keys: True means pressed, False means released.
    Float keys for triggers: 0 means fully released, 1 means fully pressed.
    Float keys for sticks: 0 means neutral, ranges from -1 to 1.
    """
    A: bool
    B: bool
    X: bool
    Y: bool
    ZL: bool
    ZR: bool
    Plus: bool
    Minus: bool
    Home: bool
    Up: bool
    Down: bool
    Left: bool
    Right: bool
    L: bool
    R: bool
    TriggerLeft: float
    TriggerRight: float
    LeftStickX: float
    LeftStickY: float
    RightStickX: float
    RightStickY: float


class WiiNunchukInputs(TypedDict, total=False):
    """
    Dictionary describing the state of a Wii Nunchuk controller.
    Boolean keys (buttons): True means pressed, False means released.
    Float keys for sticks: 0 means neutral, ranges from -1 to 1.
    """
    C: bool
    Z: bool
    StickX: float
    StickY: float


class GBAInputs(TypedDict, total=False):
    """
    Dictionary describing the state of a GameBoy Advance controller.
    Boolean keys (buttons): True means pressed, False means released.
    """
    A: bool
    B: bool
    L: bool
    R: bool
    Start: bool
    Select: bool
    Up: bool
    Down: bool
    Left: bool
    Right: bool


def get_gc_buttons(controller_id: int, /) -> GCInputs:
    """
    Retrieves the current input map for the given GameCube controller.
    All keys of :class:`GCInputs` will be present in the returned dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """


def set_gc_buttons(controller_id: int, inputs: GCInputs, /) -> None:
    """
    Sets the current input map for the given GameCube controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_gc_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """


def get_wiimote_buttons(controller_id: int, /) -> WiimoteInputs:
    """
    Retrieves the current input map for the given Wii remote.
    All keys of :class:`WiimoteInputs` will be present in the returned
    dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """


def set_wiimote_buttons(controller_id: int, inputs: WiimoteInputs,
                        /) -> None:
    """
    Sets the current input map for the given Wii remote.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_wiimote_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """


def get_wiimote_pointer(controller_id: int, /) -> (float, float):
    """
    Returns the current wii pointer position, in screen coordinates.
    For x, -1 and 1 represent the left and right edge of the screen.
    For y, -1 and 1 represent the bottom and top edge of the screen.
    The x and y values are allowed to exceed the [-1, 1] range.
    :param controller_id: 0-based index of the controller
    :return: The screen coordinates as a tuple (x, y)
    """


def set_wiimote_pointer(controller_id: int, x: float, y: float, /) -> None:
    """
    Sets the current wii pointer position, in screen coordinates.

    | For x, -1 and 1 represent the left and right edge of the screen.
    | For y, -1 and 1 represent the bottom and top edge of the screen.
    The x and y values are allowed to exceed the [-1, 1] range.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: horizontal screen coordinate, where positive means right
    :param y: vertical screen coordinate, where positive means up
    """


def get_wiimote_acceleration(controller_id: int, /) -> (float, float, float):
    """
    Returns the current wii remote acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    :param controller_id: 0-based index of the controller
    :return: The current acceleration as a tuple (x, y, z)
    """


def set_wiimote_acceleration(controller_id: int,
                             x: float, y: float, z: float, /) -> None:
    """
    Sets the current wii remote acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the acceleration vector
    :param y: y-component of the acceleration vector
    :param z: z-component of the acceleration vector
    """


def get_wiimote_angular_velocity(controller_id: int, /) \
        -> (float, float, float):
    """
    Returns the current wii remote angular velocity, as a vector (x, y, z).
    The angular velocity is measured in radians/s.
    :param controller_id: 0-based index of the controller
    :return: The current angular velocity as a tuple (x, y, z)
    """


def set_wiimote_angular_velocity(controller_id: int,
                                 x: float, y: float, z: float, /) -> None:
    """
    Sets the current wii remote angular velocity, as a vector (x, y, z).
    The angular velocity is measured in radians/s.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the angular velocity vector
    :param y: y-component of the angular velocity vector
    :param z: z-component of the angular velocity vector
    """


def get_wii_classic_buttons(controller_id: int, /) -> WiiClassicInputs:
    """
    Retrieves the current input map for the given Wii Classic controller.
    All keys of :class:`WiiClassicInputs` will be present in the returned
    dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """


def set_wii_classic_buttons(controller_id: int, inputs: WiiClassicInputs,
                            /) -> None:
    """
    Sets the current input map for the given Wii Classic controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_wii_classic_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """


def get_wii_nunchuk_buttons(controller_id: int, /) -> WiiNunchukInputs:
    """
    Retrieves the current input map for the given Wii Nunchuk controller.
    All keys of :class:`WiiNunchukInputs` will be present in the returned
    dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """


def set_wii_nunchuk_buttons(controller_id: int, inputs: WiiNunchukInputs,
                            /) -> None:
    """
    Sets the current input map for the given Wii Nunchuk controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the C button like this::

        controller.set_wii_nunchuk_buttons(0, {"C": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """


def get_wii_nunchuk_acceleration(controller_id: int, /) \
        -> (float, float, float):
    """
    Returns the current wii nunchuk acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    :param controller_id: 0-based index of the controller
    :return: The current acceleration as a tuple (x, y, z)
    """


def set_wii_nunchuk_acceleration(controller_id: int,
                                 x: float, y: float, z: float, /) -> None:
    """
    Sets the current wii nunchuk acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the acceleration vector
    :param y: y-component of the acceleration vector
    :param z: z-component of the acceleration vector
    """


def get_gba_buttons(controller_id: int, /) -> GBAInputs:
    """
    Retrieves the current input map for the given GameBoy Advance controller.
    All keys of :class:`GBAInputs` will be present in the returned dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """


def set_gba_buttons(controller_id: int, inputs: GBAInputs, /) -> None:
    """
    Sets the current input map for the given GameBoy Advance controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_gba_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """
