from src.db.postgres import Postgres
from src.db.mysql import Mysql
from src.db.mariadb import MariaDB
from src.exceptions.invalid_db_type import InvalidDBType

class DatabaseFactory:
    def __init__(self):
        pass

    def create(self, db_type):
        if db_type == 'postgresql':
            return Postgres()
        elif db_type == 'mysql':
            return Mysql()
        elif db_type == 'mariadb':
            return MariaDB()
        else:
            raise InvalidDBType('Invalid database type')

