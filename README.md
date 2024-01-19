
# crear virtual venv #
python3.11 -m venv venv

# activar virtual venv#

source venv/bin/activate



# Install pakage #

pip install -r requirements.txt


# Commands db migrate #

flask db init

flask db migrate

flask db upgrade


# Inicializar servicio #

flask run --debug


# Aplicacion # 

http://127.0.0.1:5000
