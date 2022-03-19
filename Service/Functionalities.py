from Service.BookService import BookService
from Service.LibraryService import LibraryService


class Functionalities:
    def __init__(self, book_service: BookService, library_service: LibraryService):
        self.__book_service = book_service
        self.__library_service = library_service

    def libs_decreasing_order_by_amount_of_books(self):
        """
        sorteaza librariile in functie de numarul de carti
        :return: lista sortata
        """
        libraries = self.__library_service.get_all()
        sorted_list = sorted(libraries, key=lambda library: library.books_amount, reverse=True)
        return sorted_list

    def books_for_each_category(self):
        libraries = self.__library_service.get_all()
        category_list = []

        for library in libraries:
            category_list.append(library.category)
        sums_list = []

        for library in libraries:
            the_sum = 0
            for category in category_list:
                if library.category == category:
                    the_sum = the_sum + library.books_amount
            sums_list.append(the_sum)
        return zip(category_list, sums_list)

    def number_of_books_in_one_category(self, category):
        """
        Determina suma cartilor dintro categorie aleasa
        :param category: categoria
        :return: suma
        """
        libraries = self.__library_service.get_all()

    def books_same_lib(self, book):
        """
        functie care verifica daca o carte se afla in mai multe bibl.
        :param book: un obiect
        :return: True daca e in mai multe bibl. false daca nu
        """
        books = self.__book_service.get_all()
        counter = 0
        for book_local in books:
            if book_local.name == book.name:
                counter = counter + 1
        if counter >= 2:
            return True
        else:
            return False

    def books_in_more_libs(self):
        """
        Det cartile care se alfa in mai multe bibl.
        :return: lista de carti gasite
        """

        books = self.__book_service.get_all()

        books_result = filter(lambda book: self.books_same_lib(book), books)

        return books_result
