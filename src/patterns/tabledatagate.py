from abc import ABC, abstractmethod
from typing import List, Literal

from sqlite3 import Connection

class Filter[T](ABC):
	

	def __init__(self, conn: Connection, fields: List[str], op: Literal['get', 'delete']):
		self.conn = conn
		self.cur = self.conn.cursor()
		self.fields = fields
		self.operation = op
		


	# @abstractmethod
	def where(self, expr: str) -> List[T]:
		if self.operation == 'get':
			pass

		elif self.operation == 'delete':
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
	def collect(where: str) -> List:
		pass


	@staticmethod
	def delete_all(where: str) -> int:
		pass