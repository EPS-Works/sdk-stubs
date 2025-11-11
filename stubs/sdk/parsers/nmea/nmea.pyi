from ...utils.lazy import LazyFactory as LazyFactory
from .definitions import DEFINITIONS as DEFINITIONS
from .field import Field as Field
from .models import Talker as Talker
from _typeshed import Incomplete
from typing import Any, Callable

MESSAGES: Incomplete

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
