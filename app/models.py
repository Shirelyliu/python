from app import db
import datetime
from flask_mongoengine.wtf import model_form
#
class Todolist(db.Document):
    id = db.IntField()
    title = db.StringField()
    category = db.StringField()
    leve = db.StringField()
    address = db.StringField()
    deadline = db.DateTimeField(default = datetime.datetime.now())
    description = db.StringField()
    status = db.IntField(default=0)

class Category(db.Document):
    id = db.IntField()
    name = db.StringField(required=True,max_length=20)

CategoryForm = model_form(Category)

class Level(db.Document):
    id = db.IntField()
    name = db.StringField()

class Address(db.Document):
    id = db.IntField()
    name = db.StringField()