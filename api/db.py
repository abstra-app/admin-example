from peewee import SqliteDatabase, PostgresqlDatabase
import os

connection_string = os.environ.get("DATABASE_URL", "sqlite://example.sqlite")

if connection_string.startswith("sqlite"):
    db = SqliteDatabase(connection_string.replace("sqlite://", ""))
else:
    db = PostgresqlDatabase(connection_string)

db.connect()
