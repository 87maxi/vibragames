from models.user import User, db
from flask import request, jsonify
from pprint import pprint
import json 
from lib.encrypt import encript_password
import base64 
import hashlib
import bcrypt
from flask_sqlalchemy import table


def index():
    users = User.query.all()
    
    d =[]
    for u in users:  
        del u.__dict__['_sa_instance_state']
        d.append(u.__dict__)


    return jsonify( d )

    


def create():
    if request.method == 'POST':


        user = User(name=request.get_json().get('name'),
                    password= encript_password(request.get_json().get('password')),
                    email=request.get_json().get('email'),
                    apellido=request.get_json().get('apellido'),
                    birthdate=request.get_json().get('birthdate')
                    )
        

        db.session.add(user)
        db.session.commit()
        db.session.close()


def delete():
    

    if request.method == 'POST':
        user = User.query.filter_by(id=request.get_json().get('id')).first()
        db.session.delete(user)
        db.session.commit()
        db.session.close()

def get_user():    
    if request.method == 'POST':
        user = User.query.filter_by(password=encript_password( request.get_json().get('password'))).first()



    return jsonify( {'returm':  user.email } ) 

    

    




