class Simulation:

    def __init__(self):
        self.systems = []
        self.tick = 0

    def add_system(self, system):
        self.systems.append(system)

    def run(self, ticks: int):
        for _ in range(ticks):

            self.tick += 1

            print(f"\n===== Tick {self.tick} =====")

            for system in self.systems:
                system.update()