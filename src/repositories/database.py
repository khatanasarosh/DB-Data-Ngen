from abc import ABC, abstractmethod

class DatabaseRepository(ABC):
    @abstractmethod
    def get_all_tables(self):
        pass
    
    @abstractmethod
    def get_all_data_from_table(self, table_name):
        pass

    @abstractmethod
    def get_table_schema(self, table_name):
        pass
