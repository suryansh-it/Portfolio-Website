from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Visitor(db.Model):
    __tablename__ = 'Visitors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),   nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(80),  nullable=False)
    message = db.Column(db.String(500),  nullable=False)
    # profile_data = db.Column(JSON)  # JSON column for storing arbitrary JSON data



    # def __repr__(self):
    #     return f'<Prof_data {self.name}>'