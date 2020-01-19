import flask
import os

from models import NeuralNetwork
from database import db

mod = flask.Blueprint("nn", __name__, url_prefix="/api/cnn")

@mod.route("/models", methods=["GET"])
def models():

    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":

        models = NeuralNetwork.query.all()

        response["models"] = [
            { 
                "id": model.id,
                "model": model.model_name,
                "dataset": model.dataset_name 
            } 
            for model in models
        ]
        response["success"] = True
        response["status"] = 200

    return flask.json.jsonify(response)

@mod.route("/active", methods=["GET"])
def active():

    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":

        model = NeuralNetwork.query.filter_by(active=True).first()

        response["model"] = {
            "name": model.model_name,
            "id": model.id
        } 

        response["success"] = True
        response["status"] = 200

    return flask.json.jsonify(response)

@mod.route("/activate/<model_id>", methods=["POST"])
def activate(model_id):

    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "POST":
        
        current_active_model = NeuralNetwork.query.filter_by(active=True).first()
        waiting_active_model = NeuralNetwork.query.filter_by(id=model_id).first()

        current_active_model.active = False
        waiting_active_model.active = True

        db.session.add(active_model)
        db.session.add(model)
        db.session.commit()

        response["success"] = True
        response["status"] = 200

    return flask.json.jsonify(response)
    
@mod.route("/available", methods=["GET"])
def available():

    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":
        response["status"] = 200

    return flask.json.jsonify(response)

@mod.route("/layers", methods=["GET"])
def layers():
    
    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":
        response["layers"] = {"0": "layer_1", "1": "layer_2"}

    return flask.json.jsonify(response)

@mod.route("/classes", methods=["GET"])
def classes():
    
    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":
        response["payload"] = {"0": "class_1", "1": "class_2" }

    return flask.json.jsonify(response)

@mod.route("/classify/<image_id>", methods=["GET"])
def classify(image_id):

    response = {
        "status": 400,
        "payload": {}
    }
    
    if flask.request.method == "GET":

        model = NeuralNetwork.query.filter_by(active=True).first()
        image = Image.query.get(image_id)

        api_response = requests.post(
            url="%s/predict" % model.url,
            files={
                "file": open(image.path, "rb")
            }
        )

        response["payload"] = json.loads(api_response.text)
        response["success"] = True
        response["status"] = 200

    return flask.json.jsonify(response)

@mod.route("/visualize/<image_id>", methods=["GET", "DELETE"])
def visualize(image_id):
    
    response = {
        "status": 400,
        "success": False
    }

    if flask.request.method == "GET":

        model = NeuralNetwork.query.filter_by(active=True).first()
        image = Image.query.get(image_id)

        layer_id = flask.request.args.get("layerId", "0")
        class_id = flask.request.args.get("classId", "0")

        api_response = requests.post(
            url="%s/explain" % model.url,
            files={
                "file": open(image.path, "rb")
            }
        )

        response["payload"] = json.loads(api_response.text)
        response["success"] = True
        response["status"] = 200

    return flask.json.jsonify(response)
