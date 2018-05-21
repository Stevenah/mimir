from database import db

class Architecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    dataset_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    model_file = db.Column(db.LargeBinary)
    class_file = db.Column(db.LargeBinary)
    submission_id = db.Column(db.String(80))
    