class Author:
    
    all = []
    
    def __init__(self, name = None):
        self.name: str = name
        Author.all.append(self)
        
    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [c.book for c in Contract.all if c.author == self]
    
    def sign_contract(self, book, date, royalties):
        all_criteria_met = isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int)
        if not all_criteria_met:
            raise TypeError("Please ensure that book argument is a Book object, date is a string, and royalties argument is an integer.")
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([c.royalties for c in Contract.all if c.author == self])

class Book:
    
    all = []
    
    def __init__(self, title = None):
        self.title: str = title
        Book.all.append(self)
    
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]

class Contract:
    
    all = []
    
    def __init__(
        self,
        author = None,
        book = None,
        date = None,
        royalties = None
    ):
        self.author: Author = author
        self.book: Book = book
        self.date: str = date
        self.royalties: int = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Argument must be an instance of the Author class")
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Argument must be an instance of the Book class")
        self._book = book
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Argument must be a string")
        self._date = date
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise TypeError("Argument must be an integer")
        self._royalties = royalties
        
    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]