from Repository.FileRepository import FileRepository


class BookValidator:
    def validate(self, book):
        errors = []
        library_id_list = []
        library_repo = FileRepository("libraries.txt")
        libraries = library_repo.get_all()

        for library in libraries:
            if library.entity_id not in library_id_list:
                library_id_list.append(library.entity_id)

        if book.library_id not in library_id_list:
            errors.append("Trebuie sa introduceti un id bibleoteca existent!")
        if book.name == "":
            errors.append("Trebuie sa introduceti un nume!")
        if book.year < 0:
            errors.append("Anul nu poate sa fie negativ!")
        if len(errors) > 0:
            raise ValueError(errors)
