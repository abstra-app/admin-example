import peewee as pw
import api.db as db
import uuid
from datetime import datetime


class UUIDField(pw.UUIDField):
    def python_value(self, value):
        return str(super().python_value(value))


class Base(pw.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = pw.DateTimeField(default=datetime.now)
    updated_at = pw.DateTimeField(default=datetime.now)
    deleted_at = pw.DateTimeField(null=True)

    class Meta:
        database = db.db
