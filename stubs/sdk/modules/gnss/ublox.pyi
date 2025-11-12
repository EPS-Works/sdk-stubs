from ...parsers.ubx import Format as Format, Parser as Parser, UBX as UBX
from ...stream import Stream as Stream
from ...utils import retry as retry
from .gnss import GNSS as GNSS
from typing import Any, Callable

class Ublox(GNSS):
    """Controller for Ublox ZED-F9P GNSS receivers.

    This class extends the base GNSS interface to provide high-level configuration
    of UBX protocol messages and streaming behavior. It handles enabling and disabling
    message outputs on specified ports using UBX-CFG-VALSET commands.
    """
    baudrate: int
    def autobaud(self, timeout: int | None = 100) -> None:
        """Auto-detect the baudrate of the connected GNSS receiver.

        This method attempts to detect the correct baudrate by sending a test message
        and checking for acknowledgment across common baudrates.

        Args:
            timeout: The maximum time to wait for the ACK response in milliseconds.

        Returns:
            The detected baudrate, or None if no baudrate was detected.
        """
    def load_config(self, path: str) -> None:
        """Load and apply a configuration file to the GNSS receiver.

        The configuration file is a text file containing some UBX-CFG-VALGET messages in hex format.
        Usable configurations are transformed to UBX-CFG-VALSET and applied.

        If a configuration changes the baudrate, subsequent messages will fail and
        the process will be retried once (no more than one baudrate setting is allowed).

        Args:
            path: The path to the configuration file to load.

        Raises:
            OSError: If a command cannot be applied to the receiver.
        """
    def config(self, data: list[tuple[int, tuple[int, str]]], layer: int = 1, timeout: int | None = None) -> None:
        """Configure the GNSS receiver using UBX-CFG-VALSET messages.

        This method sends configuration data to the receiver and waits for acknowledgment.

        Args:
            data: List of tuples containing (Key ID, value) pairs to configure.
            layer: The configuration layer to modify (default: RAM).
            timeout: Maximum time to wait for acknowledgment in milliseconds.

        Raises:
            OSError: If the configuration cannot be applied or acknowledgment is not received.
        """
    def stream(self, messages, port, frequency: int | None = 1, timeout: int | None = None) -> Callable[[Any], None]: ...
    def halt(self, messages, port) -> None: ...
