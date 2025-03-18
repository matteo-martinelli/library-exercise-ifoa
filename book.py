class Book(object):
    def __init__(self, title, author, publication_year, total_pages):
        if not isinstance(title, str):
            raise TypeError('Title must be a string.')
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._total_pages = total_pages

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._title

    @property
    def publication_year(self):
        return self._publication_year

    @property
    def total_pages(self):
        return self._total_pages

    def __str__():
        pass

    def __repr__():
        pass