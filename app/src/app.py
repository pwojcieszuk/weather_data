from flask import Flask
from database import db
from models import Station
import stations
from sqlalchemy.dialects.mysql import insert


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
def update_stations():
    stations_list = stations.get()
    table = Station.__table__
    for station in stations_list:
        data = {
            'name': station['label'],
            'station_id': station['serial_number'],
            'latest_pm_2_5': station['latest_reading']['pm2_5'] if 
                station['latest_reading'] else None,
            'coordinates': 'POINT({0} {1})'.format(
                        station['latitude'], station['longitude']),
        }
        insert_stmt = insert(table).values(data).on_duplicate_key_update(data)
        db.session.execute(insert_stmt)
    db.session.commit()
    return 'ok'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)