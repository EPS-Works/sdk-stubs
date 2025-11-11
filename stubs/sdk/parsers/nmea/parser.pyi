from ..parser import Parser as _Parser
from .nmea import NMEA as NMEA
from typing import Callable

class Parser(_Parser):
    """Stateful parser for streaming NMEA data.

    This class extends a generic Parser and implements a state machine to parse incoming
    bytes from a data stream into complete NMEA sentences. It handles validation, buffering,
    and extraction of structured message data from valid sentences.
    """
    def __init__(self, callback: Callable[[NMEA], None] | None = None) -> None: ...
    def reset(self) -> None:
        """Reset the parser state.

        Resets the parser state to its initial state and clears any partial
        message data. This method is called automatically when a valid message
        is parsed or when the parser is initialized.
        """
    def process(self, data: int) -> bytes | None:
        """Process and accumulate data bytes to form a complete NMEA message.

        This method appends incoming data bytes to the current message buffer,
        resetting the buffer when a start delimiter ('$') is encountered. It
        continues to accumulate bytes until a complete message with a valid
        checksum is detected or the maximum message length is exceeded.

        Args:
            data: The incoming data byte to be processed.

        Returns:
            The complete NMEA message as bytes if a valid message is formed,
            otherwise None.
        """
    def parse(self, data: bytes) -> NMEA:
        """Parse a raw NMEA message into a structured object.

        Args:
            data: A raw NMEA message as bytes.

        Returns:
            A structured NMEA object.
        """
    def find(self, data: bytes) -> tuple[None | bytes, int | None]:
        """Find a complete NMEA message in a byte sequence.

        Args:
            data: The data to search for a complete NMEA message.

        Returns:
            A tuple containing the found NMEA message as bytes if found, None
            otherwise, and the position of the message in the data if found,
            None otherwise. The position is the index of the first byte of the
            message.
        """
