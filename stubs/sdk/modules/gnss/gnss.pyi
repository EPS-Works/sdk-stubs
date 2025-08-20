from ...dio import DigitalIO as DigitalIO
from ...xbee import XBeeSocket as XBeeSocket
from typing import Callable

class GNSS:
    """Interface for controlling a GNSS receiver over UART.

    This class uses composition with XBeeSocket to provide GNSS-specific functionality including
    message streaming control and access to GNSS-specific signals like timepulse
    and geofence indicators.

    All communication operations are delegated to the XBeeSocket dependency, while this class
    provides GNSS-specific power management and signal handling.
    """
    interruption: DigitalIO | None
    timepulse: DigitalIO | None
    geofence: DigitalIO | None
    def __init__(self, socket: XBeeSocket) -> None:
        """Initialize the GNSS interface.

        Args:
            socket: XBeeSocket instance to use for communication.
        """
    @property
    def baudrate(self) -> int:
        """Get the current baudrate."""
    @baudrate.setter
    def baudrate(self, baudrate: int) -> None:
        """Set the baudrate for UART communication."""
    @property
    def buffer_size(self) -> int:
        """Get the current receive buffer size."""
    @buffer_size.setter
    def buffer_size(self, size: int) -> None:
        """Set the size of the receive buffer."""
    @property
    def is_on(self) -> bool:
        """Check if the module is powered on."""
    def write(self, data: bytes) -> None:
        """Write data to the module."""
    def read(self, nbytes: int | None = None) -> bytes:
        """Read data from the module."""
    def readinto(self, buffer: bytearray | memoryview, nbytes: int | None = None) -> int | None:
        """Read data from the module into a buffer."""
    def any(self) -> int:
        """Check if any data is available to read."""
    def flush(self) -> None:
        """Flush the UART buffers."""
    def on(self) -> None:
        """Power on the GNSS receiver.

        This method activates the GNSS receiver by setting the power pin high if available.
        It includes a longer delay to allow the GNSS receiver to initialize properly.
        """
    def off(self) -> None:
        """Power off the GNSS receiver.

        This method deactivates the GNSS receiver by setting the power pin low if available.
        It includes a delay to ensure proper shutdown.
        """
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
