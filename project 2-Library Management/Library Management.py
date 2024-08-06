class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self, book, user):
        if book in booklist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("book has been lended. database updated")
            else:
                print(f"book is already use by {self.lendDict[book]}")
        else:
            print("Apologies! we dont have the book in this library")

    def addbook(self, book):
        if book in booklist:
            print("book already exist")
        else:
            self.booklist.append(book)
            bookdatabase = open(databasename, "a")
            bookdatabase.write("\n")
            bookdatabase.write(book)
            print("book added")

    def returnbook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("book returned sucessfully")
        else:
            print("the book does not exist in lending database")


def main():
    while True:
        print(f"Welcome to the {library.name} library. Following are the options,")
        choice = """
        1.Display books
        2.Lend a book
        3.Add a book
        4.Return a book
        """
        print(choice)

        userInput = input("press Q to quit and C to continue: ")
        if userInput == "C":
            userChoice = int(input("Select an Option to continue:"))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input("enter the name of the book you want to lend:")
                user = input("enter the name of the user:")
                library.lendbook(book, user)

            elif userChoice == 3:
                book = input("Enter the name of the book you want to add: ")

                library.addbook(book)

            elif userChoice == 4:
                book = input("enter the name of the book you want to return: ")
                library.returnbook(book)

            else:
                print("please choose valid option")

        elif userInput == "Q":
            break
        else:
            print("please enter valid option")


if __name__ == "__main__":
    booklist = []
    databasename = input("enter the name of the database file with extension: ")
    bookdatabase = open(databasename, "r")
    for book in bookdatabase:
        booklist.append(book)
    library = Library(booklist, "pythonX")
    main()
