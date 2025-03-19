from book import Book
from library import Library

if __name__ == '__main__':
    my_library = Library('Babilonia', 'Scandiano')
    my_library.load_book_collection_from_file()
    print(my_library)
    print('\n')

    my_library.lend_book('Nicolò', 'Harry Potter', '34/23/2048', '0/0/0')
    print(my_library)
    print('\n')

    my_library.return_book('Harry Potter')
    print(my_library)
    print('\n')

