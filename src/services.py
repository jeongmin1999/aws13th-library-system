from typing import List

from models import Book,Member
import exceptions as e

class Services:
    def __init__(self):
        ISBN = str #Type Alias ==> 해당 생성자에서 books, members 의 변수 Type Annotation에서 조금더 직관적이기 위해 명시함 , 걍 dict[str, Book] 해도 됨.
        MEMBER_NAME = str # 얘도 마찬가지로 걍 self.member : dict[str, Member] = {} 해도 됨.
        self.books: dict[ISBN, Book] = {}
        self.members: dict[MEMBER_NAME, Member] = {}


    def add_book(self, book: Book) -> None:
        """ 책을 추가한다,,, 메인에서 Library 클래스 객체를 생성하고, 초기 initial_book_data를 넣어두고 해당 객체의 add_book 매서드를 호출할거라서
        self.book 과 인자로 받은 book.isbn을 비교할 수 있다,, 뒤에 함수들도 마찬가지
        """
        if book.isbn in self.books:
            raise e.DuplicateBookError("이미 존재하는 책 입니다.")
        self.books[book.isbn] = book

    def add_member(self, member: Member) -> None:
        if member.name in self.members:
            raise e.DuplicateMemberError("이미 등록된 회원입니다.")
        self.members[member.name] = member

    def borrow_book(self, member_name: str, isbn: str) -> None:
        if member_name not in self.members:
            raise e.MemberNotFound(f"{member_name}님은 도서관 회원이 아닙니다, 회원가입을 먼저 진행해 주세요.")
        if isbn not in self.books:
            raise e.BookNotExistsError(f"{isbn}은 잘못입력하셨거나, 도서관에 존재하는 책의 ISBN이 아닙니다. 다시 입력해 주세요.")

        this_member = self.members[member_name]
        this_book = self.books[isbn]

        if this_book.is_borrowed:
            raise e.BookAlreadyBorrowed("늦었다 후후...")

        this_book.is_borrowed = True
        this_member.borrowed_book.append(isbn)
        """
        마지막 append(isbn)> 초기책 리스트에 있는 책이 추가가 안되고(DuplicateBookError) 똑같은책이 없다는게 이 프로그램의 가정? 이기 때문에 문제 없는데..
        같은 책이 여러권 있고, 똑같은 책을 여러권 빌릴 수 있다고 생각하면 이렇게 구현했으면 안될 것 같음... 
        """

    def list_books(self) -> list[Book]:
        return list(self.books.values())

    def return_book(self, member_name :str, isbn: str) -> None:
        if member_name not in self.members:
            raise e.MemberNotFound(f"{member_name}님은 도서관 회원이 아닙니다, 회원가입을 먼저 진행해 주세요.")
        if isbn not in self.books:
            raise e.BookNotExistsError(f"입력하신 ISBN : {isbn}은 잘못입력하셨거나, 도서관에 존재하는 책의 ISBN이 아닙니다. 다시 입력해 주세요.")
        if isbn not in self.members[member_name].borrowed_book:
            raise e.BookNotBorrowedByMember(f"{member_name}님께서 빌리신 책이 아닙니다.")
        if not self.books[isbn].is_borrowed:
            raise e.BookNotBorrowed(f"ISBN : {isbn} 은 대여중인 책이 아닙니다.")
        self.books[isbn].is_borrowed = False
        self.members[member_name].borrowed_book.remove(isbn)

    def search_books(self, title : str) -> list[Book]:
        title = title.lower()
        return [b for b in self.books.values() if title in b.title.lower()]