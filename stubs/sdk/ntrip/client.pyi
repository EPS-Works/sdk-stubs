import types

class ClientConnectionError(OSError):
    """Exception raised when NTRIP caster connection fails."""

class NTRIPClient:
    """Manages connections to NTRIP casters for RTCM data streaming.

    This class provides a robust interface for connecting to NTRIP casters,
    handling authentication, and managing data streaming. It implements
    context manager protocol for safe resource management.
    """
    def __init__(self, host: str, port: int, mountpoint: str, token: str | None = None, user: str | None = None, password: str | None = None) -> None:
        """Initialize an NTRIP client with connection parameters.

        Args:
            host: NTRIP caster hostname.
            port: NTRIP caster port number.
            mountpoint: Target mountpoint name.
            token: Optional bearer token for authentication.
            user: Optional username for basic authentication.
            password: Optional password for basic authentication.

        Raises:
            ClientConnectionError: If initial connection fails.
        """
    def connect(self, token: str | None = None, user: str | None = None, password: str | None = None) -> None:
        """Establish a connection to the NTRIP caster.

        This method supports both bearer token and basic authentication.
        It handles the HTTP request formatting and connection setup.

        Args:
            token: Optional bearer token for authentication.
            user: Optional username for basic authentication.
            password: Optional password for basic authentication.

        Raises:
            ClientConnectionError: If connection fails or authentication is invalid.
            AttributeError: If neither token nor user/password pair is provided.
        """
    def read(self, size: int = 4096) -> bytes:
        """Read data from the NTRIP caster.

        Args:
            size: Number of bytes to read (default: 4096).

        Returns:
            The received data as bytes.

        Raises:
            ClientConnectionError: If not connected to the caster.
        """
    def write(self, data: bytes) -> None:
        """Write data to the NTRIP caster.

        Args:
            data: The data to send as bytes.

        Raises:
            ClientConnectionError: If not connected to the caster.
        """
    def close(self) -> None:
        """Close the connection to the NTRIP caster.

        This method safely closes the socket connection and cleans up resources.
        """
    def __enter__(self) -> NTRIPClient: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
