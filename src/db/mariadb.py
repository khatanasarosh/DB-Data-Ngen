from app.src.db.database import Database

class MariaDB(Database):
    def get_engine(self, host, port, username, password, database):
        return create_engine(f'mariadb://{username}:{password}@{host}:{port}/{database}')
