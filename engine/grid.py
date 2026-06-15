from engine.cell import Cell


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.cells = []

        for y in range(height):

            row = []

            for x in range(width):

                row.append(Cell(x, y))

            self.cells.append(row)