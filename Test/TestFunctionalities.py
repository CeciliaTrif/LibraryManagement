from Domain.BookValidator import BookValidator
from Domain.LibraryValidator import LibraryValidator
from Domain.Library import Library
from Service.BookService import BookService
from Service.LibraryService import LibraryService
from Repository.FileRepository import FileRepository
from Test.Utils import clear_file
from Service.Functionalities import Functionalities


def test_functionalities():
    clear_file("library_test.txt")
    clear_file("book_test.txt")
    library_repo = FileRepository("library_test.txt")
    book_repo = FileRepository("book_test.txt")
    book_val = BookValidator()
    lib_val = LibraryValidator()
    book_service = BookService(book_repo, book_val)
    library_service = LibraryService(library_repo, lib_val)
    service_funcs = Functionalities(book_service, library_service)
    library_repo.add(Library("4", "name1", 12, "aaa"))
    library_repo.add(Library("2", "name2", 10, "aaa"))
    library_repo.add(Library("3", "name3", 5, "aaa"))
    book_service.add("1", "1", "rrr", 2000)
    book_service.add("2", "2", "rrr", 2000)
    book_service.add("3", "3", "qwe", 2000)

    function1_list = service_funcs.libs_decreasing_order_by_amount_of_books()
    assert function1_list[0].entity_id == "4"
    assert function1_list[1].entity_id == "2"
    assert function1_list[2].entity_id == "3"

    function2_list = list(service_funcs.books_in_more_libs())

    assert function2_list[0].entity_id == "1"
    assert function2_list[1].entity_id == "2"