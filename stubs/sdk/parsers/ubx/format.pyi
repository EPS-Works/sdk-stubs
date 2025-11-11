from typing import Callable

class Format:
    """Format specifiers for binary data packing and unpacking.

    This class provides format specifiers for various data types used in UBX messages,
    including integers, floats, strings, and padding bytes.
    """
    U1: str
    I1: str
    X1: str
    U2: str
    I2: str
    X2: str
    U4: str
    I4: str
    X4: str
    U8: str
    I8: str
    R4: str
    R8: str
    CH: Callable[[int], str]
    PAD: Callable[[int], str]
    ADAPTIVE: str
