from .dio import DigitalIO as DigitalIO

class Led(DigitalIO):
    """Controls an LED connected to a digital output pin.

    This class extends DigitalIO to provide LED-specific functionality like blinking
    and pattern generation. It ensures safe pin configuration and prevents mode changes
    that could damage the LED or circuit.
    """
    def __init__(self, pin: str, inverted: bool = False) -> None:
        """Initialize an LED controller.

        Args:
            pin: The Pin ID.
            inverted: Whether to invert the LED logic (default: False).
        """
    @DigitalIO.mode.setter
    def mode(self, _mode) -> None:
        """Prevent mode changes to protect the LED circuit.

        Raises:
            AttributeError: Always raised to prevent mode changes.
        """
    def on(self) -> bool:
        """Turn the LED on.

        Returns:
            True, indicating the LED is on.
        """
    def off(self) -> bool:
        """Turn the LED off.

        Returns:
            False, indicating the LED is off.
        """
    def toggle(self) -> bool:
        """Toggle the LED state between on and off.

        Returns:
            True if the LED is now on, False if off.
        """
    def blink(self, period: int = 1000, times: int | None = None, block: bool = False) -> None:
        """Blink the LED with specified timing parameters.

        This method can operate in blocking or non-blocking mode.

        Args:
            period: Blink period in milliseconds (default: 1000).
            times: Number of blinks, or None for continuous blinking (default: None).
            block: Whether to block execution during blinking (default: False).

        Raises:
            ValueError: If period is less than 1ms.
        """
    def halt(self) -> None:
        """Stop any ongoing blinking pattern.

        This method safely deinitializes the timer and ensures the LED is turned off.
        """
