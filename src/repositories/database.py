from abc import ABC, abstractmethod

class DatabaseRepository(ABC):
    @abstractmethod
    def get_all_tables(self):
        pass
    
    @abstractmethod
    def get_all_data(self, table_name):
        pass
