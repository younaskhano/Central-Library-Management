class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks    

    
    def displayAvailableBooks(self):
        print("The books present in this library are:" )
        for book in self.books:
            print("*"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} Please keep it safe and retur it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or has already been issued to someone else. Please wait until the book is available.")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book, Hope you enjoyed reading this!")
          

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return/add: ")
        return self.book                                                                                  



if __name__== "__main__":
    libraryDetails = ["Algorithms","Python Notes","Django","Programming Book: "]
    centralLibrary = Library(libraryDetails)
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''====== Welcome to central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return/Add a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library. Have a great day ahead!")
            exit()
        else:
            print("Invalid choice")
        



    

    


