import datetime
import re
from typing import List, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag

from models import Book, Loan


class LoanParser:
    @staticmethod
    def parse_loans(content: str) -> List[Loan]:
        loans: List[Loan] = []
        soup = BeautifulSoup(content, "html.parser")
        tr_loans = soup.find("table", {"id": "loans-table"}).findChild("tbody").findChildren("tr", recursive=False)
        for i in range(len(tr_loans)):
            tr_loan = tr_loans[i]
            # Only get rows with loan data in it
            if len(tr_loan.findChildren("td", recursive=False)) > 1:
                # Get the next TR element (if applicable)
                next_tr_loan: Tag = tr_loans[i + 1] if i < len(tr_loans) - 1 else None
                # Checks whether you can re-borrow the book
                can_re_borrow = next_tr_loan is None or "renewal-warning" not in next_tr_loan.get_attribute_list(
                    "class"
                )
                loans.append(LoanParser.parse_loan(tr_loan, can_re_borrow))
        return loans

    @staticmethod
    def parse_loan(el: Tag, can_re_borrow: bool) -> Loan:
        loan = Loan()

        tds: List[Tag] = el.findChildren("td", recursive=False)

        loan.id = LoanParser.parse_loan_id(tds[0], can_re_borrow)
        loan.book = LoanParser.parse_book(tds[1])
        loan.borrowed_from = LoanParser.parse_borrowed_from(tds[2])
        loan.borrowed_at = LoanParser.parse_borrowed_at(tds[2])
        loan.due_date = LoanParser.parse_due_date(tds[3])
        loan.can_re_borrow = can_re_borrow

        return loan

    @staticmethod
    def parse_loan_id(td: Tag, can_re_borrow: bool) -> Optional[str]:
        if can_re_borrow:
            return re.search(r"loan\[(\d+)\]", td.findChild("input").get("name")).group(1)
        else:
            return None

    @staticmethod
    def parse_book(td: Tag) -> Book:
        a_el: Tag = td.findChild("a", {"class": "hidden-phone"})
        book_id: int = int(re.search(r"/titel/(\d+)/?", a_el.get("href")).group(1))
        title: str = a_el.findChild("strong").text.strip()
        author: str = a_el.findChild("span").text.strip()

        return Book(book_id, title, author)

    @staticmethod
    def parse_borrowed_at(td: Tag) -> datetime.date:
        borrowed_at = td.findChild("a", {"class": "hidden-phone"}).findChild("span").text.strip()
        return datetime.date.fromisoformat(borrowed_at)

    @staticmethod
    def parse_borrowed_from(td: Tag) -> str:
        borrowed_at = LoanParser.parse_borrowed_at(td)
        full_text = td.findChild("a", {"class": "hidden-phone"}).text
        trimmed_text = full_text.replace(str(borrowed_at), "").strip()
        return trimmed_text

    @staticmethod
    def parse_due_date(td: Tag) -> datetime.date:
        return datetime.date.fromisoformat(td.findChild("strong").text.strip())


if __name__ == "__main__":
    with open("../../responses/loans-2.html") as f:
        loans = LoanParser.parse_loans(f.read())
        for loan in loans:
            print(loan)
