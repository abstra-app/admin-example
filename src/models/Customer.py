import peewee as pw
import api.db as db


class Customer(pw.Model):
    name = pw.CharField()
    ein = pw.CharField()
    email = pw.CharField()
    phone = pw.CharField()
    country = pw.CharField()
    zip = pw.CharField()
    address = pw.CharField()

    class Meta:
        database = db.db