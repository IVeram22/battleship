import unittest

from coordinates.coordinates import Coordinates
from ship.ship import Ship
from ship.deck import ShipDeck


class TestShip(unittest.TestCase):
    def test_create_and_kill_ship_positive(self):
        start_coordinates = Coordinates(1, 1)
        end_coordinates = Coordinates(1, 4)
        ship = Ship(start_coordinates, end_coordinates, ShipDeck.FOUR)
        self.assertTrue(ship.is_alive(), "The ship is dead")
        self.assertTrue(ship.wound(Coordinates(1, 1)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(1, 2)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(1, 3)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(1, 4)), "The ship was not wound")
        self.assertFalse(ship.is_alive(), "The ship is alive")

    def test_create_and_kill_one_deck_ship_positive(self):
        coordinates = Coordinates(1, 4)
        ship = Ship.new_one_deck_ship(coordinates)
        self.assertTrue(ship.is_alive(), "The ship is dead")
        self.assertTrue(ship.wound(Coordinates(1, 4)), "The ship was not wound")
        self.assertFalse(ship.is_alive(), "The ship is alive")

    def test_create_and_kill_two_deck_ship_positive(self):
        start_coordinates = Coordinates(2, 2)
        end_coordinates = Coordinates(3, 2)
        ship = Ship.new_two_deck_ship(start_coordinates, end_coordinates)
        self.assertTrue(ship.is_alive(), "The ship is dead")
        self.assertTrue(ship.wound(Coordinates(2, 2)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(3, 2)), "The ship was not wound")
        self.assertFalse(ship.is_alive(), "The ship is alive")

    def test_create_and_kill_three_deck_ship_positive(self):
        start_coordinates = Coordinates(9, 2)
        end_coordinates = Coordinates(7, 2)
        ship = Ship.new_three_deck_ship(start_coordinates, end_coordinates)
        self.assertTrue(ship.is_alive(), "The ship is dead")
        self.assertTrue(ship.wound(Coordinates(9, 2)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(8, 2)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(7, 2)), "The ship was not wound")
        self.assertFalse(ship.is_alive(), "The ship is alive")

    def test_create_and_kill_four_deck_ship_positive(self):
        start_coordinates = Coordinates(0, 0)
        end_coordinates = Coordinates(0, 3)
        ship = Ship.new_four_deck_ship(start_coordinates, end_coordinates)
        self.assertTrue(ship.is_alive(), "The ship is dead")
        self.assertTrue(ship.wound(Coordinates(0, 2)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(0, 1)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(0, 0)), "The ship was not wound")
        self.assertTrue(ship.wound(Coordinates(0, 3)), "The ship was not wound")
        self.assertFalse(ship.is_alive(), "The ship is alive")

    def test_verify_one_deck_ship_cells_coordinates_positive(self):
        start_coordinates = Coordinates(6, 9)
        ship = Ship.new_one_deck_ship(start_coordinates)
        expected_coordinates = Coordinates(6, 9)
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            if ship_cells[index].get_coordinates().row == expected_coordinates.row \
                    and ship_cells[index].get_coordinates().column == expected_coordinates.column:
                size += 1
        self.assertTrue(1 == size, "Coordinates added incorrectly")

    def test_verify_two_deck_ship_cells_coordinates_positive(self):
        start_coordinates = Coordinates(4, 7)
        end_coordinates = Coordinates(4, 8)
        ship = Ship.new_two_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(4, 7),
            Coordinates(4, 8)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")

    def test_verify_three_deck_ship_cells_coordinates_positive(self):
        start_coordinates = Coordinates(3, 5)
        end_coordinates = Coordinates(5, 5)
        ship = Ship.new_three_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(5, 5),
            Coordinates(4, 5),
            Coordinates(3, 5)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")

    def test_verify_four_deck_ship_cells_coordinates_positive(self):
        start_coordinates = Coordinates(0, 0)
        end_coordinates = Coordinates(0, 3)
        ship = Ship.new_four_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(0, 0),
            Coordinates(0, 1),
            Coordinates(0, 2),
            Coordinates(0, 3)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")

    def test_verify_two_deck_ship_cells_coordinates_with_incorrect_size(self):
        start_coordinates = Coordinates(4, 7)
        end_coordinates = Coordinates(4, 9)
        ship = Ship.new_two_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(4, 7),
            Coordinates(4, 8)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")
        self.assertFalse(ship.wound(Coordinates(4, 9)), "The ship was wound")

    def test_verify_three_deck_ship_cells_coordinates_with_incorrect_size(self):
        start_coordinates = Coordinates(3, 5)
        end_coordinates = Coordinates(7, 5)
        ship = Ship.new_three_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(5, 5),
            Coordinates(4, 5),
            Coordinates(3, 5)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")
        self.assertFalse(ship.wound(Coordinates(6, 5)), "The ship was wound")

    def test_verify_four_deck_ship_cells_coordinates_with_incorrect_size(self):
        start_coordinates = Coordinates(0, 0)
        end_coordinates = Coordinates(0, 9)
        ship = Ship.new_four_deck_ship(start_coordinates, end_coordinates)
        expected_coordinates = [
            Coordinates(0, 0),
            Coordinates(0, 1),
            Coordinates(0, 2),
            Coordinates(0, 3)
        ]
        ship_cells = ship.get_cells()
        size = 0
        for index in range(len(ship_cells)):
            for coordinate in expected_coordinates:
                if ship_cells[index].get_coordinates().row == coordinate.row \
                        and ship_cells[index].get_coordinates().column == coordinate.column:
                    size += 1
        self.assertTrue(len(expected_coordinates) == size, "Coordinates added incorrectly")
        self.assertFalse(ship.wound(Coordinates(0, 4)), "The ship was wound")

    def test_test_create_one_deck_ship_with_incorrect_coordinates(self):
        start_coordinates = Coordinates(0, 0)
        end_coordinates = Coordinates(5, 1)
        with self.assertRaises(ValueError):
            Ship(start_coordinates, end_coordinates, ShipDeck.ONE)

    def test_test_create_four_deck_ship_with_incorrect_coordinates(self):
        start_coordinates = Coordinates(0, 0)
        end_coordinates = Coordinates(1, 9)
        with self.assertRaises(ValueError):
            Ship.new_four_deck_ship(start_coordinates, end_coordinates)


if __name__ == "__main__":
    unittest.main()
