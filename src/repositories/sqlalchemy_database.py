from app.src.db.database import Database
from app.src.repositories.database import DatabaseRepository

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

class SQLAlchemyDatabaseRepository(DatabaseRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all_tables(self):
        return self.database.metadata.tables.keys()
    
    def get_all_data(self, table_name):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.connection)
        query = select(table)
        return self.database.connection.execute(query)
    
    def get_all_data_as_dict(self, table_name):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.connection)
        query = select(table)
        return [dict(row) for row in self.database.connection.execute(query)]
