import googlemaps
import pandas as pd
from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    gmaps=googlemaps.Client(key="AIzaSyD9zIRT7YEXqFmHsxUEN4U18BLZYeW4hY")
    return gmaps.geocode('1600 Amphitheatre Parkway,CA')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
