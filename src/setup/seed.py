from api.db import db
from models.Customer import Customer


def run():
    db.create_tables([Customer])