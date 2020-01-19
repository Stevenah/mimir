from database import db

class NeuralNetwork(db.Model):

    # Unique ID of Neural Network
    id = db.Column(db.Integer, primary_key=True)

    # Name of Neural Network
    model_name = db.Column(db.String(80), nullable=False)

    # Flag for if Neural Network is currently active
    active = db.Column(db.Boolean, default=False, nullable=False)

    # URL to Neural Netwrk API
    url = db.Column(db.String(2048))

    