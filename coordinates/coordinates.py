from coordinates.layout import Layout


class Coordinates:
    row = Layout()
    column = Layout()

    def __init__(self, row, column):
        self.row = row
        self.column = column
