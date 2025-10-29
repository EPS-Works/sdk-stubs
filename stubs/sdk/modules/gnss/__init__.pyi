from .gnss import GNSS as GNSS
from .ublox import Ublox as Ublox
from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['GNSS', 'Ublox', 'GNSS_MODULES']

class GNSSModules(NamedTuple):
    ZED_F9P: Incomplete
    UM98x: Incomplete

GNSS_MODULES: Incomplete
