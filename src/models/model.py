from abc import ABC, ABCMeta
from sqlite3 import Connection

from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway, Filter

class ModelNotMappedException(Exception):
    def __init__(self, message: str = "Model instance not mapped to any database!") -> None:
        self.message = message
        super().__init__(self.message)


class IllegalModelState(Exception):
    def __init__(self, message: str = "Record's state invalid!"):
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




class AutoInitMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        # Get static attributes and their types

        # for k, v in attrs.items():
        #     if k == "__annotations__":
        #         for j, l in v.items():
        #             if issubclass(str, l):
        #                 print(j, l)
        # print(attrs.items())
        # print(attrs.items())
        # static_attributes = {a: c for a, c in attrs['__annotations__'].items() if issubclass(c, DataAttribute)}
        # print(static_attributes)

        # static_attributes = {k: v for k, v in attrs.items() if not k.startswith('__') and not callable(v)}
        # print(static_attributes)

        static_attributes = {}

        # Create an __init__ method dynamically
        def __init__(self, **kwargs):
            for attr, value in static_attributes.items():
                # Set instance variables based on class attributes
                setattr(self, attr, kwargs.get(attr, value))

                
        
        # Add the __init__ method to the class
        attrs['__init__'] = __init__
        
        return super().__new__(cls, name, bases, attrs)




# Create a common metaclass that combines all behaviors
# class CommonMeta(AutoInitMeta, ActiveRecordMeta, TableDataGatewayMeta):
#     pass


class Model(ActiveRecord, TableDataGateway, metaclass=AutoInitMeta):
# class Model(ABC):
    _connection: Connection = None
    _TABLE: str = None

    def __init__(self):
        super().__init__()

        if Model._connection is None:
            raise ModelNotMappedException()

        self._cur = Model._connection.cursor()

        self.__ID: int = None
        self.__fields = {}

        # Automatically create instance variables from class-level attributes
        self._initialize_attributes()

    def _initialize_attributes(self):
        # Iterate over all class-level attributes
        print(self.__class__.__dict__.items())

        for name, value in self.__class__.__dict__.items():
            if isinstance(value, DataAttribute):
                # Set an instance variable with a single underscore prefix
                setattr(self, f"_{name}", value)
                self.__fields[name] = value.data

    # def _collect_fields(self):
    #     for key, value in self.__dict__.items():
    #         if isinstance(value, DataAttribute):
    #             if key.startswith('_') and '__' in key:
    #                 key = key.split('__', 1)[1]
    #             self.__fields[key] = value.data

    def is_saved(self):
        return self.__ID is not None

    def fields(self):
        return self.__fields
    
    def get_ID(self):
        return self.__ID
    

    # table data gateway API

    @staticmethod
    def where() -> Filter:
        pass


    @staticmethod
    def delete() -> Filter:
        pass


    # active record API

    def save(self):
    
        # here we extract all DataAttributes defined in the model
        # fields = {}
        # for key, value in self.__dict__.items():
        # 	# Check if the attribute is a DataAttribute or its subclass
        # 	if isinstance(value, DataAttribute):
        # 		# Remove name-mangling for class-specific private attributes
        # 		if key.startswith('_') and '__' in key:
        # 			key = key.split('__', 1)[1]
                
        # 		# Add the attribute to the fields dictionary
        # 		fields[key] = value.data

        fields = self.fields()

        if not fields:
            raise IllegalModelState("No fields to insert or update")

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
            raise IllegalModelState(message="Cannot delete record: Not stored in a database!")
        
        delete_query = f"""
            DELETE FROM {self._TABLE} WHERE id = ?
        """

        self._cur.execute(delete_query, (self.__ID,))
        self._cur.connection.commit()

    # @classmethod
    # def get_field_names(cls):
    #     # Return the annotations (field names) from the constructor
        
    #     return list(cls.__init__.__annotations__.keys())





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

