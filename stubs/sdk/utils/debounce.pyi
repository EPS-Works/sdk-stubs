from typing import Callable

def debounce(delay: int = 100) -> Callable:
    """Create a debounce decorator for function calls.

    This decorator prevents a function from being called more than once within the
    specified delay period. If the function is called again before the delay has
    elapsed, the call is ignored and None is returned.

    Args:
        delay: Minimum time in milliseconds between allowed function calls (default: 100).

    Returns:
        A decorator that wraps the target function with debounce behavior. The decorated
        function will return None if called too frequently.
    """
