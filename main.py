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


class Teacher(Model):
    teach_name = CharField()
    teach_email = CharField()
    teach_password = CharField()

    class Meta:
        database = db

Teacher.create_table(fail_silently=True)


class Products(Model):
    prod_price = IntegerField()
    prod_quantity = IntegerField()
    prod_description = CharField()
    prod_colour = CharField()

    class Meta:
        database = db


Products.create_table(fail_silently=True)




