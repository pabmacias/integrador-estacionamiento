import logging
import json
from flask.views import MethodView
from flask import jsonify, request, abort
from placesA1.places import get_all_places
import base64
import numpy as np

class PlacesA1API(MethodView):
    logger = logging.getLogger(__name__)

    def __init__(self):
        if (request.method != 'POST') and not request.json:
            abort(400)

    def get(self):
        places = get_all_places()
        return jsonify(places), 200

    def post(self):
        nparr = np.fromstring(request.data, np.uint8)

        self.logger.info("########## PlacesA1 Called")

        res, alerts = get_all_places(nparr, 0.3, 0.3)

        return jsonify({
            "occuped": res,
            "alerts": alerts
        }), 201
