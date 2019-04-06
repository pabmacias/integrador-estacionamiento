import logging
import json
from flask.views import MethodView
from flask import jsonify, request, abort
from places.places import get_all_places
import base64
import numpy as np

class PlacesAPI(MethodView):
    logger = logging.getLogger(__name__)

    def __init__(self):
        if (request.method != 'POST') and not request.json:
            abort(400)

    def get(self):
        places = get_all_places()
        return jsonify(places), 200

    def post(self):
        nparr = np.fromstring(request.data, np.uint8)

        self.logger.info("########## Places Called")

        res = get_all_places(nparr, 0.5, 0.3)

        return jsonify(res), 201
