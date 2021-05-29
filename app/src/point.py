from sqlalchemy import func
from sqlalchemy.types import UserDefinedType

class Point(UserDefinedType):
    srid = 4326

    def get_col_spec(self):
        return "POINT"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, self.srid, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)
