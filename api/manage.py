import os
from application import create_app
import config

#app = create_app(config, debug=('DEBUG' in os.environ and bool(os.environ['DEBUG'])))
app = create_app(config, debug=True)
port = int(os.getenv('PORT', 5000))


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Analisis Modelo'


""" Run Configuration """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, threaded=True, debug=True)
