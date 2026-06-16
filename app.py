from engine.world import World
from engine.entity_manager import EntityManager
from components.position import PositionComponent
from systems.movement_system import MovementSystem
from engine.simulation import Simulation

def main():
    world = World()

    print("HiveMind Evolution")
    print(f"Grid: {world.grid.width} x {world.grid.height}")


    manager = EntityManager()

    entity = manager.create_entity()

    entity.add_component(PositionComponent(10, 20))

    movement_system = MovementSystem(manager)

    simulation = Simulation()

    simulation.add_system(movement_system)

    simulation.run(5)



if __name__ == "__main__":
    main()