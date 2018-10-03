from flask_sqlalchemy import SQLAlchemy
from scipy.misc import imread, imsave, imresize

import os
import base64

mimir_storage = '/srv/mimir'

MEDIA_STORAGE_PATH = f'{ mimir_storage }/media'
MODEL_STORAGE_PATH = f'{ mimir_storage }/models'

IMAGE_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'image')
VIDEO_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'video')
CHUNK_STORAGE_PATH = os.path.join(MEDIA_STORAGE_PATH, 'chunk')

if not os.path.exists(IMAGE_STORAGE_PATH):
    os.makedirs(IMAGE_STORAGE_PATH)
    
if not os.path.exists(VIDEO_STORAGE_PATH):
    os.makedirs(VIDEO_STORAGE_PATH)
    
if not os.path.exists(CHUNK_STORAGE_PATH):
    os.makedirs(CHUNK_STORAGE_PATH)
    
if not os.path.exists(MODEL_STORAGE_PATH):
    os.makedirs(MODEL_STORAGE_PATH)

db = SQLAlchemy()

class NeuralNet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    dataset_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    model_file = db.Column(db.LargeBinary)
    class_file = db.Column(db.LargeBinary)
    submission_id = db.Column(db.String(80))

    @classmethod
    def create(cls, model_file):
        
        image = cls()
        
        db.session.add(image)
        db.session.flush()

        image.name = file_name
        image_name = f'{ image.id }_{ image.name }'
        
        image_path = os.path.join(IMAGE_STORAGE_PATH, image_name)
        thumb_path = os.path.join(IMAGE_STORAGE_PATH, 'thumb_' + image_name)

        image.source = image_path

        with open(image.source, 'wb+') as f:
            f.write(file_object.read())

        imsave(thumb_path, imresize(imread(image.source), (100, 100)))

        db.session.add(image)
        db.session.commit()

    @classmethod
    def activate(cls, model_id):
        active_model = cls.query.filter_by(active=True).first()
        requested_model = cls.query.get(model_id)
        
        active_model.active = False
        requested_model.active = True

        db.session.commit()

    @classmethod
    def get_active(cls):
        active_model = cls.query.filter_by(active=True).first()


class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    source = db.Column(db.String(80))
    class_label = db.Column(db.String(80))
    class_index = db.Column(db.Integer)
    prediction = db.Column(db.Float)

    @classmethod
    def get(cls, image_id):
        return cls.query.get(image_id)

    @classmethod
    def create(cls, file_object, file_name):

        image = cls()
        
        db.session.add(image)
        db.session.flush()

        image.name = file_name
        image_name = f'{ image.id }_{ image.name }'
        
        image_path = os.path.join(IMAGE_STORAGE_PATH, image_name)
        thumb_path = os.path.join(IMAGE_STORAGE_PATH, 'thumb_' + image_name)

        image.source = image_path

        with open(image.source, 'wb+') as f:
            f.write(file_object.read())

        imsave(thumb_path, imresize(imread(image.source), (100, 100)))

        db.session.add(image)
        db.session.commit()

    @classmethod
    def load(cls, image_id, as_type='np_array', as_thumb=False):

        image = Image.get(image_id)
        path = image.thumb if as_thumb else image.source

        if as_type == 'np_array':
            return imread(path)

        if as_type == 'base_64':
            with open(path, 'rb') as f:
                return base64.b64encode(f.read()).decode('UTF-8')

        if as_type == 'string':
            with open(path, 'rb') as f:
                return f.read()

        raise NotImplementedError(f'Support for { as_type } is currenlty not supported!')

    @classmethod
    def load_all(cls, as_type='np_array', as_thumb=False):
        return [ 
            Image.load(image.id, as_type, as_thumb) 
            for image in Image.query.all()
        ]

class ClassActivationMap():
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    path = db.Column(db.String(255))
    target_layer = db.Column(db.Integer)
    target_class = db.Column(db.Integer)

    def create(self, file_object, image_id, layer_id, class_id):

        self.image_id = image_id
        self.target_layer = layer_id
        self.target_class = class_id

        self.name = f'cam_{ layer_id }_{ class_id }'

        image = Image.get(image_id)

        with open(f'{ image.source }_{ self.name }', 'wb+') as f:
            f.write(file_object.read())

        db.session.add(self)
        db.session.commit()
    
    def load(self, image_id, layer_id, class_id):
        
        image = self.query.get(image_id)
        path = image.thumb if as_thumb else image.source

        if as_type == 'np_array':
            return imread(path)

        if as_type == 'base_64':
            with open(path, 'rb') as f:
                return base64.b64encode(f.read()).decode('UTF-8')

        if as_type == 'string':
            with open(path, 'rb') as f:
                return f.read()

        raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')

    def get(self, image_id, layer_id, class_id):
        pass
    
    def remove(self):
        pass

class SaliencyMap():
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    path = db.Column(db.String(255))
    target_layer = db.Column(db.Integer)
    target_class = db.Column(db.Integer)

    def create(self, file_object, image_id, layer_id):
        self.image_id = image_id
        self.target_layer = layer_id

        image = Image.get(image_id)

        with open(f'{ image.source }_sal', 'wb+') as f:
            f.write(file_object.read())

        db.session.add(self)
        db.session.commit()

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))

    def create(self, chunked=False):
        pass

    def add_chunk(self):
        pass
        