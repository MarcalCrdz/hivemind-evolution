from engine.world import World
from engine.entity_manager import EntityManager

def main():
    world = World()

    print("HiveMind Evolution")
    print(f"Grid: {world.grid.width} x {world.grid.height}")


    manager = EntityManager()

    entity = manager.create_entity()

    print(entity.id)


if __name__ == "__main__":
    main()