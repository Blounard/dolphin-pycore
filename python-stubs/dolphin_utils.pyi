"""Module for various utilities."""


def get_script_dir() -> str:
    """
    Returns the path to the Scripts directory, \
        which is found in the Load folder inside of the user directory by default.

    :return: value as string
    """


def open_dir() -> str:
    """
    Prompts the user to open a file.

    :return: value as string
    """


def start_framedump() -> None:
    """Starts a framedump."""


def stop_framedump() -> None:
    """Stops a framedump."""


def is_framedumping() -> bool:
    """
    Checks if a framedump is occuring.

    :return: value as bool
    """


def start_audiodump() -> None:
    """Starts an audiodump."""


def stop_audiodump() -> None:
    """Stops an audiodump."""


def is_audiodumping() -> bool:
    """
    Checks if an audiodump is occuring.

    :return: value as bool
    """


def save_screenshot(filename: str | None = None) -> None:
    """Saves a screenshot of the running game."""


def toggle_play() -> None:
    """Plays/Pauses the current game."""


def is_paused() -> bool:
    """
    Checks if the emulation is currently paused.

    :return: value as bool
    """
	
	
def renderer_has_focus() -> bool:
    """
    Checks if the render window has focus.

    :return: value as bool
    """


def renderer_geometry() -> (int, int, int, int):
    """
    Get the geometry value of the rendering QtWidget

    :return: (x, y, width, height) as (int, int, int, int)
    """