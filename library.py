from book import Book


class Library(object):
    def __init__(self, library_name, library_city):
        if not isinstance(library_name, str):
            raise ValueError('The name of the library must be a string.')
        if not isinstance(library_city, str):
            raise ValueError('The name of the city where the library belong must be a string.')
        self._library_name = library_name
        self._library_city = library_city
        self._library_collection = []

    @property
    def library_name(self):
        return self._library_name

    @property
    def library_city(self):
        return self._library_city

    def add_book_to_collection(self, book):
        if not isinstance(book, Book):
            raise ValueError('The book must be a Book object.')
        self._library_collection.append(book)

    def load_book_collection_from_file(self, path):
        pass
