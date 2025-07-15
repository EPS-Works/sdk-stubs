from machine import I2C as I2C
from sdk.utils.axes import Axes as Axes, Direction as Direction, ReferenceFrame as ReferenceFrame

BNO08xSensor = tuple[int, int, int]
Vector3 = tuple[float, float, float]
Quaternion = tuple[float, float, float, float]

class BNO08x:
    """Interface for interacting with the BNO080 IMU.

    The BNO08x class provides methods for accessing various sensor readings asynchronously, updating
    data at specified intervals, and managing device reset and configuration.

    This class handles the low-level communication with the BNO08x sensor over I2C,
    including packet formatting, error handling, and data conversion.
    """
    PERIOD: int
    TIMEOUT: int
    ACCELEROMETER: BNO08xSensor
    GYROSCOPE: BNO08xSensor
    MAGNETOMETER: BNO08xSensor
    ROTATION: BNO08xSensor
    STABILIZED_ROTATION: BNO08xSensor
    def __init__(self, i2c: I2C, address: int = 74, reset: int | str | None = None, mount: Axes | None = None) -> None:
        '''Initializes the BNO08x class.

        Args:
            i2c: The I2C interface to use for communication.
            address: The I2C address of the BNO08x sensor (default: 0x4A).
            reset: Optional pin ID for hardware reset control.
            mount: The mounting frame of the BNO08x sensor on the board over
                   a NED reference frame (default: Axes(x="E", y="N", z="U")).
        '''
    @property
    def acceleration(self) -> Vector3 | None:
        """Get the current acceleration data.

        Returns:
            A tuple of (x, y, z) acceleration values in m/s², or None if data
            is not available or the sensor is not activated.
        """
    @property
    def angular_velocity(self) -> Vector3 | None:
        """Get the current angular velocity data.

        Returns:
            A tuple of (x, y, z) angular velocity values in rad/s, or None if data
            is not available or the sensor is not activated.
        """
    @property
    def magnetic_field(self) -> Vector3 | None:
        """Get the current magnetic field data.

        Returns:
            A tuple of (x, y, z) magnetic field values in microtesla (µT), or None if data
            is not available or the sensor is not activated.
        """
    @property
    def rotation(self) -> Quaternion | None:
        """Get the current rotation data.

        Returns:
            A tuple of (w, x, y, z) quaternion values representing the rotation, or None if data
            is not available or the sensor is not activated.
        """
    @property
    def stabilized_rotation(self) -> Quaternion | None:
        """Get the current stabilized rotation quaternion data.

        Returns:
            A tuple of (w, x, y, z) quaternion values representing the stabilized rotation,
            or None if data is not available or the sensor is not activated.
        """
    @property
    def attitude(self) -> tuple[float | None, float | None, float | None]:
        """Get the current attitude data.

        This property calculates roll, pitch, and yaw angles from the stabilized rotation
        quaternion or the rotation quaternion if the stabilized rotation is not available.

        Returns:
            An Attitude with roll, pitch, and yaw angles in degrees, or all None if data
            is not available or the sensor is not activated.
        """
    def reset(self) -> None:
        """Reset the BNO08x sensor.

        This method performs a hardware reset of the BNO08x sensor if a reset pin
        is configured, or a software reset otherwise. It reinitializes the sensor
        after the reset.
        """
    def set_frame(self, x: Direction, y: Direction, z: Direction) -> None:
        """Set a new reference frame for the BNO08x sensor

        Args:
            x: The x-axis direction.
            y: The y-axis direction.
            z: The z-axis direction.

        Raises:
            ValueError: If the provided axes are not valid or do not form a
                        valid right-handed system.
        """
    def activate(self, sensor: BNO08xSensor, interval: int = 100000) -> None:
        """Activate a specific sensor with the given update interval.

        This method enables data collection for the specified sensor type at the
        given interval.

        Args:
            sensor: The BNO08xSensor to activate.
            interval: The update interval in nanoseconds (default: 100_000).
        """
    def update(self) -> None:
        """Update the sensor data.

        Polls the BNO080 for incoming sensor data, processing any available packets.
        The update function will continue reading packets until either data is received
        or a timeout occurs. The timeout duration is specified by the TIMEOUT constant.

        Raises:
            OSError: If no data is received within the specified timeout period.
        """
