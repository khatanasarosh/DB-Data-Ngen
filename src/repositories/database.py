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

    @abstractmethod
    def drop_all_tables(self):
        pass

    @abstractmethod
    def create_table(self, table_name, schema, metadata):
        pass
    

    @abstractmethod
    def refresh_metadata(self):
        pass
    
    @abstractmethod
    def insert_data_into_table(self, table_name, data):
        pass

    @abstractmethod
    def get_primary_keys(self, table_name):
        pass

    @abstractmethod
    def get_foreign_keys(self, table_name):
        pass
