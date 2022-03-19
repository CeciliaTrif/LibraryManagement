class LibraryValidator:
    def validate(self, library):

        errors = []

        if library.name == "":
            errors.append("Trebuie sa introduceti un nume! ")
        if library.books_amount < 0:
            errors.append("Numarul de carti nu poate fi negativ!")
        if len(errors) > 0:
            raise ValueError(errors)
