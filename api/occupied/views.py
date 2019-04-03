from flask import Blueprint
from occupied.api import OccupiedAPI

occupied_app = Blueprint('occupied_app', __name__)

occupied_view = OccupiedAPI.as_view('occupied_api')
occupied_app.add_url_rule('/occupied/',
                          view_func=occupied_view,
                          methods=['GET'])
occupied_app.add_url_rule('/occupied/get_occupied',
                          view_func=occupied_view,
                          methods=['POST'])
