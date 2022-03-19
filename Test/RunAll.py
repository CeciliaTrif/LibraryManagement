from Test.TestBookService import test_book_service
from Test.TestRepository import test_add_repository
from Test.TestLibraryService import test_library_service
from Test.TestFunctionalities import test_functionalities

def run_all_tests():

    test_add_repository()
    test_library_service()
    test_book_service()
    test_functionalities()
