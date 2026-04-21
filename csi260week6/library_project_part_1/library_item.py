"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""

class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """
    def __init__(self, name, isbn, tags=None):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        :param tags: (list) List of CategoryTags
        """
        self.name = name
        self.isbn = isbn
        if tags:
            self.tags = tags
        else:
            self.tags = list()
        self.resource_type = 'Generic'  # This is the type of item being stored

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match or
        partial match.

        match needs to be redefined for any subclasses.  Please see the
        note/notebook case study from Chapter 2 as an example of how match
        is designed to work.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in (str(tag).lower() for tag in self.tags)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """
        return f'{self.name}\n{self.isbn}\n{self.type}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the ISBN of the item
        I.E.
        Moby Dick - 235253234
        """
        return f'{self.name} - {self.isbn}'


class Book(LibraryItem):
    def __init__(self, name, isbn, author, version, edition, tags=None):
        super.__init__(name, isbn, tags)
        self.author = author
        self.version = version
        self.edition = edition
        self.resource_type = 'Book'

    def match(self, filter_text):
        if super().match(filter_text):
            return True
        filter_lower = filter_text.lower()
        return filter_lower in self.author.lower() or \
               filter_lower in self.version.lower() or \
               filter_lower in self.edition.lower()
    
    def __str__(self):
        return (f'{super().__str__()}\n'
            f'Author: {self.author}\n'
            f'Version: {self.version}\n'
            f'Edition: {self.edition}')
    
    def to_short_string(self):
        return (f':::BOOK::: {self.name} - {self.author} - {self.isbn} - {self.version} - {self.edition}')