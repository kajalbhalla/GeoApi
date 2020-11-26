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
    api_key='AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY'
    url='https://maps.googleapis.com/maps/api/geocode/json?'
    place='AV JUAREZ 2318 405+LA PAZ+PUEBLA,+PUE+72160'
    res_ob=requests.get(url+'address='+place+'&key='+api_key)
    x=res_ob.json()
    return str(x['results'][0]['geometry']['location']['lat'])
  
    
    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
