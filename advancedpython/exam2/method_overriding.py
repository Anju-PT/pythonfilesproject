class Book:
    def setval(self,bookname,author,pages):
        self.bookname=bookname
        self.author=author
        self.pages=pages
    def print(self):
        print("Book Name::",self.bookname)
        print("Author::",self.author)
        print("Pages::",self.pages)
class Child(Book):
    def set(self,publisher):
        self.publisher=publisher
    def print(self):
        print("Publisher::",self.publisher)
        print("Book Name::",self.bookname)
        print("Author::",self.author)
        print("Pages::",self.pages)
c1=Child()
c1.setval("The world with out money","Anju P T",250)
c1.set("DC Books")
c1.print()