from app import app
from app.models import Category
from flask_script import Manager

manager = Manager(app)

@manager.command
def savecategory():
    category = Category(name = "at home")
    category.save()

if __name__ == '__main__':
    manager.run()