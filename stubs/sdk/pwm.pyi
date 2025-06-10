from .dio import DigitalIO as DigitalIO
from typing import Any

class PWM:
    """Software PWM controller for digital output pins.

    This class implements PWM functionality by toggling a DigitalIO pin at a specified
    frequency and duty cycle using software timers. It provides precise timing control
    and automatic resource management for PWM operations.

    The class supports frequency and duty cycle adjustments during operation, with
    automatic timer recalculation to maintain signal accuracy.

    Attributes:
        MIN_FREQUENCY: Minimum supported PWM frequency in Hz.
        MAX_FREQUENCY: Maximum supported PWM frequency in Hz.
    """
    MIN_FREQUENCY: int
    MAX_FREQUENCY: int
    def __init__(self, dio: DigitalIO) -> None:
        """Initialize a new PWM controller.

        This method sets up the PWM controller for a given digital output pin.
        It validates the pin configuration and prepares the controller for
        PWM operations.

        Args:
            dio: The DigitalIO pin to generate the PWM signal on.

        Raises:
            TypeError: If the pin is not an instance of DigitalIO.
            ValueError: If the pin is not configured as an output.
        """
    def __getattr__(self, name: str) -> Any:
        """Delegate unknown attributes to the underlying DigitalIO instance."""
    @property
    def is_running(self) -> bool:
        """Check if the PWM signal is currently active.

        Returns:
            True if the PWM signal is being generated, False otherwise.
        """
    @property
    def frequency(self) -> int:
        """Get the current PWM frequency.

        Returns:
            Frequency in Hertz (Hz).
        """
    @property
    def duty_cycle(self) -> int:
        """Get the current PWM duty cycle.

        Returns:
            Duty cycle percentage (0-100).
        """
    def start_pwm(self, frequency: int, duty_cycle: int) -> None:
        """Start generating a PWM signal.

        This method begins generating a PWM signal with the specified frequency
        and duty cycle. It creates and configures the necessary timer for
        accurate signal generation.

        Args:
            frequency: The frequency of the PWM signal in Hz.
            duty_cycle: The duty cycle of the PWM signal as a percentage (0-100).

        Raises:
            ValueError: If the frequency is outside the supported range or if
                the duty cycle is not between 0 and 100.
        """
    def stop_pwm(self) -> None:
        """Stop the PWM signal generation.

        This method halts the PWM signal and releases any resources used by
        the timer. The output pin is set to a low state when stopped.
        """
