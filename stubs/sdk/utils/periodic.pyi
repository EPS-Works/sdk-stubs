from typing import Awaitable, Callable

def periodic(period: int, duration: int | None = None, times: int | None = None) -> Callable[[Callable[..., None]], Callable[..., Awaitable[None]]]:
    """Create a periodic task decorator.

    This decorator wraps a function to execute it at fixed intervals. It supports
    limiting the total duration or number of executions, and uses adaptive timing
    to maintain accurate intervals.

    Args:
        period: Time interval between executions in milliseconds.
        duration: Optional maximum duration to run in milliseconds.
        times: Optional maximum number of executions.

    Returns:
        A decorator that wraps the target function for periodic execution.

    Raises:
        ValueError: If any argument is negative.
    """
