import peewee as pw
from models.Base import Base
from abstra.widgets.response_types import PhoneResponse

class PhoneField(pw.CharField):
    def db_value(self, value: PhoneResponse):
        return value.masked

    def python_value(self, masked: str):
        raw = ''.join([c for c in masked if c.isdigit()])
        response = PhoneResponse(
            masked=masked,
            raw=raw,
            country_code=raw[:2],
            national_number=raw[2:])
        return response

class Customer(Base):
    name = pw.CharField()
    ein = pw.CharField()
    email = pw.CharField()
    phone = PhoneField()
    country = pw.CharField()
    zip = pw.CharField()
    address = pw.CharField()
