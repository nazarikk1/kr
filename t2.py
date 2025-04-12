from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def is_old(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def info(self):
        print("")
        print(f"⤷Book: {self.title}")
        print(" 𝗣𝗥𝗢𝗗𝗨𝗖𝗧 𝗖𝗛𝗔𝗥𝗔𝗖𝗧𝗘𝗥𝗜𝗦𝗧𝗜𝗖𝗦")
        print(f"  Author: {self.author}")
        print(f"  Year: {self.year}")
        print(f"  Pages: {self.pages}")

    def is_old(self):
        return self.year < 2000

class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number, month):
            super().__init__(title, year)
            self.issue_number = issue_number
            self.month = month

    def info(self):
            print("")
            print(f"⤷Magazine: {self.title}")
            print(" 𝗣𝗥𝗢𝗗𝗨𝗖𝗧 𝗖𝗛𝗔𝗥𝗔𝗖𝗧𝗘𝗥𝗜𝗦𝗧𝗜𝗖𝗦")
            print(f"  Issue: {self.issue_number}")
            print(f"  Month: {self.month}")
            print(f"  Year: {self.year}")

    def is_old(self):
            return self.year < 2015

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if type(item) == Book or type(item) == Magazine:
            self.items.append(item)
        else:
            raise TypeError()

    def show_all(self):
        for item in self.items:
            item.info()

    def show_old(self):
        for item in self.items:
            if item.is_old():
                item.info()

    def find_by_title(self, keyword):
        for item in self.items:
            if keyword.lower() in item.title.lower():
                item.info()

b1 = Book(title="Harry Potter and the Sorcerer's Stone", year=1997, author="J.K. Rowling", pages=309)
b2 = Book(title="The Lord of the Rings: The Fellowship of the Ring", year=1954, author="J.R.R. Tolkien", pages=423)

m1 = Magazine(title="VOGUE", year=2025, issue_number=145, month="January")
m2 = Magazine(title="VOGUE", year=2019, issue_number=144, month="December")

library = Library()
library.add_item(b1)
library.add_item(b2)
library.add_item(m1)
library.add_item(m2)

print("КАТАЛОГ БІБЛІОТЕКИ:")
library.show_all()

print("____________________")
print("СТАРИЙ ДРУК:")
library.show_old()

print(" ")
print("👀SEARCH ")
print("𝗩𝗢𝗚𝗨𝗘")
library.find_by_title("VOGUE")