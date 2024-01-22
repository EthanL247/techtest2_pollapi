""" File containing all of the abstract classes to make concerete classes to follow dependency inversion """
from abc import ABC, abstractmethod
import sys
sys.path.append(".") #allows modules to be discovered

class DataSource(ABC):
    """ A base class/interface for CRUD methods and connnection methods for a data source """
    
    """Usually for a data source you need details such as engine details, server name, log in etc
     Below is an abstract method with a constructor to initialise with."""
    @abstractmethod
    def __init__(self, engine: str, name: str, password: str, db_name: str):
        self.engine = engine
        self.name = name
        self.password = password
        self.db = db
        
    @abstractmethod
    def connect(self) -> object:
        """ Connects to database and returns database object"""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """ closes db connection """
        pass 
    
    @abstractmethod
    def search(self,query)-> object:
        """ Searches within a database """ 
        pass
    

class Graph(ABC):
    """ A base class for Plotly graph implementations since I'm using interactive graphs rather than still images """
    
    @abstractmethod
    def etl(self, data)-> dict:
        """ Process json files into dicts to be used by plotly  """
        pass
    
    @abstractmethod
    def fig(self,data: dict) -> object:
        """ Process to produce the graph object"""
        pass
    
    @abstractmethod
    def export(self,fig: object) -> None:
        """ Directly inserts graph into html via Jinja2 """
        pass
        
 
    
    
        
    
     