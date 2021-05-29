from database import db
from point import Point
from sqlalchemy import ForeignKey

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    station_id = db.Column(db.String(80), unique=True, nullable=False)
    coordinates=db.Column(Point, nullable=False)

    def __repr__(self):
        return '<Station %r>' % self.station_id

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float())
    type = db.Column(db.String(80))
    recorded_at = db.Column(db.DateTime)
    station_id = db.Column(
        db.String(80), ForeignKey('station.station_id'), unique=True, nullable=False)

    def __repr__(self):
        return '<Measurement %r>' % self.station_id