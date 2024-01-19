from models.user import User, db
from flask import request, jsonify
from pprint import pprint
import json 

def index():
    users = User.query.all()
    
    d =[]
    for u in users:  
        del u.__dict__['_sa_instance_state']
        d.append(u.__dict__)


    return jsonify( d )

    

    