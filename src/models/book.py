from typing import Iterable

from .model import Model, DataAttribute, StringAttribute, IntegerAttribute
from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway, Filter

# Example of Active Record Pattern
# This class represents Book entity from ERD diagram

class BookFilter(Filter):

	# overriding where()

	def where(expr: str):
		pass


class Book(Model):
	title = ""

	


	# table data gateway API

	# @staticmethod
	# def find() -> :
	_TABLE = "books"






	# builder pattern used within a contructor
	def __init__(self,
			#   ID: int = None,
			  title: str = None,
			  ISBN: str = None,
			  author_id: int = None,
			#   genres: Iterable[str] = [],
			  publication_date: str = None,
			  page_count: int = None):

		super().__init__()
		# self.__ID = ID
		
		# print(f"Title: {title}")
		self.__title = StringAttribute(title)
		self.__ISBN = StringAttribute(ISBN)
		self.__author_id = IntegerAttribute(author_id)
		# self.__genres = genres
		self.__publication_date = DataAttribute(publication_date)
		self.__page_count = IntegerAttribute(page_count)
		self.__haha = IntegerAttribute(5)

		# self._collect_fields()

	

	# by returning self we can use setters for chaining initialization

	def get_ID(self):
		return self.__ID
	

	def get_title(self):
		return self.__title
	

	def set_title(self, title: str):
		self.__title = title
		return self
	
	
	def get_author(self):
		return self.__author_id
	

	
	def set_author(self, ID: int):
		self.__author = ID
		return self
	

	def get_genres(self):
		pass
		# return self.__genres


	def get_publication_date(self):
		return self.__publication_date


	def set_publication_date(self, date: str):
		self.__publication_date = date
		return self
	
	
	
	def get_page_count(self):
		return self.__page_count

	def set_page_count(self, count: int):
		self.__page_count = count
		return self
	
	
	# # overriding model interface
	# def save(self):

	# 	self._cursor.execute("""
	# 		INSERT INTO 

	# 	""")
	# 	# implementation
	# 	pass

	# def delete(self):
	# 	# implementation
	# 	pass

	# @staticmethod
	# def find(expr):
	# 	print(str(expr))


	




	def __str__(self):
	
		string = "Book: "
		
		for attr, value in self.__dict__.items():
			attr = attr[7:]
			string += attr + "=" + str(value) + ", "

		return string


# from patterns.datamapper import DataMapper

# class BookMapper(DataMapper):

# 	@staticmethod
# 	def 