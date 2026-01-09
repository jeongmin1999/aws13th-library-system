from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_borrowed: bool = False

    def __str__(self):
        if self.is_borrowed:
            status = "대출불가"
        else:
            status = "대출가능"
        return f"{self.title} {self.author} {self.isbn} / {status}"

@dataclass
class Member:
    name: str
    phone_number: str
    borrowed_book: List[str] = field(default_factory=list)

    def __str__(self):
        return f"{self.name} ({self.phone_number}), 대출중인 책은 총 {len(self.borrowed_book)}권 입니다."


