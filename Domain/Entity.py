class Entity:
    def __init__(self, entity_id):
        self.__entity_id = entity_id

    def __eq__(self, other):
        return type(self) == type(other) and self.__entity_id == other.__entity_id

    @property
    def entity_id(self):
        return self.__entity_id


