from abc import ABC, abstractmethod

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

class Database(ABC):
    @abstractmethod
    def get_engine(self, host, port, username, password, database):
        pass

    def connect(self, host, port, username, password, database):
        engine = self.get_engine(host, port, username, password, database)
        self.connection = engine.connect()
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.connection)
        self.Base = automap_base(metadata=self.metadata)
        self.Base.prepare(engine, reflect=True)
        self.tables = self.Base.classes

    def disconnect(self):
        self.connection.close()
