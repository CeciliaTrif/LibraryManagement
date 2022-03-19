from Domain.BookValidator import BookValidator

from Domain.Library import Library
from Service.BookService import BookService

from Repository.FileRepository import FileRepository

from Test.Utils import clear_file


def test_book_service():
    clear_file("library_test.txt")
    clear_file("book_test.txt")
    library_repo = FileRepository("library_test.txt")
    book_repo = FileRepository("book_test.txt")
    book_val = BookValidator()
    book_service = BookService(book_repo, book_val)

    library_repo.add(Library("1", "name", 12, "aaa"))

    book_service.add("1", "1", "ihatethis", 2000)
    assert len(book_service.get_all()) == 1
    added = book_service.get_by_id('1')
    assert added is not None

    try:
        book_service.add("1", "1", "ihatethis", 2000)
        assert False
    except Exception:
        assert True
