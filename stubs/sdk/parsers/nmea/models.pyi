from ...utils.enum import Enum as Enum
from _typeshed import Incomplete
from typing import NamedTuple

class Talker(Enum):
    """GNSS talker"""
    GPS: str
    GLONASS: str
    GALILEO: str
    BEIDOU: str
    QZSS: str
    ALL: str
    NAVIC: str

class DataValidity(Enum):
    """Data validity"""
    VALID: str
    INVALID: str

class FixType(Enum):
    """Fix of GNSS"""
    NOT_VALID: int
    GPS_FIX: int
    DIFFERENTIAL_GPS_FIX: int
    PPS: int
    RTK_FIX: int
    RTK_FLOAT: int
    ESTIMATED: int
    MANUAL: int
    SIMULATION: int

class OperationMode(Enum):
    """Operation mode"""
    MANUAL: str
    AUTOMATIC: str

class NavigationMode(Enum):
    """Navigation mode"""
    NOT_AVAILABLE: int
    FIX_2D: int
    FIX_3D: int

class PositionMode(Enum):
    """Position mode"""
    AUTONOMOUS: str
    DIFFERENTIAL: str
    ESTIMATED: str
    MANUAL: str
    SIMULATION: str
    INVALID: str

class Satellite(NamedTuple):
    prn: Incomplete
    elevation: Incomplete
    azimuth: Incomplete
    snr: Incomplete
