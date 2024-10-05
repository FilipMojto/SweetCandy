from config import ORMManager

from models.book import Book
from models.author import Author

from schemas.library import SCHEMA as LIBRARY_SCHEMA

DEF_DB_PATH = "../databases/library.db"



if __name__ == "__main__":



	manager = ORMManager(database=DEF_DB_PATH)
	manager.open()

	manager.import_schema(schema=LIBRARY_SCHEMA)




	book = Book(
			 title="Harry Potter and Philospher's Stone",
			 ISBN="978-3-16-148410-12",
			author_id=3,
			publication_date='2021-05-12',
			page_count=314)

	book.save()

	
	# here we use builder pattern's chaning feature
	book = Book(page_count=423)
	book.set_title("The Lord of the Rings: The Fellowship of the Ring").set_author("J.R.R. Tolkien")
	

	manager.close()
	
