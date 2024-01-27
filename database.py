from flask import Flask
from flaskext.mysql import MySQL

db = Flask(__name__)
database = MySQL()

db.config['MYSQL_DATABASE_USER'] = 'root'
db.config['MYSQL_DATABASE_PASSWORD'] = ''
db.config['MYSQL_DATABASE_DB'] = 'web'
db.config['MYSQL_DATABASE_HOST'] = 'localhost'
