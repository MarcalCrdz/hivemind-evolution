class Entity:
    def __init__(self, entity_id: int):
        self.id = entity_id
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type):
        return self.components.get(component_type)

    def has_component(self, component_type):
        return component_type in self.components

    def remove_component(self, component_type):
        return self.components.pop(component_type, None)