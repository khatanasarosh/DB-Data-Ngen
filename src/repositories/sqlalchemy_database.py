from src.db.database import Database
from src.repositories.database import DatabaseRepository

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import Identity
from sqlalchemy.sql.expression import Insert

import copy

from sqlalchemy.ext.compiler import compiles

@compiles(Insert)
def set_inserts_overriding_system_value(the_insert, compiler, **kw):
    text = compiler.visit_insert(the_insert, **kw)
    text = text.replace(") VALUES (", ") OVERRIDING SYSTEM VALUE VALUES (")
    return text

class SQLAlchemyDatabaseRepository(DatabaseRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all_tables(self):
        return self.database.metadata.tables.keys()

    def get_all_data_from_table(self, table_name):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.connection)
        query = select(table)
        return self.database.connection.execute(query)

    def get_table_schema(self, table_name):
        return self.database.metadata.tables[table_name].schema

    def drop_all_tables(self):
        self.database.metadata.drop_all(self.database.engine, checkfirst=True)

    def create_table(self, table_name, schema, metadata):
        table = Table(table_name, metadata, schema=schema)
        table.create(self.database.engine)

    def refresh_metadata(self):
        self.database.refresh_metadata()

    def insert_data_into_table(self, table_name, data):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.engine, always=False)
        self.database.connection.execute(table.insert(),data)
        self.database.connection.commit()

    def get_primary_keys(self, table_name):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.connection)
        return [column.name for column in table.primary_key]

    def get_foreign_keys(self, table_name):
        table = Table(table_name, self.database.metadata, autoload=True, autoload_with=self.database.connection)
        return [fk.parent.name for fk in table.foreign_key_constraints]
