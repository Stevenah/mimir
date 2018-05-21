from database import db

class Visualization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'),
        nullable=False)
    name = db.Column(db.String(255))
    type=db.Column(db.String(255))
    path = db.Column(db.String(255))
    target_layer = db.Column(db.Integer)
    target_class = db.Column(db.Integer)