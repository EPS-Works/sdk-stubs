from sdk.modules.gnss import GNSS as GNSS
from sdk.parsers.nmea import MESSAGES as MESSAGES
from typing import Callable

class Unicore(GNSS):
    """Controller for Unicore GNSS receivers.

    This class extends the base GNSS interface to provide a high-level configuration.
    It handles enabling and disabling message outputs on specified ports.
    """
    def stream(self, messages: list[str], port: int | str, frequency: int | None = None) -> Callable[[], None]: ...
    def halt(self, messages: list[str], port: int | str) -> None: ...
