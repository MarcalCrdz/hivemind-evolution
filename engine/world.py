from engine.grid import Grid


class World:
    def __init__(self):
        self.grid = Grid(
            width=50,
            height=100
        )