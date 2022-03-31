from flask import session

from databases import Database


def get_db_name(prefix: str) -> str:
    """Function that will return a database name with the user type prefix_type. Also make sure the database exist
    User has to be logged in!"""
    database_name = f'{prefix}_{session["type"]}'
    Database.create(database_name, {}, replace=False)  # make sure it will exists
    return database_name