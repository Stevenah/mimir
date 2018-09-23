from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NeuralNetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    model_name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)

    trained_on = db.Column(db.String(80))
    description = db.Column(db.String(255))

    model_file = db.Column(db.LargeBinary)
    weights_file = db.Column(db.LargeBinary)
    class_file = db.Column(db.LargeBinary)

    submission_id = db.Column(db.String(80))

class KerasModel(NeuralNetwork):

    def __init__(self):
        pass

class PytorchModel(NeuralNetwork):

    def __init__(self):
        pass


class Architecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    dataset_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    model_file = db.Column(db.LargeBinary)
    class_file = db.Column(db.LargeBinary)
    submission_id = db.Column(db.String(80))

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    prediction = db.Column(db.Float)
    label = db.Column(db.String(80))
    class_index = db.Column(db.Integer)
    visualizations = db.relationship('Visualization', backref='image', lazy=True)

class Visualization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'),
        nullable=False)
    name = db.Column(db.String(255))
    type=db.Column(db.String(255))
    path = db.Column(db.String(255))
    target_layer = db.Column(db.Integer)
    target_class = db.Column(db.Integer)