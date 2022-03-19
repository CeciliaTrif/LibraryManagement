from Domain.Book import Book
from Repository import FileRepository
from Domain import BookValidator


class BookService:
    def __init__(self, book_repository: FileRepository, book_validator: BookValidator):
        self.__book_repository = book_repository
        self.__book_validator = book_validator

    def get_by_id(self, book_id):
        return self.__book_repository.get_by_id(book_id)

    def get_all(self):
        return self.__book_repository.get_all()

    def add(self, book_id, library_id, name, year):
        book = Book(book_id, library_id, name, year)
        self.__book_validator.validate(book)
        self.__book_repository.add(book)
