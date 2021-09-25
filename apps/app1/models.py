from django.db.models import Model, CharField, IntegerField, UniqueConstraint
from django.db.models.fields import DateField, TextField
from datetime import datetime as dt


class Time:
    @property
    def today():
        return dt.now()


class Blog(Model):
    title = CharField(max_length=20)
    body = TextField()
    date_of_creation = DateField(default=dt.now)

    def __str__(self):
        return f"title: {self.title} - date:{self.date_of_creation}"

    class Meta:
        db_table = 'BLOG_TABLE'
