from .field import Field as Field
from .repeat import Repeat as Repeat
from typing import Any, Callable, Iterable

def group_by(iterable: Iterable, condition: Callable[[Any], bool]) -> tuple[list, list]:
    """Split an iterable into two lists based on a condition.

    Args:
        iterable: The iterable to split.
        condition: Function that evaluates each item and returns a boolean.

    Returns:
        Tuple containing two lists: items that satisfy the condition and items that don't.
    """

class Message:
    """Defines the format and structure of a UBX message.

    This class handles the binary format of UBX messages, including fixed and
    repeated fields, and provides methods for parsing and serializing message data.
    """
    firm: tuple[int, int]
    def __init__(self, firm: tuple[int, int], fields: list[Field | Repeat]) -> None:
        """Initialize a UBX message format.

        Args:
            firm: Tuple of (class ID, message ID) identifying the message type.
            fields: List of Field or Repeat objects defining the message structure.

        Raises:
            ValueError: If the message does not contains any fields or
                if it contains multiple repeated fields.
        """
    @property
    def fields(self) -> list[Field | Repeat]:
        """Get all fields in the message in their defined order.

        Returns:
            List of Field and Repeat objects in the order they appear in the message.
        """
    def parse(self, payload: bytes) -> dict[str, Any]:
        """Parse a UBX message payload into structured data.

        Args:
            payload: Byte sequence containing the message data.

        Returns:
            Dictionary mapping field names to their parsed values. Repeated fields
            are represented as lists of named tuples.
        """
    def serialize(self, obj: dict) -> bytes:
        """Serialize structured data into a UBX message payload.

        Args:
            obj: Dictionary mapping field names to their values.

        Returns:
            Byte sequence containing the serialized message data.
        """
