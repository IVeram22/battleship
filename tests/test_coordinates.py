import unittest

from coordinates.coordinates import Coordinates


class TestCoordinates(unittest.TestCase):
    def test_create_coordinates_positive(self):
        row = 1
        column = 2
        coordinates = Coordinates(row, column)
        self.assertTrue(coordinates.row == row, "Row object is not equal to the initial value")
        self.assertTrue(coordinates.column == column, "Column object is not equal to the initial value")

    def test_change_coordinates_positive(self):
        coordinates = Coordinates(0, 0)
        row = 5
        column = 7
        coordinates.row = row
        coordinates.column = column
        self.assertTrue(coordinates.row == row, "Row object is not equal to the initial value")
        self.assertTrue(coordinates.column == column, "Column object is not equal to the initial value")

    def test_create_coordinates_with_negative_row_value(self):
        row = -1
        column = 2
        with self.assertRaises(ValueError):
            Coordinates(row, column)

    def test_create_coordinates_with_negative_column_value(self):
        row = 0
        column = 11
        with self.assertRaises(ValueError):
            Coordinates(row, column)

    def test_create_coordinates_with_negative_row_type(self):
        row = '0'
        column = 10
        with self.assertRaises(TypeError):
            Coordinates(row, column)

    def test_create_coordinates_with_negative_column_type(self):
        row = 3
        column = list('10')
        with self.assertRaises(TypeError):
            Coordinates(row, column)


if __name__ == "__main__":
    unittest.main()
