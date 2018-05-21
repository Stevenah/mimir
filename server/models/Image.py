from database import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    prediction = db.Column(db.Float)
    label = db.Column(db.String(80))
    class_index = db.Column(db.Integer)
    visualizations = db.relationship('Visualization', backref='image', lazy=True)