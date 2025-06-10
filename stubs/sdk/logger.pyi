from .utils.path import Path as Path
from _typeshed import Incomplete
from logging import Formatter, Logger, StreamHandler

LogLevel: Incomplete

class ElapsedTimeFormatter(Formatter):
    """Formats log messages with elapsed time since program start.

    This formatter extends the standard logging Formatter to include precise
    elapsed time measurements in seconds and milliseconds.
    """
    def __init__(self, fmt: str) -> None:
        """Initialize the elapsed time formatter.

        Args:
            fmt: The format string for log messages.
        """
    def formatTime(self, *_):
        """Format the current time as elapsed seconds since program start.

        Returns:
            Elapsed time in seconds with millisecond precision.
        """

logger: Logger
console: StreamHandler

def use_log_file(filename: str = 'log.log', level=..., formatter: Formatter | None = None) -> None:
    '''Configure file-based logging.

    This function sets up logging to a file with the specified parameters.
    It ensures the log directory exists and adds a file handler to the logger.

    Args:
        filename: Path to the log file (default: "log.log").
        level: Minimum log level for file output (default: INFO).
        formatter: Custom formatter for file output (default: None, uses FORMATTER).
    '''
