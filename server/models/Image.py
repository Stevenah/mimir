from database import db

class Image(db.Model):
    
    # ID of uploaded Image
    id = db.Column(db.Integer, primary_key=True)
    
    # Path to image stored on disk
    path = db.Column(db.String(80))
    
    # Path to compressed version of Image
    thumbnail = db.Column(db.String(80))