from .models import DataValidity as DataValidity, NavigationMode as NavigationMode, OperationMode as OperationMode, Satellite as Satellite, Talker as Talker
from typing import Callable

def coordinate(value: str) -> float:
    """Convert NMEA coordinate string to decimal degrees.

    Args:
        value: Coordinate string in DDMM.MMMM format.

    Returns:
        Coordinate in decimal degrees (-180.0 to 180.0 for longitude,
        -90.0 to 90.0 for latitude).
    """
def time(value: str) -> tuple[int, int, float]:
    """Convert NMEA time string to time components.

    This function converts time from the NMEA HHMMSS.SS format to a tuple of
    hour, minute, and second components.

    Args:
        value: Time string in HHMMSS.SS format.

    Returns:
        Tuple of (hour, minute, second) where hour and minute are integers
        and second is a float.
    """
Definition = tuple[str, tuple[tuple[str, type, Callable | None], ...], Callable[[str], dict]]
DEFINITIONS: tuple[Definition, ...]
