from sqlalchemy import create_engine

from src.db.database import Database

class Mysql(Database):
    def get_engine(self, host, port, username, password, database):
        return create_engine(f'mysql://{username}:{password}@{host}:{port}/{database}')
