import sqlite3

conn = sqlite3.connect('sweetcandy.db')

cur = conn.cursor()

cur.execute("""
	CREATE TABLE IF NOT EXISTS books(
		id INTEGER PRIMARY KEY,
		name TEXT,
		author TEXT,
		genre TEXT,
		page_count INTEGER,
		release_year INTEGER
	)
""")


class Book:
	conn = conn
	cur = conn.cursor()
	def __init__(self, attribute1, attribute2):
		self.attribute1 = attribute1
		self.attribute2 = attribute2


	def __init__(self, ID: int = None, name: str = None, author: str = None, genre: str = None, release_year: str = None, page_count: str = None):
		# self.__id = id
		
		self.__ID = ID,
		# print(f"ID: {self.__ID}")
		self.__name = name
		self.__author = author
		self.__genre = genre
		self.__release_year = release_year
		self.__page_count = page_count

	
	def __str__(self):

		return f'Book::ID={self.__ID}, Name={self.__name}, Author={self.__author}, Genre={self.__genre}, ReleaseYear={self.__release_year}, Pages: {self.__page_count}'


	def set_name(self, name: str):
		self.__name = name

		return self

	def set_author(self, author: str):
		self.__author = author

		return self

	def set_genre(self, genre: str):
		self.__genre = genre
		return self

	def set_release_year(self, year: int):
		self.__release_year = year
		return self

	def set_page_count(self, count: int):
		self.__page_count = count
		return self
	

	def insert(self):
		cur.execute("""
			INSERT INTO books
			  
			  VALUES(?, ?, ?, ?, ?)

		""", [self.__name, self.__author, self.__genre, self.__release_year, self.__page_count])

	# def get(self):
		




	# @classmethod
	# def where():

	# 	return Book

	# @classmethod
	# def get():
	# 	pass


# without using design pattern principles the initialization may be confusing (it might be unclear which value represents which attribute)
# this problem becomes greater mainly when coding in programming languages like java, c++ or c#, but also in python (as shown in below example)
# first approach - how initialization looks in c++, java, etc., but also in Python without using Builder Pattern
book = Book("Harry Potter and Philoshoper's stone", "J. K. Rowling", "Fantasy", 1997, 315)

# python by itself provide mechanisms to add some clarity when initializing an object
book = Book(name="Harry Potter and Philoshoper's stone", author="J. K. Rowling", genre="Fantasy", release_year=1997, page_count=315)

# implementing a custom builder pattern in Python (unpractical)
book = Book().set_name("Harry Potter and Philoshoper's stone").set_author("J. K. Rowling").set_genre("Fantasy").set_release_year(1997).set_page_count(315)

print(book.__str__())

# book.insert()






conn.commit()
cur.close()
conn.close()