from Repository.FileRepository import FileRepository
from xlwt import Workbook


class ExcelExportService:
    def __init__(self, book_repo: FileRepository, lib_repo: FileRepository):
        self.__book_repo = book_repo
        self.__lib_repo = lib_repo

    def export(self, file_name):
        """
        Functie care face export catre un fisier excel
        :param file_name: numele fisierului
        :return:
        """
        workbook = Workbook()
        sheet1 = workbook.add_sheet("Sheet 1")
        libraries = self.__lib_repo.get_all()
        category_list = []
        for library in libraries:
            if library.category not in category_list:
                category_list.append(library.category)

        for i in range(0, len(self.__lib_repo.get_all())):
            sheet1.write(i, 2, str(self.__lib_repo.get_all()[i].name))

        for i in range(0, len(self.__book_repo.get_all())):
            sheet1.write(i, 1, str(self.__book_repo.get_all()[i].name))

        for i in range(0, len(category_list)):
            sheet1.write(i, 0, category_list[i])

        workbook.save(file_name)
