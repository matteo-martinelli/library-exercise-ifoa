class Book(object):
    def __init__(self, title, author, publication_year, total_pages):
        if not isinstance(title, str):
            raise ValueError('Title must be a string.')
        if not isinstance(author, str):
            raise ValueError('Author must be a string.')
        if not publication_year <= 2025:
            raise ValueError('Publication year must be lower than the current year.')
        if not total_pages > 0:
            raise ValueError('Pages must be a positive integer.')
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

    @title.setter
    def title(self, title_to_update):
        if not isinstance(title_to_update, str):
            raise ValueError('Title must be a string.')
        self._title = title_to_update

    def __str__(self):
        string_to_return = f'[Title]: {self._title}\n[Author]: {self._author}\n[Pub Year]: {self._publication_year}\n[Total Pages]: {self._total_pages}'
        return string_to_return

    #def __repr__():
    #    pass