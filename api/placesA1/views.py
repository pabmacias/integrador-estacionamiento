from flask import Blueprint
from placesA1.api import PlacesA1API

placesA1_app = Blueprint('placesA1_app', __name__)

placesA1_view = PlacesA1API.as_view('placesA1_api')
placesA1_app.add_url_rule('/placesA1/',
                          view_func=placesA1_view,
                          methods=['GET'])
placesA1_app.add_url_rule('/placesA1/get_placesA1',
                          view_func=placesA1_view,
                          methods=['POST'])
