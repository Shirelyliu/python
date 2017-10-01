from app import app
from flask import render_template,request
from models import Todolist
from models import Category
from models import Level
from models import Address
from models import CategoryForm

@app.route('/')
def category():
    form = CategoryForm()
    categorys = Category.objects.all()
    return render_template("/category.html",categorys = categorys,form = form)

@app.route('/addcategory',methods=['POST',])
def addcategory():
    form = CategoryForm(request.form)
    if form.validate():
        name = form.name
        category = Category(name = name)
        category.save()
    categorys = Category.objects.all()
    return render_template("/category.html",categorys = categorys,form = form)