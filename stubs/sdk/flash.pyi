from .storage import Storage as Storage, to_best_size as to_best_size
from _typeshed import Incomplete
from typing import NamedTuple

class FS(NamedTuple):
    FAT: Incomplete
    LFS: Incomplete

FileSystem: Incomplete

class FS(NamedTuple):
    FAT: Incomplete

class FlashDrive(Storage):
    """Manages flash storage devices with partitioning capabilities.

    This class extends the Storage base class to provide advanced flash storage
    operations including partition management, formatting, and mounting. It supports
    both FAT and LittleFS filesystems where available.
    """
    def format(self) -> bool:
        """Format the flash storage as a single FAT filesystem.

        Removes all existing partitions and creates a fresh filesystem. This operation
        will erase all data on the device.

        Returns:
            True if formatting was successful, False otherwise.
        """
    def mount(self) -> tuple[Storage, ...]:
        """Mount all partitions on the flash storage device.

        Reads the partition table and mounts each partition at its designated
        mount point.

        Returns:
            Tuple of Storage objects representing mounted partitions, excluding
            the base partition.
        """
    def partition(self, name: str, size: int, fs: FS = ...) -> Storage | None:
        """Create a new partition on the flash storage.

        Creates a partition with the specified name and size, formatting it with
        the requested filesystem type. The partition is created at the end of the
        available space.

        Args:
            name: Name for the new partition.
            size: Size of the partition in bytes.
            fs: Filesystem type to use (defaults to FAT).

        Returns:
            Storage object for the new partition if successful, None otherwise.

        Raises:
            ValueError: If name is invalid or there is insufficient space.
        """
