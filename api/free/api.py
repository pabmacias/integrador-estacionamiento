import logging
import json
from flask.views import MethodView
from flask import jsonify, request, abort
from free.free import get_all_free_places

class FreeAPI(MethodView):
    logger = logging.getLogger(__name__)

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

    def get(self):
        parking = request.args.get("parking")
        places = get_all_free_places(parking)
        return jsonify(places), 200

    def post(self):
        data = request.json
        self.logger.info("########## Places Called")
        self.logger.info(data)

        res = get_all_free_places()

        return jsonify(res), 201
