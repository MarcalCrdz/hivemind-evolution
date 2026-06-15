class Entity:
    def __init__(self, entity_id: int):
        self.id = entity_id
        self.components = {}