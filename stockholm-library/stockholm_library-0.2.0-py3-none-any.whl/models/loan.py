import datetime
from typing import Optional

from models.book import Book


class Loan:

    id: Optional[int]
    book: Book
    borrowed_from: str
    borrowed_date: datetime.date
    due_date: datetime.date
    can_re_borrow: bool

    def serialize(self):
        return {
            "id": self.id,
            "book": self.book.serialize(),
            "borrowed_from": self.borrowed_from,
            "borrowed_date": self.borrowed_date,
            "due_date": self.due_date,
            "can_re_borrow": self.can_re_borrow,
        }

    def __str__(self):
        return str(self.serialize())
