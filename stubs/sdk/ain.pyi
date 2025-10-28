class AnalogIn:
    """Provides an interface for reading analog values and voltages from pins.

    This class implements noise reduction through multiple sampling and provides
    both raw ADC values and voltage readings. It supports voltage divider
    configurations for accurate voltage measurements.

    Attributes:
        SAMPLE_SIZE: Number of samples to take for noise reduction (default: 500).
    """
    SAMPLE_SIZE: int
    def __init__(self, pin: str, voltage_divider: float) -> None:
        """Initialize the AnalogIn instance.

        Args:
            pin: The pin ID to read analog input from.
            voltage_divider: The voltage divider ratio for voltage calculations.
        """
    @property
    def value(self) -> float:
        """Get the filtered analog value.

        Reads multiple samples from the ADC and returns the median value to
        reduce noise by averaging out transient fluctuations.

        Returns:
            The median value from the sampled analog readings (0-65535).
        """
    @property
    def voltage(self) -> float:
        """Get the voltage of the analog input.

        Calculates the actual voltage using the raw ADC value and the configured
        voltage divider ratio.

        Returns:
            The voltage in volts.
        """

class DifferentialAnalogIn:
    """Provides differential measurements between two analog inputs.

    This class calculates the difference between a target and reference analog input,
    useful for applications requiring relative measurements or noise cancellation.
    """
    def __init__(self, target: AnalogIn, ref: AnalogIn) -> None:
        """Initialize the differential analog input.

        Args:
            target: The target analog input to measure.
            ref: The reference analog input to subtract.
        """
    @property
    def value(self) -> float:
        """Get the differential raw value.

        Returns:
            The difference between target and reference raw values.
        """
    @property
    def voltage(self) -> float:
        """Get the differential voltage.

        Returns:
            The voltage difference between target and reference in volts.
        """
