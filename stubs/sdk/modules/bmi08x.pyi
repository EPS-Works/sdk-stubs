from machine import I2C as I2C
from sdk.utils.axes import Axes as Axes, Direction as Direction, ReferenceFrame as ReferenceFrame
from typing import Callable

BMI08xSensor = tuple[int, tuple[int, int], tuple[int, int]]

class BMI08x:
    """Interface for interacting with the BMI08x IMU sensors.

    The BMI08x class provides methods for accessing accelerometer, gyroscope, and
    temperature data, managing sensor configuration, and handling device activation
    and reset procedures.

    This class abstracts low-level I2C communication with the BMI08x sensor family,
    including register configuration, data reading, and unit conversion according
    to the sensor datasheet.
    """
    ACCELEROMETER: Callable[[int, str], BMI08xSensor]
    GYROSCOPE: Callable[[int, int], BMI08xSensor]
    def __init__(self, i2c: I2C, mount: Axes | None = None) -> None:
        """Initialize the BMI08x IMU sensor.

        Args:
            i2c: I2C interface for communication with the sensor.

        The sensor is initialized with default settings for the accelerometer and
        gyroscope. The accelerometer is configured for 3G range and the gyroscope
        is configured for 125dps range. The sensor is not enabled by default and
        must be activated with the :meth:`activate` method.
        """
    @property
    def acceleration(self) -> list[float]:
        """Get the current acceleration data.

        Reads accelerometer data from the BMI088 sensor (datasheet section 5.3.4).

        Returns:
            A list of [x, y, z] acceleration values in G units.
        """
    @property
    def angular_velocity(self) -> list[float]:
        """Get the current angular velocity data.

        Reads gyroscope data from the BMI088 sensor (datasheet section 5.5.2).

        Returns:
            A list of [x, y, z] angular velocity values in rad/s.
        """
    @property
    def temperature(self) -> float | None:
        """Get the current temperature of the sensor.

        Reads temperature data from the BMI088 sensor (datasheet section 5.3.7).

        Returns:
            The current temperature in degrees Celsius.
        """
    def reset(self) -> None:
        """Reset the sensor."""
    def activate(self, sensor: BMI08xSensor) -> None:
        """Activate the specified sensor.

        This method sets the configuration for the sensor specified and enables the
        sensor. The sensor must be activated before data can be retrieved.

        Args:
            sensor: A BMI08xSensor containing the configuration for the
                sensor to activate.
        """
    def set_frame(self, x: Direction, y: Direction, z: Direction) -> None:
        """Set a new reference frame for the BMI08x sensor

        Args:
            x: The x-axis direction.
            y: The y-axis direction.
            z: The z-axis direction.

        Raises:
            ValueError: If the provided axes are not valid or do not form a
                        valid right-handed system.
        """
