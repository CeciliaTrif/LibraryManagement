from Domain.Entity import Entity


class Book(Entity):
    def __init__(self, book_id, library_id, name, year):
        super().__init__(book_id)
        self.__library_id = library_id
        self.__name = name
        self.__year = year

    @property
    def library_id(self):
        return self.__library_id

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f"Book ID: {self.entity_id}, Library ID:{self.library_id}, Name:{self.name}, Year:{self.year}"

    def __eq__(self, other):
        return type(self) == type(other) and self.entity_id == other.book_id
