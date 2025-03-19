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
        self._lent_collection = []

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

    def search_book_by_name_in_lib_collection(self, book_by_name):
        if not isinstance(book_by_name, str):
            book_by_name = str(book_by_name)
        book_by_name = book_by_name.strip().lower()
        book_found = None
        for elem in self._library_collection:
            if elem.title.lower() == book_by_name:
                print('Book found!')
                book_found = elem
                break
        return book_found

    def search_lent_book_lent_collection(self, book_by_name):
        if not isinstance(book_by_name, str):
            book_by_name = str(book_by_name)
        book_by_name = book_by_name.strip().lower()
        dict_found = None
        for elem in self._lent_collection:
            if elem['lent book'].title.lower() == book_by_name:
                print('Dict of the lent book found!')
                dict_found = elem
                break
        return dict_found

    def lend_book(self, lender_name, book_title, lending_date, returning_date):
        if not isinstance(lender_name, str):
            raise ValueError('The name of the lender must be a string.')
        if not isinstance(book_title, str):
            raise ValueError('The title of the book must be a string.')
        # Control that dates follow the correct pattern
        if not isinstance(lending_date, str):
            raise ValueError('The lending date must be a string.')
        if not isinstance(returning_date, str):
            raise ValueError('The returning date must be a string.')
        book_to_lend = self.search_book_by_name_in_lib_collection(book_title)
        if not isinstance(book_to_lend, Book):
            raise ValueError('Book not found.')
        self._library_collection.remove(book_to_lend)
        dict_of_lent_book = {
            'lender name': lender_name,
            'lending date': lending_date,
            'returning date': returning_date,
            'lent book': book_to_lend
        }
        self._lent_collection.append(dict_of_lent_book)
        print(f'Book successfully lent to {lender_name}!')

    def return_book(self, book_title):
        if not isinstance(book_title, str):
            raise ValueError('The title of the book must be a string.')
        returning_dict = self.search_lent_book_lent_collection(book_title)
        if not isinstance(returning_dict, dict):
            raise ValueError('Dict of the lent book not found.')
        self._lent_collection.remove(returning_dict)
        self._library_collection.append(returning_dict['lent book'])
        print('Book successfully returned!')

    def __str__(self):
        string_to_return = (f'{self._library_name} library of {self._library_city} city\n'
                            f'Books in collection: {len(self._library_collection)}\n'
                            f'Books List: [\n')
        for book in self._library_collection:
            string_to_return += f'\t{book.title}\n'
        string_to_return += ']'
        return string_to_return