from flask import Blueprint
from places.api import PlacesAPI

places_app = Blueprint('places_app', __name__)

places_view = PlacesAPI.as_view('places_api')
places_app.add_url_rule('/places/',
                          view_func=places_view,
                          methods=['GET'])
places_app.add_url_rule('/places/get_places',
                          view_func=places_view,
                          methods=['POST'])
