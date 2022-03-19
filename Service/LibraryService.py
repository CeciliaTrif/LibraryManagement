from Domain.Library import Library
from Repository import FileRepository
from Domain import LibraryValidator


class LibraryService:
    def __init__(self, library_repository: FileRepository, library_validator: LibraryValidator):
        self.__library_repository = library_repository
        self.__library_validator = library_validator

    def get_by_id(self, car_id):
        return self.__library_repository.get_by_id(car_id)

    def get_all(self):
        return self.__library_repository.get_all()

    def add(self, library_id, name, books_amount, category):
        library = Library(library_id, name, books_amount, category)
        self.__library_validator.validate(library)
        self.__library_repository.add(library)
