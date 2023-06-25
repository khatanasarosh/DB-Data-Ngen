# let's make database connection factory class.

# Path: app/src/factories/db_connection.py

from app.src.db.postgres import Postgres
from app.src.db.mysql import Mysql
from app.src.db.mariadb import MariaDB
from app.src.exceptions.invalid_db_type import InvalidDBType

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

