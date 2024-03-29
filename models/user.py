from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    apellido = db.Column(db.String(128))
    password = db.Column(db.Text)
    birthdate = db.Column(db.String(20))
    email = db.Column(db.String(200), nullable=False)
    