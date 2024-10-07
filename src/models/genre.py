from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway
from models.model import StringField

class Genre(TableDataGateway, ActiveRecord):

	def __init__(self, name: str):
		self.__name = StringField(name)
	

	def get_name(self):
		return self.__name
	
	def set_name(self, name: str):
		self.__name = StringField(name)

		