import requests
import googlemaps
import logging
import time
import json
import pandas
import sys
from flask import Flask
app = Flask(__name__)


@app.route('/')
def apig():
    gmaps=googlemaps.Client(key='AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY')
    geocode_result=gmaps.geocode('1600 Amphitheatre Parkway,CA')
    print(geocode_result)
    return 'helo'
    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
