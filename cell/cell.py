from cell.methods import CellMethods
from cell.type import CellType
from coordinates.coordinates import Coordinates


class Cell(CellMethods):
    def type(self):
        return self.__type

    def get_value(self):
        return self.__type.value

    def set_value(self, cell_type: CellType):
        self.__type = self.__set_cell_type(cell_type)

    def get_coordinates(self):
        return self.__coordinates

    def __init__(self, coordinates: Coordinates, cell_type: CellType = CellType.UNKNOWN):
        self.__type = self.__set_cell_type(cell_type)
        self.__coordinates = coordinates

    @classmethod
    def __set_cell_type(cls, cell_type):
        if type(cell_type) != CellType:
            raise TypeError('Works only with objects of CellType')
        return cell_type
