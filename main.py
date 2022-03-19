from Domain.BookValidator import BookValidator
from Domain.LibraryValidator import LibraryValidator
from Service.BookService import BookService
from Service.LibraryService import LibraryService
from Service.Functionalities import Functionalities
from Repository.FileRepository import FileRepository
from Service.ExcelExportService import ExcelExportService
from Test.RunAll import run_all_tests
from UI.Console import Console


def main():
    library_repository = FileRepository("libraries.txt")
    book_repository = FileRepository("books.txt")

    library_validator = LibraryValidator()
    book_validator = BookValidator()

    library_service = LibraryService(library_repository, library_validator)

    book_service = BookService(book_repository, book_validator)
    excel_export_service = ExcelExportService(book_repository, library_repository)
    functionalities = Functionalities(book_service, library_service)

    console = Console(library_service, book_service, functionalities, excel_export_service)
    console.run_menu()


run_all_tests()
main()
