class TimeoutError(Exception):
    """Exception raised when a timeout occurs."""

class Timeout:
    """
    This class is used to implement a timeout mechanism, allowing to track a time period and detect
    when it has expired. It can be used to add time limits to operations, such as waiting for a
    response or completing a task, and trigger actions when the time limit is reached.
    """
    def __init__(self, timeout: int = 1000) -> None: ...
    @property
    def expired(self) -> bool:
        """Indicates whether the timeout has expired.

        Returns:
            bool: True if the timeout has expired, False otherwise.
        """
    def reset(self, timeout: int | None = None) -> None:
        """Reset the timeout.

        Args:
            timeout: Optional timeout value in milliseconds. If not provided, the
                default timeout value will be used.
        """
    def extend(self, timeout: int) -> None:
        """Extend the timeout by the given amount of milliseconds.

        Args:
            timeout: The additional timeout in milliseconds.
        """
    def __enter__(self) -> Timeout: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
