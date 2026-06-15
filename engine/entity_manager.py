from engine.entity import Entity


class EntityManager:

    def __init__(self):
        self.entities = {}
        self.next_id = 1

    def create_entity(self):

        entity = Entity(self.next_id)

        self.entities[self.next_id] = entity

        self.next_id += 1

        return entity