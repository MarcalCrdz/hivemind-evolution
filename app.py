from engine.world import World
from engine.entity_manager import EntityManager
from components.position import PositionComponent
from systems.movement_system import MovementSystem

def main():
    world = World()

    print("HiveMind Evolution")
    print(f"Grid: {world.grid.width} x {world.grid.height}")


    manager = EntityManager()

    entity = manager.create_entity()

    entity.add_component(PositionComponent(x=10, y=20))

    position = entity.get_component(PositionComponent)

    movement_system = MovementSystem(manager)
    movement_system.update()

    print(position.x)
    print(position.y)



if __name__ == "__main__":
    main()