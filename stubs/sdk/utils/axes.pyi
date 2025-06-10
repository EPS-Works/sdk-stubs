from _typeshed import Incomplete
from typing import NamedTuple

Direction: Incomplete

class Axes(NamedTuple):
    x: Incomplete
    y: Incomplete
    z: Incomplete
Vector = tuple[float, ...]
Matrix = tuple[Vector, ...]

class ReferenceFrame:
    """Represents a right-handed 3D frame using directional axes over a NED reference frame."""
    FRAME: dict[Direction, Vector]
    def __init__(self, base: Axes, mount: Axes) -> None:
        """Initializes the basis frame with a specific orientation over a NED reference frame.

        Args:
            base: Directional axes tuple the of the base orientation.
            mount: Directional axes tuple of the mounting orientation.

        Raises:
            ValueError: If the provided axes do not form a valid right-handed system.
        """
    def rotation_matrix(self, axes: Axes) -> Matrix:
        """Returns the rotation matrix of the reference frame transformed by the given axes.

        Args:
            axes: Directional axes tuple.

        Returns:
            A 3x3 rotation matrix corresponding to the rotated mounting frame.
        """
    def axes(self, rotation: Axes) -> Axes:
        """Transforms the given axes into the frame's reference orientation.

        Args:
            rotation: Directional axes tuple to be transformed.

        Returns:
            A new Axes instance representing the input axes in the frame's
            reference orientation.

        Raises:
            ValueError: If the transformed vector does not match any basis vector.
        """
    def remapping_vectors(self, rotation: Axes) -> tuple[tuple[int, ...], tuple[int, ...]]:
        """Get the remapping vectors for the given axes over the frame's reference orientation.

        Args:
            rotation: Directional axes tuple to be remapped.

        Returns:
            A tuple of two vectors, the first containing the order of the axes and
            the second containing the sign of each axis in the remapped coordinate system.
        """
