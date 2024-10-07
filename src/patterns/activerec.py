# from models.model import Model, DataAttribute, IllegalModelState
from abc import ABC
# class IllegalModelState(Exception):
# 	def __init__(self, message: str = "Record's state invalid!"):
# 		self.message = message
# 		super().__init__(self.message)



class ActiveRecord(ABC):

	# public interface for all active records

	def __init__(self):
		super().__init__()
		


	def save(self):
		pass
	


	def delete(self):
		pass
