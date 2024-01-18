from flask import Flask, render_template

from flask_migrate import Migrate

from models.user import db

app = Flask(__name__, 
            template_folder='views',
            static_folder="static"
             )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vibragames.db'

db.init_app(app)

migrate = Migrate(app, db)





@app.route("/")
def status():
    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)
    