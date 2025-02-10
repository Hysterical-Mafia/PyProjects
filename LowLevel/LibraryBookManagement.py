#Library Book Management System

'''
-Add new books
    ask user for book details, date, title, author
    store details in dictionary
    append dictionary to the list of books
-View All Books
    loop throught the list and display each book and its details
'''

library = []

def main():
    add_book()
        
        
def add_book():
    for _ in range(1):
        book_title = input("Enter the following \nTitle: ")
        book_author = input("Author: ")
        book_date = int(input("Date: "))
        book = {"book title": book_title, "author": book_author, "date": book_date}  
        library.append(book)
        again = input("Would you like to add another book? Yes or No: ").lower() 
        if again == "yes":
            add_book()  
        else:
            for book in library:
                print(f"""
                      Ok, here are your books:
                      Book Name: {book['book title']}
                      Author: {book['author']}
                      Date: {book['date']}
                      """)
            
main()

