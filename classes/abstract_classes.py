""" File containing all of the abstract classes to make concerete classes to follow dependency inversion """
from abc import ABC, abstractmethod
import sys
sys.path.append(".") #allows modules to be discovered

class DataSource(ABC):
    """ A base class/interface for CRUD methods and connnection methods for a data source """
    
    # Usually for a data source you need details such as engine details, server name, log in etc
    """ 1.Below is an abstract method with a constructor to initialise with.
        2. This commented out because @abstractmethod makes so that concrete class has to override
        the abstract method to initialise.
        
        So this method is needed in an actual program but not within the scope of the test.
        Not commenting it out will force extra parameters/fixtures/inlinedata for testing. 
    """
    #@abstractmethod
    # def __init__(self, engine: str, name: str, password: str, db_name: str)
    # self.engine = engine
    # self.name = name
    # self.password = password
    # self.db = db
    
    @abstractmethod
    def connect(self) -> object:
        """ Connects to database and returns database object"""
        pass
    
    def close(self) -> None:
        """ closes db connection """
        pass 
        
    
     