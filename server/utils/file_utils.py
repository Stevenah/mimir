from database import db
from models import Visualization

import cv2
import base64

def save_visualization(source, image_id, layer_id, class_id, viz_type, from_type='string'):

    image = Visualization()

    image.name = f'{layer_id}_{class_id}_{image_id}_{viz_type}.png'
    image.target_layer = layer_id
    image.target_class = class_id
    image.image_id = image_id
    image.type = viz_type
    image.path = f'uploads/{viz_type}/{image.name}_{image.id}_{image.name}'

    if from_type == 'np_array':
        cv2.imwrite(image.path, source)

    elif from_type == 'string':
        with open(image.path, 'wb+') as f:
            f.write(source.read())

    else:
        raise NotImplementedError(f'Support for {from_type} is currenlty not supported!')

    db.session.add(image)
    db.session.commit()

def load_visualization(image_id, layer_id, class_id, viz_type, as_type='string'):

    image = Visualization.query.filter_by(image_id=image_id, target_layer=layer_id, target_class=class_id, type=viz_type).first()

    if as_type == 'np_array':
        image = cv2.imread(image.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    if as_type == 'base_64':
        with open(image.path, 'rb') as f:
            return base64.b64encode(f.read()).decode('UTF-8')

    if as_type == 'string':
        with open(image.path, 'rb') as f:
            return f.read()

    raise NotImplementedError(f'Support for {as_type} is currenlty not supported!')
    
