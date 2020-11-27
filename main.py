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
    age=[1,2,3,4,5]
    count=0
    for i in range(5):
        count=count+age[i]
    return count
    
    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
