from typing import Protocol

class Serial(Protocol):
    """Protocol defining the interface for serial communication.

    This protocol specifies the minimum interface required for serial communication
    implementations. Classes implementing this protocol must provide methods for
    reading, writing, and flushing serial data.
    """
    def read(self, nbytes: int | None = None) -> bytes:
        """Read data from the serial port.

        Args:
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The bytes read from the serial port.
        """
    def readinto(self, buffer: bytearray | memoryview, nbytes: int | None = None) -> int | None:
        """Read data from the serial port into a bytearray.

        Args:
            buffer: The bytearray to read into.
            nbytes: Number of bytes to read. If None, reads all available data.
        """
    def write(self, data: bytes) -> None:
        """Write data to the serial port.

        Args:
            data: The bytes to write to the serial port.
        """

class SerialBuffer:
    """Buffered circular serial data reader with multiple cursors.

    This class provides a rolling buffer for serial data with support for multiple
    independent cursors. Each cursor can track its position in the buffer.
    The buffer automatically wraps around when the end of the buffer is reached.
    """
    size: int
    def __init__(self, serial: Serial, size: int = ...) -> None:
        """Initialize the serial buffer.

        Args:
            serial: A Serial implementation that provides the raw serial data.
            size: Buffer size in bytes. New data is wrapped around the circular buffer.
        """
    def readinto(self, buffer: bytearray | memoryview, cursor: str = '__cursor__', nbytes: int | None = None) -> None:
        """Read data from the buffer or underlying serial port into a bytearray.

        Args:
            buffer: The bytearray to read into.
            cursor: Name of the cursor to read from.
            nbytes: Number of bytes to read. If None, reads up to the buffer size.
        """
    def read(self, cursor: str = '__cursor__', nbytes: int | None = None) -> bytes:
        """Read data from the buffer or underlying serial port.

        Args:
            cursor: Name of the cursor to read from.
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The bytes read from the buffer, starting from the cursor position.
        """
    def cursor(self, name: str) -> SerialBufferCursor:
        """Create a new cursor at the current buffer position.

        Args:
            name: Unique identifier for the new cursor.

        Returns:
            A SerialBufferCursor instance bound to this buffer.

        Raises:
            ValueError: If a cursor with the specified name already exists.
        """
    def remove(self, cursor: str) -> None:
        """Remove a cursor from the buffer.

        Args:
            cursor: Name of the cursor to remove.
        """
    def write(self, data: bytes) -> None:
        """Write data to the underlying serial port.

        Args:
            data: The bytes to write to the serial port.
        """

class SerialBufferCursor:
    """Cursor for reading from a SerialBuffer.

    This class provides a convenient interface for reading from a specific position
    in a SerialBuffer. The cursor automatically flushes its position when garbage
    collected to prevent memory leaks.
    """
    def __init__(self, buffer: SerialBuffer, name: str) -> None:
        """Initialize a new cursor.

        This constructor should not be called directly. Use SerialBuffer.cursor()
        instead to create new cursors.

        Args:
            buffer: The SerialBuffer this cursor belongs to.
            name: The name identifying this cursor in the buffer.
        """
    def read(self, nbytes: int | None = None) -> bytes:
        """Read data from the buffer starting at this cursor's position.

        Args:
            nbytes: Number of bytes to read. If None, reads all available data.

        Returns:
            The bytes read from the buffer.
        """
    def readinto(self, buffer: bytearray | memoryview, nbytes: int | None = None) -> None:
        """Read data from the buffer starting at this cursor's position into a buffer.

        Args:
            buffer: The bytearray to read into.
            nbytes: Number of bytes to read. If None, reads the buffer length.
        """
    def write(self, data: bytes) -> None:
        """Write data to the underlying serial port.

        Args:
            data: The bytes to write to the serial port.
        """
    def __del__(self) -> None: ...
