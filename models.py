from datetime import datetime

from config import db, ma


# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Student(db.Model):
    __tablename__ = "students"
    sid = db.Column(db.Integer, primary_key=True)
    enrolled = db.Column(db.Boolean, default=True)
    name = db.Column(db.String(32))
    classs = db.Column(db.String(32))
    age = db.Column(db.Integer)
    des = db.Column(db.String(32))
    fd = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True
