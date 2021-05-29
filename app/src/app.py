from flask import Flask, request, jsonify
from database import db
from models import Station, Measurement
import stations
from sqlalchemy.dialects.mysql import insert


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysqldb/stations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/get-stations")
def get_stations():
    radius = request.args.get('radius')
    coordinates = request.args.get('coordinates').split(',')
    date=request.args.get('date')

    statement = """SELECT s.*, m.value, m.type, m.recorded_at,
        ST_Distance(ST_GeomFromText('POINT({0} {1})', 4326), coordinates, "kilometre") as distance
        FROM station s
        LEFT JOIN measurement m ON s.station_id = m.station_id
        WHERE DATE(m.recorded_at) = :date
        HAVING distance <= :radius;""".format(coordinates[0], coordinates[1])

    result = db.session.execute(statement, {'radius': radius, 'date': date})

    output = []

    for row in result:
        output.append({
            'id': row['id'],
            'name': row['name'],
            'station_id': row['station_id'],
            'type': row['type'],
            'value': row['value'],
            'recorded_at': row['recorded_at'],
        })

    return jsonify(output)

@app.cli.command('initdb')
def db_init():
    db.create_all()
    
@app.cli.command('update-stations')
def update_stations():
    stations_list = stations.get()
    station_table = Station.__table__
    measurement_table = Measurement.__table__

    for station in stations_list:
        station_data = {
            'name': station['label'],
            'station_id': station['serial_number'],
            'coordinates': 'POINT({0} {1})'.format(
                        station['latitude'], station['longitude']),
        }
        station_insert = insert(station_table).values(station_data).on_duplicate_key_update(station_data)
        db.session.execute(station_insert)
        
        latest_pm_2_5 = station['latest_reading']['pm2_5'] if station['latest_reading'] else None
        
        if (latest_pm_2_5): 
            measurement_data = {
                'value': latest_pm_2_5,
                'type': 'latest_pm_2_5',
                'station_id': station['serial_number'],
                'recorded_at': station['latest_reading']['recorded_at']
            }
            measurement_insert = insert(measurement_table).values(
                measurement_data)
            db.session.execute(measurement_insert)
    
    db.session.commit()
    return 'ok'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)