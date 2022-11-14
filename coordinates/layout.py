class Layout:
    """Data descriptor"""

    @classmethod
    def verify_coordinate(cls, number):
        if type(number) != int:
            raise TypeError('Coordinate must be an int type.')
        if number <= -1 or number > 9:
            raise ValueError('Coordinate must be from 0 to 9.')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coordinate(value)
        setattr(instance, self.name, value)
