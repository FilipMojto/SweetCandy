from abc import ABC, abstractmethod
from typing import List

from sqlite3 import Connection

class Filter(ABC):
	COLS: List[str] = None

	def __init__(self, conn: Connection):
		self.conn = conn
		self.cur = self.conn.cursor()





	@abstractmethod
	def where(expr: str):
		pass




class TableDataGateway:
	pass


class TableDataGateway(ABC):

	# public API for all tables
	
	# these methods are not really required, since it is best to use save() method
	# provided by active_record

	# @staticmethod
	# def insert(object: TableDataGateway):
	# 	pass

	# @staticmethod
	# def update():
	# 	pass

	@staticmethod
	def where() -> Filter:
		pass


	@staticmethod
	def delete() -> Filter:
		pass