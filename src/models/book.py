from typing import Iterable
from active_record import ActiveRecord

# Example of Active Record Pattern
# This class represents Book entity from ERD diagram

class Book(ActiveRecord):
	title = ""


	# builder pattern used within a contructor
	def __init__(self,
			  ID: int = None,
			  title: str = None,
			  author: str = None,
			  genres: Iterable[str] = [],
			  publication_date: str = None,
			  page_count: int = None):
	
		
		self.__ID = ID
	
		self.__title = title
		self.__author = author
		self.__genres = genres
		self.__publication_date = publication_date
		self.__page_count = page_count

	# by returning self we can use setters for chaining initialization

	def get_ID(self):
		return self.__ID
	

	def get_title(self):
		return self.__title
	

	def set_title(self, title: str):
		self.__title = title
		return self
	
	
	def get_author(self):
		return self.__author
	

	
	def set_author(self, ID: int):
		self.__author = ID
		return self
	

	def get_genres(self):
		return self.__genres


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
	
	
	# overriding model interface
	def save():
		# implementation
		pass

	def delete():
		# implementation
		pass

	# @staticmethod
	# def find(expr):
	# 	print(str(expr))


	




	def __str__(self):
	
		string = "Book: "
		
		for attr, value in self.__dict__.items():
			attr = attr[7:]
			string += attr + "=" + str(value) + ", "

		return string

	