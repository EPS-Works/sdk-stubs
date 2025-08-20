from .serial import Serial as Serial
from .stream import Stream as Stream
from typing import Callable

class Forwarder:
    """Manages data forwarding between serial interfaces.

    This class provides a flexible mechanism for forwarding data from a source serial
    interface to one or more target interfaces, with optional throttling control.
    """
    def __init__(self, source: Serial, throttle: int | None = None) -> None:
        """Initialize a data forwarder.

        Args:
            source: The source Serial interface to read data from.
            throttle: Optional throttle value in milliseconds to control data flow rate.
        """
    def to(self, target: Serial | Callable[[bytes], None]) -> None:
        """Add a target for data forwarding.

        Args:
            target: The Serial interface to forward data to or a callback function
            that accepts bytes as input.
        """
    async def start(self) -> None:
        """Start the data forwarding process.

        This method creates a stream from the source and forwards all received
        data to all registered targets. The process continues until the stream
        is closed or an error occurs.
        """
