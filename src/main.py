from services import Services
from pathlib import Path
from models import Book, Member
from utils import prompt_str,prompt_int
from exceptions import LibraryError
from repository import CsvBookRepository


def print_menu():
    print("\n=== 도서관 관리 시스템 ===\n1. 도서 등록\n2. 도서 목록\n3. 회원 등록\n4. 대출\n5. 반납\n6. 검색\n7. 종료\n")

def main():
    library_system = Services()
    base_dir = Path(__file__).resolve().parent.parent
    csv_dir = base_dir / "data" / "books.csv"

    try:
        repo = CsvBookRepository(csv_dir)
        for book in repo.load_book():
            try:
                library_system.add_book(book)
            except LibraryError:
                pass
        print(f"{csv_dir}에서 데이터를 불러왔습니다.")
    except FileNotFoundError:
        print(f"{csv_dir}에서 데이터를 불러오지 못했습니다.")

    while True:
        print_menu()
        choice = prompt_int("번호 선택: ",range(1,8))
        try:
            if choice == 1:
                print("[도서 등록]")
                title = prompt_str("제목: ")
                author = prompt_str("저자: ")
                isbn = prompt_str("ISBN: ")
                library_system.add_book(Book(title, author, isbn))
                print(">> 도서 등록 완료")

            elif choice == 2:
                print("[도서 목록]")
                for books in library_system.list_books():
                    print(books)

            elif choice == 3:
                print("[회원 등록]")
                name = prompt_str("이름: ")
                phone = prompt_str("전화번호: ")
                library_system.add_member(Member(name, phone))
                print(">> 회원 등록 완료")

            elif choice == 4:
                print("[대출]")
                name = prompt_str("회원 이름: ")
                isbn = prompt_str("ISBN: ")
                library_system.borrow_book(name, isbn)
                print(">> 대출 완료")

            elif choice == 5:
                print("[반납]")
                name = prompt_str("회원 이름: ")
                isbn = prompt_str("ISBN: ")
                library_system.return_book(name, isbn)
                print(">> 반납 완료")

            elif choice == 6:
                print("[검색]")
                keyword = prompt_str("검색어: ")
                results = library_system.search_books(keyword)
                for b in results:
                    print(b)

            elif choice == 7:
                print("종료합니다.")
                break
        except LibraryError as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()
