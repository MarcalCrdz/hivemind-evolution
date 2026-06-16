from components.position import PositionComponent

class MovementSystem:

    def __init__(self, entity_manager):
        self.entity_manager = entity_manager

    def update(self):
        for entity in self.entity_manager.entities.values():

            if entity.has_component(PositionComponent):

                position = entity.get_component(PositionComponent)

                position.x += 1

                print(f"Entity {entity.id} moved to ({position.x}, {position.y})")