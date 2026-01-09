import csv
from pathlib import Path
from models import Book

class BookRepository:
    def  load_book(self) -> list[Book]:
        raise   NotImplementedError

class CsvBookRepository(BookRepository):
    def __init__(self, csv_path: Path):
        self.csv_path = csv_path

    def load_book(self) -> list[Book]:
        books : list[Book] = []
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                if len(row) < 3:
                    continue
                title = row[0].strip()
                author = row[1].strip()
                isbn = row[2].strip()
                if not isbn:
                    continue
                books.append(Book(title=title, author=author, isbn=isbn))
        return books

