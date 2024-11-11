  #Book class with attributes for title, author, and year published.
# The class includes a method to return a formatted description of the book.

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_description(self):
        """Returns a formatted string describing the book."""
        return f"{self.title} by {self.author}, published in {self.year_published}"
    
    
    
# function to sort books by year published
def sorted_books_by_year(books):
   

#checking if the list is empty
   if not books:
      print("The book list is empty")
      return[]
   
# check if all the items in the list are in the Book object
   for book in books:
      if not isinstance (book, Book):
         raise ValueError("All items in the list must be in the Book object")

   return sorted(books,key=lambda book: book.year_published)
      
# sample books in the list   
book1 = Book("Things Fall Apart","Chinuwe Achebe", 2002)
book2 = Book("Straw Dogs","Micheal Pitty", 2015)
book3 = Book("Crowal","Dunk Walter", 2023)
book4 = Book("Sheild", "Quack Mathew", 2007)

books=[book1,book2,book3]

sorted_books = sorted_books_by_year(books)

# Display books using the for loop

for book in sorted_books:
   print(book.get_description())

# search Functionality
def search_books(books):
   while True:
#Enter book title
     book_title = input("\n Enter Book title ( or type 'exit' to) :   ")
     if book_title.lower() =="exit":
        print("Exiting search")
        break
     
# search for the book title
     found = False
     for book in books:
        if book.title.lower() == book_title.lower():
           print("Book found", book.get_description())
           found = True
           break
     
     if not found:
        print("Book does not exit")

# searh function start again

search_books(sorted_books)


           
           
           




     








