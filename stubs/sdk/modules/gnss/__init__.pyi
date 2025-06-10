from .gnss import GNSS as GNSS
from .ublox import Ublox as Ublox
from sdk.dio import DigitalIO as DigitalIO
from typing import NamedTuple

MODULES: dict[str, type[GNSS]]

class GNSSFactory:
    """Factory for creating and managing GNSS receiver instances.

    This class manages the creation and tracking of GNSS receiver instances,
    ensuring proper initialization and preventing duplicate mounting of
    receivers in the same slot.

    The factory supports different types of GNSS modules and handles their
    configuration with appropriate UART settings and power control.
    """
    def __init__(self, slots: NamedTuple, modules: NamedTuple) -> None:
        """Initialize the GNSS factory.

        This method sets up the factory with available serial slots and
        supported GNSS module types.

        Args:
            slots: A NamedTuple containing available serial slots with optional power pins.
            modules: A NamedTuple containing available GNSS module types.
        """
    def create(self, slot: tuple[int, DigitalIO | None], module: str) -> GNSS:
        """Create a new GNSS receiver instance.

        This method creates and initializes a GNSS receiver of the specified type
        in the given slot. It ensures the slot is valid and not already in use.

        Args:
            slot: A tuple containing (port number, optional power pin) for the receiver.
            module: The type of GNSS module to instantiate.

        Returns:
            An initialized GNSS receiver instance.

        Raises:
            ValueError: If the slot is invalid, already mounted, or the module type
                       is not supported.
        """
