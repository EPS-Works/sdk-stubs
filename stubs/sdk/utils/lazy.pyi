from typing import Callable

class LazyFactory:
    """Factory for lazy instantiation"""
    def __init__(self, name: str) -> None: ...
    def register(self, factories: dict[str, Callable]):
        """Update the factory map after setup"""
    def __getattr__(self, name: str):
        """Lazy instantiation of hardware components"""
    def get(self, name: str, default=None):
        """Get an item with optional default"""
    def __contains__(self, name: str) -> bool:
        """Check if an item exists in the factory"""
    def __dir__(self):
        """Return list of available attributes for dir() and help()"""
