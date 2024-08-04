from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

db = SQLAlchemy()

class Visitor(db.Model):
    __tablename__ = 'Visitor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),   nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(80),  nullable=False)
    message = db.Column(db.String(500),  nullable=False)
    # profile_data = db.Column(JSON)  # JSON column for storing arbitrary JSON data



    # def __repr__(self):
    #     return f'<Prof_data {self.name}>'

class BlogData(db.Model):
    __tablename__ = 'Blog_Data'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),   nullable=False)
    content = db.Column(db.Text , nullable=False)
    author = db.Column(db.String(80),  nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    comments = db.relationship('CommentData', backref='blog', lazy=True) #one to many relationship

# backref='blog' : it allows you to access the blog post from a comment using comment.blog.
#lazy=True :  comments are not immediately loaded when the blog post is queried.
    #       Instead, they are loaded when the comments attribute is accessed for the first time


class CommentData(db.Model):
    __tablename__ = 'Comment_Data'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text , nullable=False)
    author = db.Column(db.String(80),  nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    blog_id = db.Column(db.Integer, db.ForeignKey('Blog_Data.id'), nullable= False) #blog_id fk references id in blog_data
