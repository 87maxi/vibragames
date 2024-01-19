
from models.user import User, db

from flask import  render_template, redirect, url_for
from flask import request, jsonify

from pprint import pprint

from sqlalchemy import delete, select


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
    

def edit(id):
    user= User.query.get(id)

    d = user.__dict__
    del d['_sa_instance_state']
    return jsonify(d)


def update(id):
    User.query.filter_by(id=id).first()


def delete(idx):
    

    if request.method == 'POST':
        user = User.query.filter_by(id=idx).first()
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('blueprint.index'))