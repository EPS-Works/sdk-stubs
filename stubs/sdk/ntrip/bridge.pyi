from ..parsers.nmea import Parser as Parser
from ..serial import SerialBufferCursor as SerialBufferCursor
from ..stream import Stream as Stream
from .client import NTRIPClient as NTRIPClient

class NTRIPBridge:
    """Manages bidirectional data flow between GNSS receiver and NTRIP caster.

    This class bridges NMEA messages from a GNSS receiver to an NTRIP caster and
    forwards RTCM corrections back to the receiver. It supports asynchronous
    operation with configurable message throttling.
    """
    def __init__(self, client: NTRIPClient) -> None:
        """Initialize the NTRIP bridge.

        Args:
            client: Configured NTRIP client instance for caster communication.
        """
    async def run(self, cursor: SerialBufferCursor, throttle: int = 100) -> None:
        """Start the bidirectional data bridge.

        This method continuously forwards NMEA messages to the NTRIP caster and
        sends received RTCM corrections back to the GNSS receiver.

        Args:
            cursor: Serial buffer cursor for GNSS receiver communication.
            throttle: Message processing delay in milliseconds (default: 100).
        """
