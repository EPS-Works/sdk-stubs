from typing import Any

class Enum:
    """Base class for defining enumerated types.

    This class provides a lightweight implementation of enumerated types, associating
    symbolic names (keys) with unique values. Instances are initialized with a value
    that is validated against the defined enum members.

    The class supports comparison operations and string representation, making it
    suitable for use in type-safe code and debugging scenarios.
    """
    def __init__(self, value: str | int) -> None:
        """Initialize an Enum instance with a given value.

        This method validates the provided value against the enum members defined
        in the subclass. If the value matches one of the defined enum members,
        the corresponding key is stored. Otherwise, a ValueError is raised.

        Args:
            value: The value to validate and associate with an enum member.

        Raises:
            ValueError: If the provided value does not match any defined enum member.
        """
    @property
    def value(self) -> Any:
        """Get the value of the current enum instance.

        Returns:
            The value associated with the current enum member.
        """
    def __eq__(self, other) -> bool: ...
    def __lg__(self, other) -> bool: ...
