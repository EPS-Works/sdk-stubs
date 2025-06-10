from sdk.dio import DigitalIO as DigitalIO
from typing import Callable

class GNSS:
    """Interface for controlling a GNSS receiver over UART.

    This class represents a GNSS receiver connected via UART. It handles low-level serial
    communication, and provides methods to start and stop the streaming of GNSS messages
    to specified ports.

    The class supports power management through an optional power control pin and
    provides access to various GNSS signals through DigitalIO pins.
    """
    interruption: DigitalIO | None
    timepulse: DigitalIO | None
    geofence: DigitalIO | None
    def __init__(self, port: int | str, baudrate: int = ..., power: DigitalIO | None = None) -> None:
        """Initialize the GNSS interface.

        Args:
            port: The UART port to use for communication with the GNSS receiver.
            baudrate: The baudrate to use for communication with the GNSS receiver.
            power: Optional pin ID for power control of the GNSS receiver.
        """
    @property
    def baudrate(self) -> int:
        """Get the current baudrate used for communication with the GNSS receiver.

        Returns:
            The baudrate as an integer.
        """
    @baudrate.setter
    def baudrate(self, baudrate) -> None:
        """Set the baudrate used for communication with the GNSS receiver.

        Args:
            baudrate: The new baudrate to use for communication with the GNSS receiver.
        """
    @property
    def buffer_size(self) -> int:
        """Get the size of the receive buffer for the GNSS receiver.

        Returns:
            The size of the receive buffer in bytes.
        """
    @buffer_size.setter
    def buffer_size(self, size) -> None:
        """Set the size of the receive buffer for the GNSS receiver.

        Args:
            size: The new size of the receive buffer in bytes.
        """
    def on(self) -> None:
        """Power on the GNSS receiver.

        This method activates the GNSS receiver by setting the power pin high if available.
        It includes a delay to allow the receiver to initialize properly.
        """
    def off(self) -> None:
        """Power off the GNSS receiver.

        This method deactivates the GNSS receiver by setting the power pin low if available.
        It includes a delay to ensure proper shutdown.
        """
    def write(self, data: bytes) -> None:
        """Write data to the GNSS receiver.

        Args:
            data: The data to write to the GNSS receiver.
        """
    def read(self, nbytes: int | None = None) -> bytes:
        """Read data from the GNSS receiver.

        Args:
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The data read from the GNSS receiver.
        """
    def readinto(self, buffer: bytearray | memoryview, nbytes: int | None = None) -> int:
        """Read data from the GNSS receiver into a buffer.

        Args:
            buffer: The bytearray to read into.
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The number of bytes read into the buffer.
        """
    def any(self) -> int:
        """Check if data is available to read.

        Returns:
            The number of bytes available to read, or 0 if no data is available.
        """
    def flush(self) -> None:
        """Flush the UART buffer."""
    def stream(self, messages: list[str], port: int | str, frequency: int | None = None) -> Callable[[], None]:
        """Start streaming GNSS messages.

        This method configures the GNSS receiver to stream specified messages to a port
        at the given frequency.

        Args:
            messages: List of message types to stream.
            port: The port to stream messages to.
            frequency: Optional frequency in Hz for message streaming.

        Returns:
            A callable that can be used to stop the streaming.

        Raises:
            ValueError: If any message type is not supported.
            OSError: If the stream cannot be started.
        """
    def halt(self, messages: list[str], port: int | str) -> None:
        """Stop streaming GNSS messages.

        Args:
            messages: List of message types to stop streaming.
            port: The port to stop streaming messages to.

        Raises:
            ValueError: If any message type is not supported.
            OSError: If the stream cannot be started.
        """
