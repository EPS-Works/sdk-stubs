from typing import Any, Callable

class DigitalIO:
    """Provides a robust interface for digital I/O operations with event handling.

    This class wraps Pin to provide safe state transitions and event handling
    capabilities. It prevents incorrect operations (e.g., writing while in input mode)
    and supports multiple event handlers for rising, falling, and change events.

    Attributes:
        IN: Input mode for digital pins.
        OUT: Output mode for digital pins.
        RISING: Trigger for rising edge events.
        FALLING: Trigger for falling edge events.
        CHANGE: Trigger for both rising and falling edge events.
    """
    IN: int
    OUT: int
    RISING: int
    FALLING: int
    CHANGE: int
    def __init__(self, pin: str, mode: int = ..., pull: int | None = None, inverted: bool = False, value: bool = False) -> None:
        """Initialize a digital I/O pin wrapper.

        Args:
            pin: The pin ID.
            mode: The initial pin mode (IN or OUT).
            pull: Optional pull-up or pull-down configuration.
            inverted: Whether to invert the pin logic (default: False).
            value: The initial pin value. Only applicable in OUT mode (default: False).
        """
    @property
    def mode(self) -> int:
        """Get the current pin mode.

        Returns:
            The pin mode (DigitalIO.IN or DigitalIO.OUT).
        """
    @mode.setter
    def mode(self, mode: int) -> None:
        """Set the pin mode.

        Args:
            mode: The mode to set (DigitalIO.IN or DigitalIO.OUT).

        Raises:
            ValueError: If the mode is not IN or OUT.
        """
    @property
    def value(self) -> bool:
        """Get the current pin state.

        Returns:
            True if the pin is high, False if low.
        """
    def set(self, value: bool) -> bool:
        """Set the pin output state.

        Args:
            value: True for high, False for low.

        Returns:
            The value that was set.

        Raises:
            ValueError: If the pin is in input mode.
        """
    def high(self) -> bool:
        """Set the pin to high state.

        Returns:
            True, indicating the high state.

        Raises:
            ValueError: If the pin is in input mode.
        """
    def low(self) -> bool:
        """Set the pin to low state.

        Returns:
            False, indicating the low state.

        Raises:
            ValueError: If the pin is in input mode.
        """
    def toggle(self) -> bool:
        """Toggle the pin state between high and low.

        Returns:
            The new pin state (True for high, False for low).

        Raises:
            ValueError: If the pin is in input mode.
        """
    def attach(self, trigger: int, handler: Callable[[DigitalIO], Any]) -> None:
        """Register an event handler for pin state changes.

        Args:
            trigger: The event type (RISING, FALLING, or CHANGE).
            handler: The function to call when the event occurs.

        Raises:
            ValueError: If the trigger type is invalid.
        """
    def detach(self, trigger: int | None = None, handler: Callable[[DigitalIO], Any] | None = None) -> None:
        """Remove event handlers based on trigger type and/or handler function.

        Args:
            trigger: Optional trigger type to filter handlers to remove.
            handler: Optional specific handler function to remove.

        If both trigger and handler are None, all handlers are removed.

        Raises:
            ValueError: If the trigger type is invalid.
        """
