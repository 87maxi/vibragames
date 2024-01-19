
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


# Api list elements #

## list elements ##
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/api/v1

## create element ##

curl -i -H 'Content-Type: application/json' -d '{"name":"asdfasdf", "apellido":"paredes100", "email":"lkj@123.net123","birthdate":"2022-01-15", "password":"adsfasdfasdf"  }' -X POST  http://127.0.0.1:5000/api/v1/

## delete element ##

curl -i -H 'Content-Type: application/json' -d '{"id":"6"}' -X POST  http://127.0.0.1:5000/api/v1/delete

