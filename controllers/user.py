
from models.user import User, db
from flask import  render_template, redirect, url_for
from flask import request, jsonify
from lib.encrypt import EncrytPasswd
from pprint import pprint

def index():
    users = User.query.all()

    return render_template("index.html",  users=users )
    


def create():

    if request.method == 'POST':


        user = User(name=request.form.get('name'),
                    password= EncrytPasswd().encript_password(request.form.get('password')),
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
    d["password"] = EncrytPasswd().decript_password(d.get('password'))
    del d['_sa_instance_state']
    return jsonify(d)


def update():
    
    if request.method == 'POST':

        data= {           
            "name":request.form.get('name'),
            "password": EncrytPasswd().encript_password(request.form.get('password')),
            "email":request.form.get('email'),
            "apellido":request.form.get('apellido'),
            "birthdate":request.form.get('birthdate'),
            "id": request.form.get('id')
         }

    
    db.session.query(User).filter(User.id==request.form.get('id')).update(data)
    db.session.commit()


def delete(idx):
    

    if request.method == 'POST':
        user = User.query.filter_by(id=idx).first()
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('blueprint.index'))