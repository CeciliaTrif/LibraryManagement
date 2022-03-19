from Domain.LibraryValidator import LibraryValidator
from Repository.FileRepository import FileRepository
from Service.LibraryService import LibraryService
from Test.Utils import clear_file


def test_library_service():
    clear_file("library_test.txt")
    library_repository = FileRepository("library_test.txt")
    library_validator = LibraryValidator()
    service = LibraryService(library_repository, library_validator)

    service.add("1", "name", 12, "aaa")
    assert len(service.get_all()) == 1
    added = library_repository.get_by_id("1")
    assert added is not None
    assert added.entity_id == "1"
    assert added.name == "name"
    assert added.books_amount == 12
    assert added.category == "aaa"

    try:
        service.add("1", "name", 12, "aaa")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
