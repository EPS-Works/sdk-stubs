import types
from .parsers.parser import Parser as Parser
from .serial import Serial as Serial
from typing import Any, Callable

class Stream:
    """Serial data stream processor with parser support.

    This class provides a high-level interface for reading and processing serial data
    streams. It supports multiple parsers, configurable throttling, and timeouts.
    The class can be used as a context manager for automatic resource cleanup and as
    an iterator for convenient message processing.
    """
    def __init__(self, serial: Serial, parsers: list[Parser] | None = None, raw: bool = False, throttle: int = 10, timeout: int | None = None, buffer_size: int = 256) -> None:
        """Initialize a serial data stream processor.

        Args:
            serial: The Serial interface providing the data stream.
            parsers: Optional list of Parser classes for message parsing.
            raw: If True, return raw bytes instead of parsed messages.
            throttle: Milliseconds to wait between reads (default: 10).
            timeout: Optional timeout in milliseconds for read operations.
            buffer_size: Size of internal buffer (default: 256).
        """
    def cleanup(self) -> None:
        """Clean up stream resources.

        This method resets the internal buffer.
        It is automatically called when the stream is closed or garbage collected.
        """
    def __aiter__(self) -> Stream: ...
    async def __anext__(self) -> Any: ...
    def __iter__(self) -> Stream: ...
    def __next__(self) -> Any: ...
    def __enter__(self) -> Stream: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def stream(parsers: list[type[Parser]] | None = None, raw: bool = False, throttle: int = 10, timeout: int | None = None, buffer_size: int = 256) -> Callable[[Callable[[Any, Serial], None]], Callable[[Serial], Any]]:
    """Create a message processor decorator for serial streams.

    This decorator transforms a function into an automatic message processor for
    serial data streams. It handles stream initialization, iteration, and cleanup,
    calling the decorated function with each parsed message.

    Args:
        parsers: Optional list of Parser classes for message parsing.
        raw: If True, pass raw bytes instead of parsed messages.
        throttle: Milliseconds to wait between reads (default: 10).
        timeout: Optional timeout in milliseconds for read operations.
        buffer_size: Size of internal buffer (default: 256).

    Returns:
        A decorator that wraps a function to process messages from a serial stream.

    The decorated function should accept 2 arguments:
        - msg: The parsed message or raw bytes
        - serial: The Serial interface instance
    """
