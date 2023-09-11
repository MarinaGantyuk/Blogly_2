"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

def connect_db(app):
    db.init_app(app)    
    
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, default = 'blankuseravatar.png')

class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default = datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    
