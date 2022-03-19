from Domain.Entity import Entity


class Library(Entity):
    """Descrie entitatea librarie"""

    def __init__(self, library_id, name, books_amount, category):
        super().__init__(library_id)
        self.__name = name
        self.__books_amount = books_amount
        self.__category = category

    @property
    def name(self):
        return self.__name

    @property
    def books_amount(self):
        return self.__books_amount

    @property
    def category(self):
        return self.__category

    def __str__(self):
        return f"Library ID: {self.entity_id}, Name:{self.name}, Books Amount:{self.books_amount}," \
               f" Category:{self.category}"

    def __eq__(self, other):
        return type(self) == type(other) and self.entity_id == other.library_id
