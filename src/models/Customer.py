import peewee as pw
from models.Base import Base


class Customer(Base):
    name = pw.CharField()
    ein = pw.CharField()
    email = pw.CharField()
    phone = pw.CharField()
    country = pw.CharField()
    zip = pw.CharField()
    address = pw.CharField()
