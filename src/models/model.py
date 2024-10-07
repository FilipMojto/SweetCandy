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


class ModelContraintViolation(Exception):
    def __init__(self, message: str = "Model's contraint violated") -> None:
        super().__init__(message)



class Field:
    
    def __init__(self, data: object = None):
        self.data = data


class StringField(Field):
    
    def __init__(self, data: str = None):
        super().__init__(data=data)


        if data is not None and not isinstance(data, str):
            raise TypeError("Provided data must be a string!")
    
    



class IntegerField(Field):
    def __init__(self, data: int = None):
        super().__init__(data=data)

        if data is not None and not isinstance(data, int):
            raise TypeError("Provided data must be a integer!")
        

class FloatField(Field):
    def __init__(self, data: float = None):
        super().__init__(data=data)

        if data is not None and not isinstance(data, float):
            raise TypeError("Provided data must be a float!")




class AutoInitMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        # Prepare static attributes (class-level attributes) for initialization
        static_attributes = {k: v for k, v in attrs.items() if isinstance(v, Field) or isinstance(v, property)}

        # Get the __init__ method from attrs or inherit from bases
        original_init = attrs.get('__init__')

        # If __init__ is not in attrs, look for it in base classes
        if original_init is None:
            for base in bases:
                original_init = getattr(base, '__init__', None)
                if original_init is not None:
                    break

        # Check if the current class is a subclass of Model
        if any(issubclass(base, Model) for base in bases):
            # Define a new __init__ method that wraps the original
            def __init__(self, *args, **kwargs):
                # Call the original __init__ method if it exists
                if original_init is not None:
                    # Filter out kwargs intended for Model's base class
                    model_args = {k: v for k, v in kwargs.items() if hasattr(self, f"_{k}")}

                    # Call the original init with filtered kwargs
                    original_init(self, *args, **model_args)

                # print(static_attributes)

             

                # Append static attribute initialization for fields in the child class
                for attr, field in static_attributes.items():
                    print(f"{attr}:{field}")
                    # Ensure we set the value within the Field object
                    if isinstance(field, Field):
                        field.data = kwargs.get(attr, field.data)  # Set the data of the Field instance
                    setattr(self, f"_{attr}", field)  # Preserve the Field instance itself
                    print(self.title)

                  


            # Replace the __init__ method in attrs
            attrs['__init__'] = __init__

        return super().__new__(cls, name, bases, attrs)


# Create a common metaclass that combines all behaviors
# class CommonMeta(AutoInitMeta, ActiveRecordMeta, TableDataGatewayMeta):
#     pass

class Model:
    pass

class Model(ActiveRecord, TableDataGateway, metaclass=AutoInitMeta):
    _connection: Connection = None
    _TABLE: str = None

    __models = []

 

    def __setattr__(self, name: str, value) -> None:
        # Construct the name of the setter method
        # print("chECKING setting attr")
        setter_name = f"test_{name}"

        # Check if the setter method exists in the class
        setter_method = getattr(self, setter_name, None)
        # print(setter_name)
        # If the setter method exists and is callable, call it
        # print(setter_method)
        if callable(setter_method):
            result = setter_method(value)  # Call the setter method with the value

            if result is not None and isinstance(result, bool) and not result:
                raise ModelContraintViolation(message=f"Model's contrain violated: {name}")

        
        super().__setattr__(name, value)
        # else:
        #     # Otherwise, set the attribute directly
        #     super().__setattr__(name, value)
        


    def __init__(self):
        super().__init__()

        if Model._connection is None:
            raise ModelNotMappedException()

        self._cur = Model._connection.cursor()

        self._ID: int = None  # Changed __ID to _ID (avoid name mangling)
        # self._fields = {}  # Changed __fields to _fields
        # print("INITIALIZING!")
        # Automatically create instance variables from class-level attributes
        # self._initialize_attributes()


    

    # def _collect_attributes(self):
    #     # print("INITIALIZING!")
    #     # Iterate over all class-level attributes

    #     # print(self.__class__.__dict__.items())
    #     for name, value in self.__class__.__dict__.items():
    #         if isinstance(value, Field):
    #             # Set an instance variable with a single underscore prefix
    #             setattr(self, f"_{name}", value)
    #             self._fields[name] = value.data

    def _collect_attributes(self):
        """
        Collects all attributes that are instances of the Field class 
        and returns them as a dictionary.
        """
        collected = {}

        print(self.__dict__.items())

        # Iterate over all instance variables
        for attr_name, attr_value in self.__dict__.items():
            # Check if the attribute is a Field or subclass of Field
            if isinstance(attr_value, Field):
                # Remove leading underscore from the attribute name if present
                clean_name = attr_name.lstrip('_')
                collected[clean_name] = attr_value.data  # Assuming Field has a 'data' attribute to store value

        return collected



    def is_saved(self):
        return self._ID is not None

    # def get_fields(self):
    
    #     return self._fields
    
    def __str__(self):
        # print("ErE")
        # print(vars(self))
        


        rep = self.__class__.__name__ + ": "




        for attr, value in vars(self).items():
            # print(value)
            # print(attr)
            rep += (attr + "=")
            rep += str(value.data) if isinstance(value, Field) else str(value)
            rep += ", "
        # print(rep)
        rep = rep[:-2]

        return rep

    
    def get_ID(self):
        return self._ID


    # ActiveRecord and TableDataGateway API (as before)
    @staticmethod
    def where() -> Filter:
        pass

    @staticmethod
    def delete() -> Filter:
        pass



    def save(self):
        fields = self._collect_attributes()
        print(fields)
        # print(f"Fields: {fields}")

        if not fields:
            raise IllegalModelState("No fields to insert or update")

        if not self.is_saved():
            # Insert logic
            placeholders = ', '.join(['?'] * len(fields))
            columns = ', '.join(fields.keys())

        
            values = list(fields.values())
            

            insert_query = f"INSERT INTO {self._TABLE} ({columns}) VALUES ({placeholders})"
            self._cur.execute(insert_query, values)

            # Set the ID after inserting (assuming autoincrement)
            self._ID = self._cur.lastrowid
        else:
            # Update logic
            set_clause = ', '.join([f"{key} = ?" for key in fields.keys()])
            values = list(fields.values())
            values.append(self._ID)

            update_query = f"UPDATE {self._TABLE} SET {set_clause} WHERE id = ?"
            self._cur.execute(update_query, values)

        self._cur.connection.commit()

    def delete(self):
        if self._ID is None:
            raise IllegalModelState(message="Cannot delete record: Not stored in a database!")

        delete_query = f"DELETE FROM {self._TABLE} WHERE id = ?"
        self._cur.execute(delete_query, (self._ID,))
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

