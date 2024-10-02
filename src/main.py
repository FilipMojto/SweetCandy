
from models.book import Book

if __name__ == "__main__":

	book = Book(ID=1,
			 title="Harry Potter and Philospher's Stone",
			 author="J. K. Rowling",
			 genres=['Fantasy'],
			publication_date='2021-05-12',
			page_count=314)
	
	print(book.__str__())

	
	# here we use builder pattern's chaning feature
	book = Book(ID=5, page_count=423)
	book.set_title("The Lord of the Rings: The Fellowship of the Ring").set_author("J.R.R. Tolkien")
	
	book.find(Book.title == "name")

	print(book.__str__())
	
