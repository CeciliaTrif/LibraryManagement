from copy import deepcopy
import jsonpickle as jsonpickle
from Domain.Entity import Entity


class FileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__storage = {}  # dictionar avand drept chei id-urile maisnilor si drept valori masinile in sine

    def __read_file(self):
        try:
            with open(self.__file_name, 'r') as fp:
                self.__storage = jsonpickle.decode(fp.read())
        except:
            self.__storage = {}

    def __write_to_file(self):
        with open(self.__file_name, 'w') as fp:
            fp.write(jsonpickle.encode(self.__storage))

    def get_all(self):
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def get_by_id(self, entity_id):
        self.__read_file()
        if entity_id in self.__storage:
            return deepcopy(self.__storage[entity_id])
        return None

    def add(self, entity: Entity):

        if self.get_by_id(entity.entity_id):
            raise KeyError(f"Exista deja o entitate cu id-ul {entity.entity_id}.")

        self.__storage[entity.entity_id] = entity
        self.__write_to_file()

    def delete(self, entity_id):
        if self.get_by_id(entity_id) is None:
            raise KeyError(f"Nu exista nicio entitate cu id-ul {entity_id}.")
        del self.__storage[entity_id]
        self.__write_to_file()

    def update(self, entity: Entity):
        if self.get_by_id(entity.entity_id) is None:

            raise KeyError(f"Nu exista nicio entitate cu id-ul {entity.entity_id}.")
        self.__storage[entity.entity_id] = entity
        self.__write_to_file()
