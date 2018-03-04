from flask import current_app as app

import base64
import uuid
import cv2
from scipy.misc import imsave, imread, imresize
import os


def save_image(image, file_path, as_np=False, mode='RGB'):

    dir_path = os.path.dirname(file_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if as_np:
        cv2.imwrite(file_path, image)
    else:
        with open(file_path, 'wb+') as f:
            f.write(image.read())

def load_image(file_path, as_np=False, mode='RGB'):

    if as_np:
        return cv2.imread(path)

    with open(file_path, 'rb') as f:
        return f.read()


def save_file(f, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'wb+') as destination:
        destination.write(f.read())
 
def read_image(image_id, filter_type='original'):

    base_dir = app.config[f'{filter_type.upper()}_DIRECTORY']

    file_dir = os.path.join(base_dir, image_id)
    file_name = os.listdir(file_dir)[0]
    file_path = os.path.join(file_dir, file_name)

    with open(file_path, 'rb') as f:
        return f.read(), file_name

def np_read_image(image_id, filter_type='original'):

    base_dir = app.config[f'{filter_type.upper()}_DIRECTORY']

    file_dir = os.path.join(base_dir, image_id)
    file_name = os.listdir(file_dir)[0]
    file_path = os.path.join(file_dir, file_name)

    return imread(file_path, mode='RGB')

def read_all_image(filter_type):
    for image_id in os.listdir(app.config[f'{filter_type.upper()}_DIRECTORY']):
        yield read_image(image_id, filter_type), image_id

def handle_delete(uuid):
    filepath = os.path.join(app.config['UPLOAD_DIRECTORY'], uuid)
    shutil.rmtree(filepath)

def handle_upload(form_file, form_attributes):

    chunked = False
    chunksize = None
    chunkindex = None
    chunkdir = None

    if 'qqtotalparts' in form_attributes:
        chunked = True
        chunksize = int(form_attributes['qqtotalparts'])
        chunkindex = int(form_attributes['qqpartindex'])
        chunkdir = app.config['CHUNKS_DIRECTORY']

    filepath = ''

    filename = form_attributes['qqfilename']
    fileuuid = form_attributes['qquuid']
    filedir = app.config['ORIGINAL_DIRECTORY']

    dest = os.path.join(filedir, fileuuid, filename)

    if chunked and chunksize > 1:
        dest = os.path.join(chunkdir, fileuuid, filename, str(chunkindex))

    save_file(form_file, dest)

    if chunked and (chunksize - 1 == chunkindex):

        filepath = os.path.join(filedir, fileuuid, filename)

        combine_chunks(
            chunksize=chunksize,
            source_dir=os.path.dirname(dest),
            dest=filepath)

        shutil.rmtree(os.path.dirname(os.path.dirname(dest)))
    
    return filepath

def combine_chunks(chunksize, source_dir, dest):

    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    with open(dest, 'wb+') as destination:
        for chunk_index in range(chunksize):
            chunk = os.path.join(source_dir, str(chunk_index))
            with open(chunk, 'rb') as source:
                destination.write(source.read())