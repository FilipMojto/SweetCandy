from typing import Literal
from pathlib import Path

from models.model import Model
from patterns.datamapper import DataMapper

import sqlite3


class ConnectionError(Exception):

	def __init__(self, message: str):
		super().__init__(message)


class ORMManager():

	def __init__(self, database: str) -> None:
		# self.__DBMS = dbms
		self.__DATABASE = database

		path = Path(self.__DATABASE)

		if not path.parent.exists():
			raise ConnectionError("Provided database path not exists!")
	

	def open(self):

		self.__connection = sqlite3.connect(database=self.__DATABASE)
		self.__cursor = self.__connection.cursor()
		Model._connection = self.__connection
		
		DataMapper._connection = self.__connection
		DataMapper._cursor = DataMapper._connection.cursor()

		

	def is_open(self):
		return self.__connection is not None and self.__cursor is not None
	

	def import_schema(self, schema: str):

		if not self.is_open():
			raise ConnectionError("Connection not open!")
		
		# Split the SCHEMA into individual SQL statements and execute each one
		statements = schema.strip().split(';')
		for statement in statements:
			if statement.strip():  # Avoid empty statements
			
				self.__cursor.execute(statement.strip())

		# self.__cur.execute(schema)
		self.__connection.commit()
	
	# we can implement this later
	
	# def register_model(self, model: Model, table: str = None):
	# 	"""_summary_

	# 	Args:
	# 		model (Model): a model instance to be registered to the ORM

	# 	Raises:
	# 		ConnectionError: is thrown when 1. precondition fails
		
	# 	Preconditions:
	# 		1. A database needs to be connected.
	# 	"""

	# 	if table is None:
	# 		table = Model.__name__.lower() + 's'




	# 	if self.__connection is None:
	# 		raise ConnectionError("Registation failed: Not connected to any database.")
	

	def close(self):
		
		if not self.is_open():
			return False

		Model._connection.close()
		Model._connection = None

		return True

		

		
		




# class ORMConfig():

# 	@staticmethod
# 	def set_DBMS(DBMS: Literal['sqlite']):
# 		Model._DBMS = DBMS

	
# 	@staticmethod
# 	def set_DB(db: str):
# 		Model._DB = db


# 	@staticmethod
# 	def connect(db: str = None):
# 		# Model._DBMS = DBMS
# 		Model._DB = db

# 		# match Model._DBMS:
# 		# 	case 'sqlite':
# 		if Model._DB is not None:
# 			path = Path(Model._DB)


# 			if not path.parent.exists():
# 				raise ConnectionError("Provided database path not exists!")
			

# 			Model._CONN = sqlite3.connect(database=Model._DB)

# 	@staticmethod
# 	def register_model(model: Model, table: str = None):
# 		"""_summary_

# 		Args:
# 			model (Model): a model instance to be registered to the ORM

# 		Raises:
# 			ConnectionError: is thrown when 1. precondition fails
		
# 		Preconditions:
# 			1. A database needs to be connected.
# 		"""

# 		if table is None:
# 			table = Model.__name__.lower() + 's'




# 		if Model._CONN is None:
# 			raise ConnectionError("Registation failed: Not connected to any database.")
		
	
		





# if __name__ == "__main__":
# 	print("DSDS")
