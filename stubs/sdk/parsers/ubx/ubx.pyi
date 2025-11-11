from ...utils.lazy import LazyFactory as LazyFactory
from .definitions import DEFINITIONS as DEFINITIONS
from .message import Field as Field, Message as Message, Repeat as Repeat
from _typeshed import Incomplete

LOOKUP: dict[tuple[int, int], str]
MESSAGES: Incomplete

class UBX:
    """UBX protocol message parser and generator.

    This class implements the UBX protocol parser interface, providing methods
    for finding, validating, and parsing UBX messages. It supports message
    checksum validation and proper message framing.
    """
    name: str
    SYNC1: int
    SYNC2: int
    def __init__(self, name: str, **kwargs) -> None:
        '''Initialize a UBX message.

        Args:
            name: Message identifier (e.g., "NAV-PVT").
            **kwargs: Message-specific field values.

        Raises:
            ValueError: If the message name is not supported.
            TypeError: If a field value does not match the expected type.
        '''
    @classmethod
    def checksum(cls, data: bytes) -> tuple[int, int]:
        """Calculates the UBX checksum for the given data.

        Args:
            data: The data over which to calculate the checksum.

        Returns:
            A tuple of two bytes, (ck_a, ck_b), representing the UBX checksum.
        """
    @classmethod
    def validate(cls, data: bytes) -> None:
        """Validates the given UBX message.

        Args:
            data: The UBX message to validate.

        Raises:
            AssertionError: If any of the checks fail.
        """
    @classmethod
    def is_valid(cls, data: bytes) -> bool:
        """Check if the given UBX message is valid.

        Args:
            data: The UBX message to validate.

        Returns:
            True if the given UBX message is valid, False otherwise.
        """
    @classmethod
    def wrap(cls, name: str, payload: bytes) -> bytes:
        """Wrap the given payload into a UBX message.

        Args:
            name: The name of the UBX message.
            payload: The payload to wrap.

        Raises:
            ValueError: If the message name is not supported.
        """
    @classmethod
    def parse(cls, data: bytes, validate: bool = True) -> UBX:
        """Parse a UBX message from bytes.

        Args:
            data: A byte sequence representing the UBX message.
            validate: Whether to validate the message before parsing.

        Returns:
            A UBX message instance parsed from the given data.

        Raises:
            ValueError: If the message name is not supported.
            AssertionError: If validation fails.
        """
    def serialize(self) -> bytes:
        """Serialize the UBX message instance into a byte sequence.

        Returns:
            The serialized UBX message as a byte sequence. Returns an empty
            byte sequence if the message format is not found.
        """
    @classmethod
    def register(cls, name: str, class_id: int, msg_id: int, fields: list[Field | Repeat]) -> None:
        '''Register a new UBX message type.

        Args:
            name: Message identifier (e.g., "NAV-PVT").
            class_id: Message class ID.
            msg_id: Message ID within the class.
            fields: List of Field or Repeat objects defining the message structure.

        Raises:
            ValueError: If a message with the same name is already registered.
        '''
