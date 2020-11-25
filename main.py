import requests
import googlemaps
import logging
import time
import json
import pandas
import sys
import geocoder
from flask import Flask
app = Flask(__name__)


@app.route('/')
def apig():
    geocode_result=geocoder.ip('1600 Amphitheatre Parkway,CA')
    print(geocode_result.latlng)
    return 'helo'
    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
