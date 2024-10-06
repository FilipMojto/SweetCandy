from sqlite3 import Connection, Cursor

from models.model import Model, IllegalModelState

# import sqlite3
class DataMapper(Model):
	_connection: Connection = None
	_cursor: Cursor = None

	@staticmethod
	def save(model: Model):
		
		fields = model.fields()
		print(fields)

		if not fields:
			raise IllegalModelState("No fields to insert or update")

		if not model.is_saved():
			# Insert logic if ID is None
			placeholders = ', '.join(['?'] * len(fields)) 
			columns = ', '.join(fields.keys())
			values = list(fields.values())

			# print(self._TABLE)
			# print(columns)
			
			insert_query = f"INSERT INTO {model._TABLE} ({columns}) VALUES ({placeholders})"
		
			DataMapper._cursor.execute(insert_query, values)

			# Sets the ID after inserting (assuming autoincrement)
			model.__ID = DataMapper._cursor.lastrowid

			# self.__ID = self._cur.lastrowid 
			
			
		else:
			# Update logic if ID exists
			set_clause = ', '.join([f"{key} = ?" for key in fields.keys()])  # Create SET part of the query
			values = list(fields.values())  # Values to set
			values.append(model.get_ID())  # Append ID for the WHERE clause

			update_query = f"UPDATE {Model._TABLE} SET {set_clause} WHERE id = ?"
			DataMapper._cursor.execute(update_query, values)
			# self._cur.execute(update_query, values)
		
		# Commit the transaction to save changes
		# self._cur.connection.commit()
		DataMapper._connection.commit()



	@staticmethod
	def delete(model: Model):
		# pass

		if not model.is_saved():
			raise IllegalModelState(message="Cannot delete record: Not stored in a database!")
		
		delete_query = f"""
			DELETE FROM {model._TABLE} WHERE id = ?
		"""

		DataMapper._cursor.execute(delete_query, (model.get_ID(),))
		DataMapper._connection.commit()
