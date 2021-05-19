class Book:
    def setval(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print("Library Name::",self.library_name)
        print("Book Name   ::",self.book_name)
        print("Author      ::",self.author)
        print("Pages       ::",self.pages)
b1=Book()
b1.setval("District Library","The Wings of Fire","A.P.J Abdul Kalam",228)
b1.printval()