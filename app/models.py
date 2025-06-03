from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Toilet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    location = db.Column(db.String(255))  # Address
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    reviews = db.relationship('Review', backref='toilet', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    toilet_id = db.Column(db.Integer, db.ForeignKey('toilet.id'), nullable=False)
    cleanliness = db.Column(db.Integer)
    safety = db.Column(db.Integer)
    smell = db.Column(db.Integer)
    comment = db.Column(db.Text)

class PoopStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    upvotes = db.Column(db.Integer, default=0)
