class Book:

    id: int
    title: str
    author: str

    def __init__(self, book_id: int, title: str, author: str):
        self.id = book_id
        self.title = title
        self.author = author

    def serialize(self):
        return {"id": self.id, "title": self.title, "author": self.author}

    def __str__(self):
        return str(self.serialize())

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.id == other.id and self.title == other.title and self.author == other.author
        else:
            return False

    def __hash__(self):
        return hash((self.id, self.title, self.author))
