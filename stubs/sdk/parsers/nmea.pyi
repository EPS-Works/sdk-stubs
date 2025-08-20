from ..utils.enum import Enum as Enum
from .parser import Parser as Parser
from _typeshed import Incomplete
from typing import Any, Callable, NamedTuple

class Talker(Enum):
    """GNSS talker"""
    GPS: str
    GLONASS: str
    GALILEO: str
    BEIDOU: str
    QZSS: str
    ALL: str
    NAVIC: str

class DataValidity(Enum):
    """Data validity"""
    VALID: str
    INVALID: str

class FixType(Enum):
    """Fix of GNSS"""
    NOT_VALID: int
    GPS_FIX: int
    DIFFERENTIAL_GPS_FIX: int
    PPS: int
    RTK_FIX: int
    RTK_FLOAT: int
    ESTIMATED: int
    MANUAL: int
    SIMULATION: int

class OperationMode(Enum):
    """Operation mode"""
    MANUAL: str
    AUTOMATIC: str

class NavigationMode(Enum):
    """Navigation mode"""
    NOT_AVAILABLE: int
    FIX_2D: int
    FIX_3D: int

class PositionMode(Enum):
    """Position mode"""
    AUTONOMOUS: str
    DIFFERENTIAL: str
    ESTIMATED: str
    MANUAL: str
    SIMULATION: str
    INVALID: str

def coordinate(value: str) -> float:
    """Convert NMEA coordinate string to decimal degrees.

    Args:
        value: Coordinate string in DDMM.MMMM format.

    Returns:
        Coordinate in decimal degrees (-180.0 to 180.0 for longitude,
        -90.0 to 90.0 for latitude).
    """
def time(value: str) -> tuple[int, int, float]:
    """Convert NMEA time string to time components.

    This function converts time from the NMEA HHMMSS.SS format to a tuple of
    hour, minute, and second components.

    Args:
        value: Time string in HHMMSS.SS format.

    Returns:
        Tuple of (hour, minute, second) where hour and minute are integers
        and second is a float.
    """

class Satellite(NamedTuple):
    prn: Incomplete
    elevation: Incomplete
    azimuth: Incomplete
    snr: Incomplete

class Field(NamedTuple):
    name: Incomplete
    type: Incomplete
    parse: Incomplete

MESSAGES: dict[str, tuple[tuple[tuple[str, type, Callable | None], ...], Callable[[list[str]], dict[str, Any]] | None]]

class NMEA:
    """NMEA message.

    This class provides high-level methods to validate, parse and handle NMEA messages.
    It supports both standard and custom NMEA message types.
    """
    msg_id: str
    talker: Talker
    def __init__(self, msg_id: str, talker: str, **kwargs) -> None:
        '''Initialize an NMEA message.

        Args:
            msg_id: Message identifier (e.g., "GGA" for position data).
            talker: GNSS system identifier (e.g., "GP" for GPS).
            **kwargs: Message-specific field values.

        Raises:
            ValueError: If the message name is not supported.
            TypeError: If a field value does not match the expected type.
        '''
    @classmethod
    def checksum(cls, data: bytes) -> int:
        """Calculate the NMEA checksum for the given data.

        Args:
            data: The byte sequence over which to calculate the checksum.

        Returns:
            An string representing the XOR hex checksum of the provided data.
        """
    @classmethod
    def validate(cls, data: bytes, name: str | None = None) -> None:
        """Validate a raw NMEA message.

        Args:
            data: A raw NMEA message as bytes.
            name: The expected NMEA message type.

        Raises:
            AssertionError: If the message is invalid.
        """
    @classmethod
    def is_valid(cls, data: bytes, msg: str | None = None) -> bool:
        """Check if data is a valid NMEA message.

        Args:
            data: A raw NMEA message as bytes.
            msg: The expected NMEA message type.

        Returns:
            True if the message is valid, False otherwise.
        """
    @classmethod
    def parse(cls, data: bytes) -> NMEA:
        """Parse a raw NMEA message into a structured object.

        Args:
            data: A raw NMEA message as bytes.
            validate: Whether to validate the message before parsing.

        Returns:
            A structured NMEA object.
        """
    @classmethod
    def register(cls, msg_id: str, fields: list[Field], parser: Callable[[str], dict[str, Any]] | None = None) -> None:
        '''Register a new NMEA message type.

        This function allows adding support for custom NMEA message types by
        registering their field definitions and optional custom parser.

        Args:
            name: The message identifier (e.g., "GGA").
            fields: List of Field namedtuples defining the message structure.
            parser: Optional custom parser function for complex message types.

        Raises:
            ValueError: If a message with the same name is already registered.
        '''

class NMEAParser(Parser):
    """Stateful parser for streaming NMEA data.

    This class extends a generic Parser and implements a state machine to parse incoming
    bytes from a data stream into complete NMEA sentences. It handles validation, buffering,
    and extraction of structured message data from valid sentences.
    """
    def __init__(self) -> None: ...
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
