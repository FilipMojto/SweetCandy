from patterns.active_record import ActiveRecord
from patterns.table_data_gateway import TableDataGateway

from models.model import StringAttribute

class Author(TableDataGateway, ActiveRecord):

	_TABLE = "authors"

	def __init__(self, username: str):
		super().__init__()

		self.__username = StringAttribute(username)


	def get_username(self):
		return self.__username
	

		
		


