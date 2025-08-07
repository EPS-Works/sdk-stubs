from typing import Any, Callable

def chunks(array: list, size: int, pad: Any = None):
    """Split a list into fixed-size chunks with optional padding.

    This utility function divides a list into chunks of a specified size, with
    optional padding for the last chunk if it's smaller than the requested size.

    Args:
        array: The list to be divided into chunks.
        size: The desired size of each chunk.
        pad: Optional value used to pad the last chunk if it is smaller than size.

    Yields:
        A chunk of the specified size from the list.
    """
def to_canbus_filters(pattern: str, extended: bool = False) -> list[tuple[int, int]]:
    """Convert regex patterns to CAN bus message filters.

    This function converts regex patterns for CAN message IDs into ID and mask
    pairs suitable for hardware filtering. It supports various pattern formats
    including exact matches, wildcards, ranges, and lists.

    Args:
        pattern: Regular expression pattern matching desired CAN IDs.
        extended: Whether to use extended (29-bit) or standard (11-bit) IDs.

    Returns:
        List of filter tuples (base_id, mask) for hardware configuration.

    Raises:
        ValueError: If the pattern is invalid or cannot be converted to a valid
            hardware filter configuration.
    """

class CANBus:
    """CAN bus controller for hardware communication.

    This class provides a high-level interface for CAN bus operations, including
    message transmission, reception, and filtering.

    The class supports both standard (11-bit) and extended (29-bit) message IDs,
    configurable baudrates, and message filtering capabilities. It also provides
    silent mode for bus monitoring without transmission.
    """
    def __init__(self, port: int = 1, baudrate: int = 500000, silent: bool = False) -> None:
        """Initialize a CAN bus controller.

        Args:
            port: The CAN bus port number (default: 1).
            baudrate: The communication speed in bits per second (default: 500000).
            silent: Whether to operate in silent mode, only listening without
                transmission (default: False).
        """
    @property
    def filters(self) -> int:
        """Get the number of filters configured on the CAN bus.

        Returns:
            The number of filters configured on the CAN bus.
        """
    def silent(self, activate: bool = True) -> None:
        """Set the CAN bus to silent mode.

        In silent mode, the CAN bus will only listen to the bus and not
        transmit any messages. It is useful for sniffing the bus.

        Args:
            activate: Whether to activate the silent mode
        """
    @property
    def baudrate(self) -> int:
        """Get the baudrate for the CAN bus.

        Returns:
            The baudrate for the CAN bus
        """
    @baudrate.setter
    def baudrate(self, baudrate: int) -> None:
        """Set the baudrate for the CAN bus.

        Args:
            baudrate: The baudrate to set for the CAN bus.
        """
    def write(self, msg_id: int, data: bytes, extended: bool = False, timeout: int = 0) -> None:
        """Send data to the CAN bus

        Args:
            msg_id: The message ID to use.
            data: The data to send to the CAN bus.
            extended: Whether to use an extended or simple ID
            timeout: The timeout in milliseconds to wait for the message to be sent
        """
    def read(self, fifo: int = 0, timeout: int = 500) -> tuple[int, bool, bytes] | tuple[None, None, None]:
        """Read a message from the CAN bus.

        Args:
            fifo: The FIFO buffer to read from (default: 0).
            timeout: Maximum time to wait for a message in milliseconds (default: 500).

        Returns:
            A tuple of (msg_id, extended, data) if a message is received, or
            (None, None, None) if no message is available within the timeout period.
        """
    def filter(self, pattern, fifo: int | None = 0, extended: bool = False) -> Callable[[], None]:
        """Set a filter for the CAN bus.

        Args:
            pattern: The regex pattern to use for the filter.
            fifo: The FIFO to use for the filter. Must be 0 or 1.
            extended: Whether to use an extended or simple ID.

        Returns:
            A function that clears the filter when called.
        """
    def attach(self, callback: Callable[[int, bool, bytes], None], fifo: int | None = 0) -> Callable[[], None]:
        """Attach a callback function to the CAN bus for message reception.

        Args:
            callback: The callback function to attach to the CAN bus.
        """
