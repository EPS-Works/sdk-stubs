from .field import Field as Field
from typing import Generator, NamedTuple

def chunk(data: bytes, size: int) -> Generator[bytes, None, None]:
    """Split a byte sequence into fixed-size chunks.

    Args:
        data: The byte sequence to split.
        size: Size of each chunk in bytes.

    Yields:
        Chunks of the specified size. The last chunk may be smaller if the data
        length is not a multiple of the chunk size.
    """

class Repeat:
    """Represents a repeated field in a UBX message format.

    This class handles variable-length repeated fields in UBX messages, providing
    methods for parsing and serializing arrays of structured data.
    """
    name: str
    def __init__(self, name: str, fields: list[Field]) -> None:
        """Initialize a repeated field definition.

        Args:
            name: Name of the repeated field (typically plural).
            fields: List of Field instances defining the structure of each repetition.

        Raises:
            ValueError: If it has no fields.
        """
    def parse(self, payload: bytes) -> list[NamedTuple]:
        """Parse a byte sequence into a list of structured data.

        Args:
            payload: Byte sequence containing the repeated field data.

        Returns:
            List of named tuples, each representing one repetition of the field.
        """
    def serialize(self, data: list[NamedTuple]) -> bytes:
        """Serialize a list of structured data into a byte sequence.

        Args:
            data: List of named tuples to serialize.

        Returns:
            Byte sequence containing the serialized repeated field data.
        """
