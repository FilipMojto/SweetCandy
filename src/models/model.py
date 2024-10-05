from abc import ABC
from sqlite3 import Connection

class ModelNotMappedException(Exception):
	def __init__(self, message: str = "Model instance not mapped to any database!") -> None:
		self.message = message
		super().__init__(self.message)


class DataAttribute:
	
	def __init__(self, data: object):
		self.data = data


class StringAttribute(DataAttribute):
	
	def __init__(self, data: str):
		super().__init__(data=data)


		if data is not None and not isinstance(data, str):
			raise TypeError("Provided data must be a string!")


class IntegerAttribute(DataAttribute):
	def __init__(self, data: int):
		super().__init__(data=data)

		if data is not None and not isinstance(data, int):
			raise TypeError("Provided data must be a integer!")
		

class FloatAttribute(DataAttribute):
	def __init__(self, data: float):
		super().__init__(data=data)

		if data is not None and not isinstance(data, float):
			raise TypeError("Provided data must be a float!")


	






class Model(ABC):
	# DB = 

	# _DBMS: Literal['sqlite'] = None


	# _DB: str = None
	_connection: Connection  = None

	# _TABLE: str = None

	def __init__(self):
		super().__init__()

		if Model._connection is None:
			
			raise ModelNotMappedException()
		
	
		self._cur = Model._connection.cursor()

		
		# this implies that the record is not part of a database
		# must not be modified by user!
		self.__ID = None
	
	def is_saved(self):
		return self.__ID is not None
	




	# def set_DBMS(self, DBMS: Literal['sqlite']):
	# 	Model.__DBMS = DBMS

	# def set_conn(self, conn):
	# 	Model.__conn = conn

	# def save(self):
	# 	# Prepare data for insertion or update
	# 	fields = {key[7:]: value for key, value in self.__dict__.items() if not key.startswith('_')}  # Strip private prefixes
		
	# 	if self.__ID is None:
	# 		# Insert logic if ID is None
	# 		placeholders = ', '.join(['?'] * len(fields))  # Placeholder for values
	# 		columns = ', '.join(fields.keys())  # Join column names
	# 		values = list(fields.values())  # Corresponding values

	# 		insert_query = f"INSERT INTO Book ({columns}) VALUES ({placeholders})"
	# 		self._cursor.execute(insert_query, values)

	# 		# Set the ID after inserting (assuming autoincrement)
	# 		self.__ID = self._cursor.lastrowid  # Get last inserted ID
			
	# 	else:
	# 		# Update logic if ID exists
	# 		set_clause = ', '.join([f"{key} = ?" for key in fields.keys()])  # Create SET part of the query
	# 		values = list(fields.values())  # Values to set
	# 		values.append(self.__ID)  # Append ID for the WHERE clause

	# 		update_query = f"UPDATE Book SET {set_clause} WHERE id = ?"
	# 		self._cursor.execute(update_query, values)
		
	# 	# Commit the transaction to save changes
	# 	self._cursor.connection.commit()





	
	

	
	
	# def __init__(self, ):
	# 	pass

