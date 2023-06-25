from sqlalchemy import create_engine

from app.src.db.database import Database

class Postgres(Database):
    def get_engine(self, host, port, username, password, database):
        return create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
