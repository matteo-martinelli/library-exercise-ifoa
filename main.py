from book import Book
from library import Library

if __name__ == '__main__':
    my_library = Library('Babilonia', 'Scandiano')
    my_library.load_book_collection_from_file()
    print(my_library)
    book_searched = my_library.search_book_by_name('Guida Galattica per autostoppisti')
    print(book_searched)
