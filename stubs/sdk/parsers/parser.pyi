from typing import Any

class Parser:
    """Base class for binary data parsers.

    This abstract class defines the interface for parsing binary data streams.
    Subclasses must implement the processing and parsing methods
    to handle specific binary protocols.
    """
    def process(self, data: int) -> bytes | None:
        """Process and accumulate data bytes to form a complete message.

        Args:
            data: The incoming data byte to be processed.

        Returns:
            The complete message as bytes if found, otherwise None.
        """
    def parse(self, data: bytes) -> Any:
        """Parse binary data into a structured object.

        Args:
            data: Binary data to parse.

        Returns:
            Parsed data in an implementation-specific format.
        """
    def reset(self) -> None:
        """Reset the parser state."""
    def find(self, data: bytes) -> list[bytes]:
        """Find a complete message in a byte sequence.

        Args:
            data: The data to search for a complete message.

        Returns:
            A list of complete messages found in the data.
        """
