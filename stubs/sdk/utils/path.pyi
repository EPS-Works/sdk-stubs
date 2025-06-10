class Path:
    """Path manipulation utilities for uPython environments.

    This class provides static methods for common path operations, including path
    joining, directory creation, and path component extraction. It is designed to
    work in uPython environments where os.path functionality is not available.

    The class implements a subset of path manipulation functions commonly found in
    standard library implementations, optimized for memory usage and simplicity.
    """
    @staticmethod
    def join(base: str, *args: str) -> str:
        """Join path components into a normalized path.

        This method combines multiple path components into a single path string,
        ensuring consistent forward slash usage and proper handling of separators.

        Args:
            base: The base path component.
            *args: Additional path components to join.

        Returns:
            A normalized path string with single forward slashes.
        """
    @staticmethod
    def makedirs(path: str) -> None:
        """Create directories recursively.

        This method creates all necessary directories in the given path. It silently
        skips existing directories and handles path normalization automatically.

        Args:
            path: The directory path to create.

        Raises:
            OSError: If directory creation fails for reasons other than the directory
                already existing.
        """
    @staticmethod
    def dirname(path: str) -> str:
        '''Extract the directory component from a path.

        This method returns the directory portion of a path, handling special
        cases for root directories and paths without directory components.

        Args:
            path: The input path to process.

        Returns:
            The directory component of the path. Returns "/" for root paths,
            "" for paths without directories, or the directory path otherwise.
        '''
    @staticmethod
    def exists(path: str) -> bool:
        """Check if a file exists.

        Args:
            path: The file path to check.

        Returns:
            True if the file exists, False otherwise.
        """
