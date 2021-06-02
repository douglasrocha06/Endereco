import pymysql.cursors
import pymysql
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'api_clientes'
app.config['MYSQL_DATABASE_HOST'] = 'djlbanco.cxycaymkd24m.us-east-1.rds.amazonaws.com'
mysql.init_app(app)