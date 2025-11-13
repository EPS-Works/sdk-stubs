from ..parser import Parser as _Parser
from .ubx import UBX as UBX
from typing import Callable

class Parser(_Parser):
    """Stateful parser for streaming UBX data.

    This class extends a generic Parser and implements a state machine to parse incoming
    bytes from a data stream into complete UBX sentences. It handles validation, buffering,
    and extraction of structured message data from valid sentences.
    """
    def __init__(self, callback: Callable[[UBX], None] | None = None, on_error: Callable[[Exception], None] | None = None) -> None:
        """Initialize the Parser instance.

        This constructor initializes the parser by resetting its internal state.
        It sets up the parser to be ready for processing incoming UBX data streams.
        """
    def reset(self) -> None:
        """Reset the parser state.

        Resets the parser state to its initial state and clears any partial
        message data. This method is called automatically when a valid message
        is parsed or when the parser is initialized.
        """
    def process(self, data: int) -> bytes | None:
        """Process and accumulate data bytes to form a complete UBX message.

        This method appends incoming data bytes to the current message buffer,
        resetting the buffer when a start delimiter is encountered. It
        continues to accumulate bytes until a complete message with a valid
        checksum is detected or the maximum message length is exceeded.

        Args:
            data: The incoming data byte to be processed.

        Returns:
            The complete UBX message as bytes if a valid message is formed,
            otherwise None.
        """
    def parse(self, data: bytes) -> UBX: ...
