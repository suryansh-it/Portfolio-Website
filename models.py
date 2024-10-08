from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Visitor(db.Model):
    __tablename__ = 'Visitor'

    visitor_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(80),   nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(80),  nullable=False)
    message = db.Column(db.String(500),  nullable=False)
    timestamp= db.Column(db.DateTime,  default=lambda: datetime.now(timezone.utc))
    # profile_data = db.Column(JSON)  # JSON column for storing arbitrary JSON data



    # def __repr__(self):
    #     return f'<Prof_data {self.name}>'

class BlogData(db.Model):
    __tablename__ = 'Blog_Data'

    blog_id = db.Column(db.Integer, primary_key=True)
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

    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text , nullable=False)
    author = db.Column(db.String(80),  nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    blog_id_no = db.Column(db.Integer, db.ForeignKey('Blog_Data.blog_id'), nullable= False) #blog_id fk references id in blog_data

class ProjectData(db.Model):
    __tablename__ = 'Project_Data'
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(80),  nullable=False)
    project_summary = db.Column(db.Text , nullable=False)
    

class AboutSection(db.Model):
    __tablename__ = 'About_Section'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

class AdminData(db.Model, UserMixin):
    __tablename__ = 'Admin_Data'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)