import unittest

from cell.cell import Cell
from cell.type import CellType
from coordinates.coordinates import Coordinates


class TestCell(unittest.TestCase):
    def test_create_cell_positive(self):
        coordinates = Coordinates(0, 1)
        cell = Cell(coordinates)
        self.assertTrue(cell.type() == CellType.UNKNOWN)
        self.assertTrue(cell.get_value() == CellType.UNKNOWN.value)
        self.assertTrue(cell.get_coordinates() == coordinates)

    def test_change_cell_positive(self):
        row = 1
        column = 9
        coordinates = Coordinates(row, column)
        cell = Cell(coordinates)
        cell.set_value(CellType.LIVE)
        self.assertTrue(cell.type() == CellType.LIVE)
        self.assertTrue(cell.get_value() == CellType.LIVE.value)
        cell.get_coordinates().row = 2
        cell.get_coordinates().column = 1
        self.assertFalse(cell.get_coordinates().row == row, "Cell object did not change row value")
        self.assertFalse(cell.get_coordinates().column == column, "Cell object did not change column value")

    def test_create_cell_with_negative_type(self):
        with self.assertRaises(TypeError):
            Cell(Coordinates(5, 5), 'MISS')

    def test_change_cell_with_negative_type(self):
        cell = Cell(Coordinates(9, 9), CellType.KILLED)
        with self.assertRaises(TypeError):
            cell.set_value(list('miss'))


if __name__ == "__main__":
    unittest.main()
