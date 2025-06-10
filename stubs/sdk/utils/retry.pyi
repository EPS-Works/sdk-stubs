from typing import Callable

ErrorHandler = Callable[[Exception, int], None]

def retry(delay: int = 0, attempts: int | None = None, on_error: ErrorHandler | None = None) -> Callable:
    """Create a retry decorator for function calls.

    This decorator wraps a function to automatically retry it when it fails.
    It supports configurable delays between attempts, maximum attempt limits,
    and custom error handling through a callback function. The retry mechanism
    will continue until either success or the maximum attempt limit is reached.

    Args:
        delay: Milliseconds to wait between retry attempts (default: 0).
        attempts: Optional maximum number of retry attempts before failing.
            If None, retries indefinitely until success.
        on_error: Optional callback function to handle errors during retries.
            The callback receives the exception and current attempt count.

    Returns:
        A decorator that adds retry logic to the target function. The decorated
        function will be retried on any exception until either success or the
        attempt limit is reached.

    Raises:
        ValueError: If delay is negative or attempts is non-positive.
    """
