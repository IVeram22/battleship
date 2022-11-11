from abc import ABC, abstractmethod
from cell.type import CellType


class CellMethods(ABC):
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, cell_type: CellType):
        pass

    @abstractmethod
    def get_coordinates(self):
        pass
