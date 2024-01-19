from flask import Flask, render_template

from flask_migrate import Migrate

from models.user import db
from routes import blueprint
from api_routes import api_v1


app = Flask(__name__, 
            template_folder='views',
            static_folder="static"
             )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vibragames.db'

db.init_app(app)

app.register_blueprint(blueprint, url_prefix='/')

app.register_blueprint(api_v1, url_prefix='/api/v1')

migrate = Migrate(app, db)





if __name__ == "__main__":

    app.run(debug=True)
    