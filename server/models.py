from flask_sqlalchemy import SQLAlchemy
from scipy.misc import imread, imsave, imresize

import os
import base64

MEDIA_STORAGE_PATH = '/srv/mimir/media'
IMAGE_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'image')
VIDEO_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'video')
CHUNK_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'chunk')

MODEL_STORAGE_PATH = '/srv/mimir/models'

os.makedirs(IMAGE_STORAGE_PATH)
os.makedirs(VIDEO_STORAGE_PATH)
os.makedirs(CHUNK_STORAGE_PATH)
os.makedirs(MODEL_STORAGE_PATH)

db = SQLAlchemy()

class KerasModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    dataset_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    model_file = db.Column(db.LargeBinary)
    class_file = db.Column(db.LargeBinary)
    submission_id = db.Column(db.String(80))

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))

    def create(self, chunked=False):
        pass

    def add_chunk(self):
        pass
        
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    prediction = db.Column(db.Float)
    label = db.Column(db.String(80))
    class_index = db.Column(db.Integer)
    visualizations = db.relationship('Visualization', backref='image', lazy=True)

    @classmethod
    def create(self, file_object, file_name):
        
        if getattr(self, 'id', None) is None:
            db.session.add(self)
            db.session.flush()

        self.name = file_name

        image_name = f'{self.id}_{self.name}'
        
        image_path = os.path.join(IMAGE_STORAGE_PATH, image_name)
        thumb_path = os.path.join(IMAGE_STORAGE_PATH, 'thumb_' + image_name)

        self.path = image_path
        self.thumb = thumb_path

        with open(self.path, 'wb+') as f:
            f.write(file_object.read())

        imsave(self.thumb, imresize(imread(self.path), (100, 100)))

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(self, image_id, as_type='string', as_thumb=False):

        image = self.query.get(image_id)
        path = image.thumb if as_thumb else image.path

        if as_type == 'np_array':
            return imread(path)

        if as_type == 'base_64':
            with open(path, 'rb') as f:
                return base64.b64encode(f.read()).decode('UTF-8')

        if as_type == 'string':
            with open(path, 'rb') as f:
                return f.read()

        raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')

    @classmethod
    def remove(self):
        pass

    @classmethod
    def update(self, image_id):
        pass

    @classmethod
    def all(self, as_thumb=False):
        images = self.query.all()
        return images

class Visualization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    name = db.Column(db.String(255))
    type=db.Column(db.String(255))
    path = db.Column(db.String(255))
    target_layer = db.Column(db.Integer)
    target_class = db.Column(db.Integer)