from database import db
from point import Point

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    station_id = db.Column(db.String(80), unique=True, nullable=False)
    latest_pm_2_5 = db.Column(db.Float(), unique=True, nullable=False)
    coordinates=db.Column(Point, nullable=False)

    def __repr__(self):
        return '<Station %r>' % self.station_id
