from cell.cell import Cell
from cell.type import CellType
from coordinates.coordinates import Coordinates
from ship.controller import ShipController
from ship.deck import ShipDeck


class Ship(ShipController):
    def is_alive(self):
        if self.__life_count <= 0:
            return False
        return True

    def wound(self, coordinates: Coordinates):
        for index in range(len(self.__data)):
            if self.__data[index].get_coordinates().row == coordinates.row \
                    and self.__data[index].get_coordinates().column == coordinates.column:
                self.__data[index].set_value(CellType.KILLED)
                self.__life_count -= 1
                return True
        return False

    def get_cells(self):
        return self.__data

    def __init__(self, start: Coordinates, end: Coordinates, decks: ShipDeck):
        self.__decks = decks
        self.__size = self.__life_count = decks.value
        self.__start = start
        self.__end = end
        self.__data = [Cell(Coordinates(0, 0)) for i in range(self.__size)]
        self.__set_ship_coordinates()

    @staticmethod
    def new_one_deck_ship(coordinates: Coordinates):
        return OneDeckShip(coordinates)

    @staticmethod
    def new_two_deck_ship(start: Coordinates, end: Coordinates):
        return TwoDeckShip(start, end)

    @staticmethod
    def new_three_deck_ship(start: Coordinates, end: Coordinates):
        return ThreeDeckShip(start, end)

    @staticmethod
    def new_four_deck_ship(start: Coordinates, end: Coordinates):
        return FourDeckShip(start, end)

    def __add_single_deck_ship(self):
        if self.__start.row == self.__end.row and self.__start.column == self.__end.column:
            self.__data[0].get_coordinates().row = self.__start.row
            self.__data[0].get_coordinates().column = self.__start.column
            return True
        return False

    def __add_multi_deck_ship(self):
        if self.__start.row == self.__end.row and self.__start.column != self.__end.column:
            row = self.__start.row
            direction = self.__start.column - self.__end.column < 0
            column = self.__start.column if direction else self.__end.column
            for index in range(len(self.__data)):
                self.__data[index].get_coordinates().row = row
                self.__data[index].get_coordinates().column = column
                column += 1
            return True
        elif self.__start.column == self.__end.column and self.__start.row != self.__end.row:
            column = self.__start.column
            direction = self.__start.row - self.__end.row < 0
            row = self.__start.row if direction else self.__end.row
            for index in range(len(self.__data)):
                self.__data[index].get_coordinates().row = row
                self.__data[index].get_coordinates().column = column
                row += 1
            return True
        else:
            return False

    def __set_ship_coordinates(self):
        if self.__size == 1:
            if not self.__add_single_deck_ship():
                raise ValueError('Can not add single deck ship!')
        else:
            if not self.__add_multi_deck_ship():
                raise ValueError('Can not add multi deck ship!')


class OneDeckShip(Ship):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates, coordinates, ShipDeck.ONE)


class TwoDeckShip(Ship):
    def __init__(self, start: Coordinates, end: Coordinates):
        super().__init__(start, end, ShipDeck.TWO)


class ThreeDeckShip(Ship):
    def __init__(self, start: Coordinates, end: Coordinates):
        super().__init__(start, end, ShipDeck.THREE)


class FourDeckShip(Ship):
    def __init__(self, start: Coordinates, end: Coordinates):
        super().__init__(start, end, ShipDeck.FOUR)
