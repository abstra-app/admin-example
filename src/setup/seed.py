from api.db import db
from models.Customer import Customer

# Create the tables
db.create_tables([Customer])