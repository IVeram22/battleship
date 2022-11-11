from enum import Enum


class CellType(Enum):
    LIVE = '#'
    KILLED = 'X'
    MISS = '0'
    UNKNOWN = '-'
