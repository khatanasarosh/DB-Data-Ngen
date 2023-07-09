from src.factories.database import DatabaseFactory
from src.factories.randomiser import RandomiserFactory
from src.repositories.database import DatabaseRepository
from src.repositories.sqlalchemy_database import SQLAlchemyDatabaseRepository

from copy import deepcopy

import json
import os

def main():
    source_db_factory = DatabaseFactory()

    source_db: Database = source_db_factory.get_database(os.getenv('SOURCE_DB_ENGINE'))
    source_db.connect(
        host=os.getenv('SOURCE_DB_HOST'),
        port=os.getenv('SOURCE_DB_PORT'),
        username=os.getenv('SOURCE_DB_USER'),
        password=os.getenv('SOURCE_DB_PASSWORD'),
        database=os.getenv('SOURCE_DB_DATABASE')
    )
    source_db_repo = SQLAlchemyDatabaseRepository(source_db)

    target_db_factory = DatabaseFactory()
    target_db: Database = target_db_factory.get_database(os.getenv('TARGET_DB_ENGINE'))
    target_db.connect(
        host=os.getenv('TARGET_DB_HOST'),
        port=os.getenv('TARGET_DB_PORT'),
        username=os.getenv('TARGET_DB_USER'),
        password=os.getenv('TARGET_DB_PASSWORD'),
        database=os.getenv('TARGET_DB_DATABASE')
    )

    target_db_repo= SQLAlchemyDatabaseRepository(target_db)
    target_db_repo.drop_all_tables()

    randomiser_factory = RandomiserFactory()

    for table_name in source_db_repo.get_all_tables():
        target_db_repo.create_table_without_foreign_keys(
            table_name, 
            source_db_repo.get_table_schema(table_name), 
            source_db_repo.database.metadata
        )
    
    target_db_repo.refresh_metadata()

    for table_name in source_db_repo.get_all_tables():
        constraints = source_db_repo.get_constraints_for_table(table_name)
        for constraint in constraints:
            if constraint.name == 'primary_key':
                continue
            target_db_repo.database.metadata.tables[table_name].append_constraint(deepcopy(constraint))
            target_db_repo.refresh_metadata()

    for table_name in source_db_repo.get_all_tables():
        primary_keys = source_db_repo.get_primary_keys(table_name)
        foreign_keys = source_db_repo.get_foreign_keys(table_name)

        result = source_db_repo.get_all_data_from_table(table_name)

        row_dicts = []

        if result:
            for row in result:
                row_dict = dict(row._mapping)
                for key in row_dict:
                    if key in primary_keys or key in foreign_keys:
                        continue
                    row_dict[key] = randomiser_factory.get_randomiser(row_dict[key]).randomise(row_dict[key])
                
                row_dicts.append(row_dict)
            
            if row_dicts:
                target_db_repo.insert_data_into_table(table_name, row_dicts)

    source_db.disconnect()
    target_db.disconnect()

if __name__ == '__main__':
    main()
