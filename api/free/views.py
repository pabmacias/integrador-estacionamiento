from flask import Blueprint
from free.api import FreeAPI

free_app = Blueprint('free_app', __name__)

free_view = FreeAPI.as_view('free_api')
free_app.add_url_rule('/free/',
                          view_func=free_view,
                          methods=['GET'])
free_app.add_url_rule('/free/get_free',
                          view_func=free_view,
                          methods=['POST'])
