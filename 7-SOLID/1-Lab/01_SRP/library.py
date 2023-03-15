from typing import List
from book import Book


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def find_book(self, title: str):
        for b in self.books:
            if b.title == title:
                return b

        return None
