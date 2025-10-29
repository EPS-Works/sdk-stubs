from .parser import Parser as Parser
from _typeshed import Incomplete
from typing import Any, Callable, Generator, Iterable, NamedTuple

def group_by(iterable: Iterable, condition: Callable[[Any], bool]) -> tuple[list, list]:
    """Split an iterable into two lists based on a condition.

    Args:
        iterable: The iterable to split.
        condition: Function that evaluates each item and returns a boolean.

    Returns:
        Tuple containing two lists: items that satisfy the condition and items that don't.
    """
def chunk(data: bytes, size: int) -> Generator[bytes, None, None]:
    """Split a byte sequence into fixed-size chunks.

    Args:
        data: The byte sequence to split.
        size: Size of each chunk in bytes.

    Yields:
        Chunks of the specified size. The last chunk may be smaller if the data
        length is not a multiple of the chunk size.
    """

class Format:
    """Format specifiers for binary data packing and unpacking.

    This class provides format specifiers for various data types used in UBX messages,
    including integers, floats, strings, and padding bytes.
    """
    U1: str
    I1: str
    X1: str
    U2: str
    I2: str
    X2: str
    U4: str
    I4: str
    X4: str
    U8: str
    I8: str
    R4: str
    R8: str
    CH: Callable[[int], str]
    PAD: Callable[[int], str]
    ADAPTIVE: str

class Field(NamedTuple):
    name: Incomplete
    format: Incomplete

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

DEFINITIONS: dict[str, tuple[tuple[int, int], tuple[tuple[str, str | tuple[tuple[str, str], ...]], ...]]]
MESSAGES: dict[str, Message]
LOOKUP: dict[tuple[int, int], str]

class UBX:
    """UBX protocol message parser and generator.

    This class implements the UBX protocol parser interface, providing methods
    for finding, validating, and parsing UBX messages. It supports message
    checksum validation and proper message framing.
    """
    name: str
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
    def activate(cls, *names: str) -> None:
        """Activate the UBX message with the given name.

        Args:
            name: The name of the UBX message to activate.

        Raises:
            ValueError: If the message name is not supported.
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

class UBXParser(Parser):
    """Stateful parser for streaming UBX data.

    This class extends a generic Parser and implements a state machine to parse incoming
    bytes from a data stream into complete UBX sentences. It handles validation, buffering,
    and extraction of structured message data from valid sentences.
    """
    def __init__(self, callback: Callable[[UBX], None] | None = None) -> None:
        """Initialize the UBXParser instance.

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
    def find(self, data: bytes) -> tuple[bytes | None, int]:
        """Find the first UBX message in the given data.

        Args:
            data: The data to search for a UBX message.

        Returns:
            A tuple containing the first UBX message found in the data and the position of
            the message in the data, or both None if no message is found.
        """
