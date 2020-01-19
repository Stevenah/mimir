import os
import flask
import uuid
import base64

from models import Image
from database import db

mod = flask.Blueprint("upload", __name__, url_prefix="/api/images")

uploads_dir = "./uploads"

@mod.route("/", methods=[ "GET", "POST" ])
def route_images():

    response = {
        "status": 400,
        "success": False
    }
    
    print(flask.request.method)

    if flask.request.method == "POST":

        image = Image()

        raw_file = flask.request.files[ "imagefile" ]
        filetype = raw_file.filename.split('.')[-1]

        image.name = "%s.%s" % (uuid.uuid4(), filetype)
        image.path = "%s/%s" % (uploads_dir, image.name)
        image.thumbnail = "%s/thumbnail_%s" % (uploads_dir, image.name)

        with open(image.path, "wb+") as f:
            f.write(raw_file.read())

        db.session.add(image)
        db.session.commit()
        
        response[ "success" ] = True
        response[ "status" ] = 200

    if flask.request.method == "GET":
        
        images = []
        thumbnail = False

        for image in Image.query.all():
            
            with open(image.thumbnail if thumbnail else image.path, "rb") as f:
                image_base64 = base64.b64encode(f.read()).decode("UTF-8")

            images.append({
                "id": image.id,
                "source": image_base64
            })

        response[ "payload" ] = images
        response[ "status" ] = 200
        response[ "success" ] = True

    return flask.json.jsonify(response)


@mod.route("/images/<image_id>", methods=[ "GET", "DELETE" ])
def route_image(image_id):
    
    response = {
        "status": 400,
        "success": False
    }
    
    if flask.request.method == "GET":

        image = Image.query.get(image_id)

        with (image.path, "rb") as f:
            image_base64 = base64.b64encode(f.read()).decode("UTF-8")

        response[ "image" ] = image_base64
        response[ "success" ] = True
        response[ "status" ] = 200

    return flask.json.jsonify(response)