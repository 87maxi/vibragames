
from models.user import User, db

from flask import  render_template, redirect, url_for
from flask import request
from pprint import pprint




def index():
    users = User.query.all()

    return render_template("index.html",  users=users )
    


def create():

    if request.method == 'POST':


        user = User(name=request.form.get('name'),
                    password=request.form.get('password'),
                    email=request.form.get('email'),
                    apellido=request.form.get('apellido'),
                    birthdate=request.form.get('birthdate')
                    )
        db.session.add(user)
        db.session.commit()


        return redirect(url_for('blueprint.index'))
    

    



def edit():
    
    pass