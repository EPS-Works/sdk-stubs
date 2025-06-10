class Ethernet:
    """Manages Ethernet network connections and configuration.

    This class provides a simplified interface for configuring and monitoring
    Ethernet connections, with support for static and dynamic IP addressing.
    """
    def __init__(self, phy_type: int | None = None) -> None:
        """Initialize an Ethernet connection manager.

        Args:
            phy_type: The type of PHY to use for the Ethernet connection.
        """
    @property
    def ip(self) -> str:
        '''Get the current IP address.

        Returns:
            The IP address in string format (e.g., "192.168.1.100").
        '''
    @property
    def gateway(self) -> str:
        """Get the gateway IP address.

        Returns:
            The gateway IP address in string format.
        """
    @property
    def is_connected(self) -> bool:
        """Check if the Ethernet connection is active.

        Returns:
            True if connected, False otherwise.
        """
    def connect(self, ip: str | None = None, gateway: str | None = None, subnet: str = '255.255.255.0', dns: str = '1.1.1.1') -> None:
        '''Configure and establish an Ethernet connection.

        This method supports both static IP configuration and DHCP. If IP is provided,
        a static configuration is used; otherwise, DHCP is enabled.

        Args:
            ip: Optional static IP address. If None, DHCP is used.
            gateway: Optional gateway IP address.
            subnet: Subnet mask (default: "255.255.255.0").
            dns: DNS server IP address (default: "1.1.1.1").
        '''
    def disconnect(self) -> None:
        """Disable the Ethernet interface.

        This method deactivates the Ethernet connection and releases any
        allocated network resources.
        """
