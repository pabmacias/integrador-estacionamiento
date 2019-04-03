import logging
import json
from flask.views import MethodView
from flask import jsonify, request, abort
from places.places import get_all_places
import base64

class PlacesAPI(MethodView):
    logger = logging.getLogger(__name__)

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

    def get(self):
        places = get_all_places()
        return jsonify(places), 200

    def post(self):
        data = request.json
        self.logger.info("########## Places Called")
        # self.logger.info(data)
        # decoded = base64.b64encode(data.get('image'))
        # image = base64.b64decode(json.loads(data.get('image').decode('utf-8')))
        # image = base64.b64decode(decoded)
        encoded = str.encode(data.get('image'))
        decoded = base64.b64encode(encoded)

        res = get_all_places(data.get('image'), data.get('confidence'), data.get('threshold'))

        return jsonify(res), 201
