from .utils import Path as Path
from _typeshed import Incomplete
from typing import Callable, IO, NamedTuple

class DiskUsage(NamedTuple):
    total: Incomplete
    used: Incomplete
    free: Incomplete

def to_best_size(size_bytes: int, decimals: int = 1) -> str:
    '''Convert a byte size to human-readable format.

    This function converts a size in bytes to the most appropriate unit (B, KB, MB, GB)
    with the specified decimal precision.

    Args:
        size_bytes: Size in bytes to convert.
        decimals: Number of decimal places to show (default: 1).

    Returns:
        Formatted string with size and unit (e.g., "1.5 MB").
    '''

class Storage:
    """Manages file system operations under a specified root directory.

    This class provides a unified interface for file operations, directory management,
    and storage metrics. It ensures proper path handling and directory creation for
    all operations.
    """
    def __init__(self, root: str) -> None:
        """Initialize a storage manager.

        Args:
            root: Base directory path for storage operations.
        """
    @property
    def root(self) -> str:
        """Get the base storage directory path.

        Returns:
            The root directory path.
        """
    @property
    def usage(self) -> DiskUsage:
        """Get storage usage statistics.

        Returns:
            DiskUsage tuple containing (total, used, free) space in bytes.

        Raises:
            OSError: If the storage path is unavailable.
        """
    def list(self, path: str = '') -> list[str]:
        '''List contents of a directory.

        Args:
            path: Relative path within the root directory (default: "").

        Returns:
            List of file and directory names in the specified path.

        Raises:
            OSError: If the directory cannot be listed.
        '''
    def open(self, filename: str, mode: str, encoding: str = 'utf-8') -> IO:
        '''Open a file with the specified mode and encoding.

        This method ensures the file\'s directory exists before opening.

        Args:
            filename: Name of the file to open.
            mode: File open mode (e.g., "r", "w", "a").
            encoding: File encoding (default: "utf-8").

        Returns:
            File object opened with the specified parameters.

        Raises:
            OSError: If the file cannot be opened.
        '''
    def file(self, filename: str, mode: str, encoding: str = 'utf-8') -> Callable:
        '''Create a decorator for file-based operations.

        This decorator manages file opening and closing for the decorated function.
        It ensures proper resource cleanup even if exceptions occur.

        Args:
            filename: Name of the file to operate on.
            mode: File open mode.
            encoding: File encoding (default: "utf-8").

        Returns:
            Decorator function that manages file operations.
        '''
    def exists(self, filename: str) -> bool:
        """Check if a file exists.

        Args:
            filename: Name of the file to check.

        Returns:
            True if the file exists, False otherwise.
        """
    def remove(self, filename: str) -> None:
        """Remove a file.

        Args:
            filename: Name of the file to remove.

        Raises:
            OSError: If the file cannot be removed.
        """
