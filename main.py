import requests
import logging
import time
import json
import pandas
import sys
from flask import Flask
app = Flask(__name__)


@app.route('/')
def apig():
    """Return a friendly HTTP greeting."""
    api_key='AIzaSyD9zIRT7YEXqFmHsxUEN4U18BLZYeW4hY'
    url='https://maps.googleapis.com/maps/api/geocode/json?'
    place='Dehradun'
    res_ob=requests.get(url+'address ='+place+'&key='+api_key)
    x=res_ob.json()
    return x


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
