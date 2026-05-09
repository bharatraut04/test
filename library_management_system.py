class Library : 
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBooks (self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo (self):
        print(f"The library has {self.noBooks} books. The Books are :")

        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks("rich DAD poor DAD")
l1.addBooks("rich DAD poor DAD2")
l1.addBooks("rich DAD poor DAD3")
l1.showInfo()