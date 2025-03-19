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

    def load_book_collection_from_file(self):
        path = 'book_collection.txt'
        try:
            with open(path, 'r') as f:
                content = f.read()
                books_elem = content.strip().split('-')
                books_list = list()
                for elem in books_elem:
                    book_elem = elem.strip().split('\n')
                    books_list.append(book_elem)
                for book in books_list:
                    book_to_add = Book(book[0], book[1], int(book[2]), int(book[3]))
                    self._library_collection.append(book_to_add)
        except FileNotFoundError:
            print('File does not exist!')

    """
    File to write: 
    library name: name_of_the_library
    library city: city_of_the_library
    books in collection: number_of_books_in_collection
    average pages in collection: average_pages_in_collection
    """
    def write_to_txt_file(self):
        string_to_write = (f'library name: {self._library_name}\n'
                           f'library city: {self._library_city}\n'
                           f'books in collection: {len(self._library_collection)}\n'
                           f'average pages in collection: {self.calculate_average_pages()}')
        try:
            with open('library_summary.txt', 'a') as f:
                f.write(string_to_write)
        except Exception as e:
            print(e)
    def calculate_average_pages(self):
        total_pages_in_library = 0
        for elem in self._library_collection:
            total_pages_in_library += elem.total_pages
        average_pages_in_library = total_pages_in_library / len(self._library_collection)
        return average_pages_in_library

    def __str__(self):
        string_to_return = (f'{self._library_name} library of {self._library_city} city\n'
                            f'Books in collection: {len(self._library_collection)}\n'
                            f'Books List: [\n')
        for book in self._library_collection:
            string_to_return += f'\t{book.title}\n'
        string_to_return += ']'
        return string_to_return