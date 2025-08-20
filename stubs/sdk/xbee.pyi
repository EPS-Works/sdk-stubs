from .dio import DigitalIO as DigitalIO

class XBeeSocket:
    """XBee Socket interface for UART-based modules with power control.

    This class provides a simple wrapper around UART communication with
    optional power management through a digital I/O pin. It's designed
    to work with any module that fits the XBee socket form factor.

    The socket handles power sequencing and provides standard UART
    communication methods for reading and writing data.
    """
    def __init__(self, port: int, baudrate: int = ..., power: DigitalIO | None = None, rxbuf: int = ...) -> None:
        """Initialize the XBee socket interface.

        Args:
            port: The UART port to use for communication.
            baudrate: The baudrate for UART communication (default: 115200).
            power: Optional power control pin for the module.
            rxbuf: Size of the receive buffer in bytes (default: 512).
        """
    @property
    def baudrate(self) -> int:
        """Get the current baudrate.

        Returns:
            The baudrate as an integer.
        """
    @baudrate.setter
    def baudrate(self, baudrate: int) -> None:
        """Set the baudrate for UART communication.

        Args:
            baudrate: The new baudrate to use.
        """
    @property
    def buffer_size(self) -> int:
        """Get the current receive buffer size.

        Returns:
            The buffer size in bytes.
        """
    @buffer_size.setter
    def buffer_size(self, size: int) -> None:
        """Set the size of the receive buffer.

        Args:
            size: The new buffer size in bytes.
        """
    @property
    def is_on(self) -> bool:
        """Check if the module is powered on.

        Returns:
            True if the module is powered on, False otherwise.
        """
    def on(self, wait: int = 100) -> None:
        """Power on the XBee socket module.

        This method activates the module by setting the power pin high if available.
        It includes a delay to allow the module to initialize properly.

        Args:
            wait: Delay in seconds to allow the module to power up (default: 0.1).
        """
    def off(self, wait: int = 100) -> None:
        """Power off the XBee socket module.

        This method deactivates the module by setting the power pin low if available.
        It includes a delay to ensure proper shutdown.

        Args:
            wait: Delay in seconds to allow the module to power down (default: 0.1).
        """
    def write(self, data: bytes) -> None:
        """Write data to the module.

        Args:
            data: The data to write to the module.
        """
    def read(self, nbytes: int | None = None) -> bytes:
        """Read data from the module.

        Args:
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The bytes read from the module.
        """
    def readinto(self, buffer: bytearray | memoryview, nbytes: int | None = None) -> int | None:
        """Read data from the module into a buffer.

        Args:
            buffer: The bytearray to read into.
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            Number of bytes read, or None if no data available.
        """
    def any(self) -> int:
        """Check if any data is available to read.

        Returns:
            Number of bytes available in the receive buffer.
        """
    def flush(self) -> None:
        """Flush the UART buffers."""
