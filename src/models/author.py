from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway

from models.model import StringAttribute

class Author(TableDataGateway, ActiveRecord):
    _TABLE = "authors"

    # Class-level attribute
    username = StringAttribute("dds")

    @property
    def username(self):
        """Getter for the username"""
        return self._username.data  # Access the dynamically created _username

    @username.setter
    def username(self, value: str):
        """Setter for the username"""
        self._username = StringAttribute(value)

    # def set_username(self, username: str = None):
    # 	if username is None:
    # 		return self._username
    # 	else:
    # 		self._username = StringAttribute(username)



    

    # def __init__(self, username: str):
    # 	super().__init__()

    # 	self.__username = StringAttribute(username)


    # def get_username(self):
    # 	return self.__username
    

        
        


