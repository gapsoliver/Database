from peewee import *

from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "oliver.db"))


# creating our first table

class Student(Model):
    stude_name = CharField()
    stude_email = CharField()
    stude_password = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)
