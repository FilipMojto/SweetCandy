from typing import Iterable

from .model import Model, Field, StringField, IntegerField
from patterns.activerec import ActiveRecord
from patterns.tabledatagate import TableDataGateway, Filter

# Example of Active Record Pattern
# This class represents Book entity from ERD diagram

class BookFilter(Filter):

    # overriding where()

    def where(expr: str):
        pass


class Book(Model):
    _TABLE = "books"

    title = StringField()
    ISBN = StringField()
    author_id = IntegerField()
    publication_date = StringField()
    page_count = IntegerField()


    def test_title(self, title: str):
        # print(f"Checking title to: {title}")
        return title is not None and title and title[0].isupper()
    
        
    def test_page_count(self, count: int):
        # print(f"checking page count: {count}")
    
        return count is not None and count > 0
    
    def test_publication_date(self, date: str):
        # print("SHJHSDJSDJSD!")
        return date is not None and date
    
 
