from models.model import Model, DataAttribute

class IllegalRecordState(Exception):
	def __init__(self, message: str = "Record's state invalid!"):
		self.message = message
		super().__init__(self.message)



class ActiveRecord(Model):

	# public interface for all active records

	def __init__(self):
		super().__init__()
		
		
		



	def save(self):
	
		# here we extract all DataAttributes defined in the model
		fields = {}
		for key, value in self.__dict__.items():
			# Check if the attribute is a DataAttribute or its subclass
			if isinstance(value, DataAttribute):
				# Remove name-mangling for class-specific private attributes
				if key.startswith('_') and '__' in key:
					key = key.split('__', 1)[1]
				
				# Add the attribute to the fields dictionary
				fields[key] = value.data


		if not fields:
			raise ValueError("No fields to insert or update")

		if not self.is_saved():
			# Insert logic if ID is None
			placeholders = ', '.join(['?'] * len(fields)) 
			columns = ', '.join(fields.keys())
			values = list(fields.values())

			# print(self._TABLE)
			# print(columns)
			
			insert_query = f"INSERT INTO {self._TABLE} ({columns}) VALUES ({placeholders})"
		
			self._cur.execute(insert_query, values)

			# Sets the ID after inserting (assuming autoincrement)
			self.__ID = self._cur.lastrowid 
			
			
		else:
			# Update logic if ID exists
			set_clause = ', '.join([f"{key} = ?" for key in fields.keys()])  # Create SET part of the query
			values = list(fields.values())  # Values to set
			values.append(self.__ID)  # Append ID for the WHERE clause

			update_query = f"UPDATE {Model._TABLE} SET {set_clause} WHERE id = ?"
			self._cur.execute(update_query, values)
		
		# Commit the transaction to save changes
		self._cur.connection.commit()



	def delete(self):
		if self.__ID is None:
			raise IllegalRecordState(message="Cannot delete record: Not stored in a database!")
		
		delete_query = f"""
			DELETE FROM {self._TABLE} WHERE id = ?
		"""

		self._cur.execute(delete_query, (self.__ID,))
		self._cur.connection.commit()

