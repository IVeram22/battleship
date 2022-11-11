from abc import ABC, abstractmethod
from coordinates.coordinates import Coordinates


class ShipController(ABC):
    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def wound(self, coordinates: Coordinates):
        pass

    @abstractmethod
    def get_cells(self):
        pass
