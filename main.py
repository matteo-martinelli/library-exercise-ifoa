from book import Book
from library import Library

if __name__ == '__main__':
    my_library = Library('Babilonia', 'Scandiano')
    my_library.load_book_collection_from_file()
    print(my_library)
    my_library.write_to_txt_file()