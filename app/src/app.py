from flask import Flask
from database import db
import stations
from models import Station


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysqldb/stations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.cli.command('initdb')
def db_init():
    db.create_all()
    
@app.cli.command('update-stations')
def db_init():
    return stations.get()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)