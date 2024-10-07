from config import ORMManager

from models.book import Book
from models.author import Author

from schemas.library import SCHEMA as LIBRARY_SCHEMA

from patterns.datamapper import DataMapper

DEF_DB_PATH = "../databases/library.db"





if __name__ == "__main__":
	
	# in order to start a new connection to the database we initialize
	# an ORM manager
	manager = ORMManager(database=DEF_DB_PATH)
	manager.open()
	
	# we can create a new Book Model instance by using the constructor
	book = Book(title="The Lord of the Rings", ISBN="DKSKDS", page_count=112, publication_date=None)

	# we can modify instance's attributes
	# model's tester methods will verify the constraints defined in the class
	book.page_count = 5
	book.title = "Harry Potter"

	# author = Author(username="J. K. Rowling")


	# we can print model's attributes in neat way
	print(book.__str__())

	# we can store or remote the book instance from the database by using ActiveRecord API
	book.save()
	book.delete()

	# alternatively we can use DataMapper's API to save/update/delete an istance
	DataMapper.save(model=book)
	DataMapper.delete(model=book)


	# here we close the connection
	manager.close()
	
