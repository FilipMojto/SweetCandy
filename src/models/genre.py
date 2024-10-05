from patterns.active_record import ActiveRecord
from patterns.table_data_gateway import TableDataGateway
from models.model import StringAttribute

class Genre(TableDataGateway, ActiveRecord):

	def __init__(self, name: str):
		self.__name = StringAttribute(name)
	

	def get_name(self):
		return self.__name
	
	def set_name(self, name: str):
		self.__name = StringAttribute(name)
		
		