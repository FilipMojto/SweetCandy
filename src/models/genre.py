from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway
from models.model import StringAttribute

class Genre(TableDataGateway, ActiveRecord):

	def __init__(self, name: str):
		self.__name = StringAttribute(name)
	

	def get_name(self):
		return self.__name
	
	def set_name(self, name: str):
		self.__name = StringAttribute(name)

		