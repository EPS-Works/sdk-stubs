from typing import Awaitable, Callable, TypeVar

R = TypeVar('R')
ErrorHandler = Callable[[Exception, int], None]

def retry(delay: int = 0, attempts: int = ..., on_error: ErrorHandler | None = None) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """Create a retry decorator for function calls.

    This decorator wraps a function to automatically retry it when it fails.
    It supports configurable delays between attempts, maximum attempt limits,
    and custom error handling through a callback function. The retry mechanism
    will continue until either success or the maximum attempt limit is reached.

    Args:
        delay: Milliseconds to wait between retry attempts (default: 0).
        attempts: Maximum number of retry attempts before failing (default: 1000).
        on_error: Optional callback function to handle errors during retries.
            The callback receives the exception and current attempt count.

    Returns:
        A decorator that adds retry logic to the target function. The decorated
        function will be retried on any exception until either success or the
        attempt limit is reached.

    Raises:
        ValueError: If delay is negative or attempts is non-positive.
    """
def aretry(delay: int = 0, attempts: int = ..., on_error: ErrorHandler | None = None) -> Callable[[Callable[..., Awaitable[R]]], Callable[..., Awaitable[R]]]:
    """Create a retry decorator for async function calls.

    This decorator wraps an async function to automatically retry it when it fails.
    It supports configurable delays between attempts, maximum attempt limits,
    and custom error handling through a callback function. The retry mechanism
    will continue until either success or the maximum attempt limit is reached.

    Args:
        delay: Milliseconds to wait between retry attempts (default: 0).
        attempts: Maximum number of retry attempts before failing (default: 1000).
        on_error: Optional callback function to handle errors during retries.
            The callback receives the exception and current attempt count.

    Returns:
        A decorator that adds retry logic to the target async function. The decorated
        function will be retried on any exception until either success or the
        attempt limit is reached.

    Raises:
        ValueError: If delay is negative or attempts is non-positive.
    """
