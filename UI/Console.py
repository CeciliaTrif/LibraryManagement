from Service.BookService import BookService
from Service.LibraryService import LibraryService
from Service.ExcelExportService import ExcelExportService
from Service.Functionalities import Functionalities


class Console:
    def __init__(self, library_service: LibraryService, book_service: BookService, functionalities: Functionalities,
                 excel_export_service: ExcelExportService):
        self.__functionalities = functionalities
        self.__library_service = library_service
        self.__book_service = book_service
        self.__excel_export_service = excel_export_service

    def ui_print_list(self, element_list):
        """
        Printeaza o lista cu elemente,element cu element
        :param element_list: lista
        :return: -
        """
        for element in element_list:
            print(element)

    # class add

    def ui_add_book(self):
        """
        Adauga carte
        :return: -
        """
        try:
            book_id = input("Introduceti id-ul cartii: ")
            library_id = input("Introduceti id-ul bibleotecii: ")
            name = input("Introduceti numele cartii: ")
            year = int(input("Introduceti anul aparitiei: "))
            self.__book_service.add(book_id, library_id, name, year)

        except ValueError as v_error:
            print(v_error)

        except KeyError as k_error:
            print(k_error)

        except Exception as error:
            print(error)

    def ui_add_library(self):
        """
        Adauga librarie
        :return: -
        """
        try:
            library_id = input("Introduceti id-ul bibleotecii ")
            name = input("Introduceti numele bibleotecii ")
            books_amount = int(input("Introduceti numarul de carti: "))
            category = input("Introduceti categoria: ")
            self.__library_service.add(library_id, name, books_amount, category)

        except ValueError as v_error:
            print(v_error)

        except KeyError as k_error:
            print(k_error)

        except Exception as error:
            print(error)

    # functionalities
    def ui_libs_decreasing_order_by_amount_of_books(self):
        """
        Af. toate librariile in ord descr dupa numarul cartilor, si numarul cartilor dintr-o anumita categorie
        :return: -
        """

        sorted_libraries = self.__functionalities.libs_decreasing_order_by_amount_of_books()
        self.ui_print_list(sorted_libraries)
        for x in self.__functionalities.books_for_each_category():
            print(x)


    def ui_books_in_more_libs(self):
        """
        Af. toate cartile care se afla in mai multe librarii.
        :return: -
        """
        all_books = self.__functionalities.books_in_more_libs()
        self.ui_print_list(all_books)

    def ui_to_excel(self):
        file_name = input("Ce nume va avea fisierul? ")
        self.__excel_export_service.export(str(file_name) + ".xls")

    # menu
    def run_menu(self):
        while True:
            print("\n1.Adauga bilbleoteca.")
            print("2.Adauga carte.")
            print("3.Afisarea bibl. in ordine descrescatoare dupa nr cartilor."
                  " Se afiseaza si numarul cartilor dintr-o anumita categorie.")
            print("4.Afisarea tuturor cartilor care se gasesc in mai multe bibleoteci(cel putin 2).")
            print("5.Creeaza fisier Excel cu nume citit de la tastatura care va contine bibl. si cartile care se afla "
                  "in acecste bibl. afisate in functie de categorii in format tabelar.")
            print("x.Iesire.")
            print("a1.Afiseaza bibleoteci.")
            print("a2.Afiseaza carti.")

            option = input("Alegeti o optiune:")
            if option == "1":
                self.ui_add_library()
            elif option == "2":
                self.ui_add_book()
            elif option == "3":
                self.ui_libs_decreasing_order_by_amount_of_books()
            elif option == "4":
                self.ui_books_in_more_libs()
            elif option == "5":
                self.ui_to_excel()
            elif option == "a1":
                self.ui_print_list(self.__library_service.get_all())
            elif option == "a2":
                self.ui_print_list(self.__book_service.get_all())
            elif option == "x":
                return False
            else:
                print("Optiune invalida!")
