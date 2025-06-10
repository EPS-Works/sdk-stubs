from .dio import DigitalIO as DigitalIO
from machine import I2C as I2C

class UsbHub:
    """USB hub controller with power and reset management.

    This class provides a high-level interface for controlling a USB hub, including
    power management, reset operations, and hub configuration through I2C communication.
    It supports enabling USB ports and configuring hub parameters for proper device
    operation.
    """
    ADDRESS: int
    def __init__(self, i2c: I2C, power: DigitalIO, reset: DigitalIO) -> None:
        """Initialize the USB hub controller.

        Args:
            i2c: I2C interface for hub communication.
            power: Pin ID for power control.
            reset: Pin ID for reset control.
        """
    def on(self) -> None:
        """Power on the USB hub.

        This method sets the power pin high to enable power to the USB hub
        and its connected devices.
        """
    def off(self) -> None:
        """Power off the USB hub.

        This method sets the power pin low to disable power to the USB hub
        and its connected devices.
        """
    def reset(self) -> None:
        """Reset the USB hub.

        This method performs a hardware reset of the USB hub by toggling the
        reset pin. It includes appropriate delays to ensure proper reset timing.
        """
    def enable(self, config: list[list[int]], ports: list[int], attach: list[int]) -> None:
        """Enable and configure the USB hub.

        The configuration data includes hub parameters, port settings, and
        device attachment configuration.
        """
