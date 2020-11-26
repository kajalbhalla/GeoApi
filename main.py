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
    place=['AV JUAREZ 2318 405+LA PAZ+PUEBLA+PUE+72160','MINEROS 54+COL REAL DEL MONTE+ALVARO OBREGON+CDMX+01130']
    lat1 = [None] * 2
    lng1 = [None] * 2
    for i in range(len(place)):
        res_ob=requests.get(url+'address='+place[i]+'&key='+api_key)
        x=res_ob.json()
        lat1[i]=str(x['results'][0]['geometry']['location']['lat'])
        lng1[i]=str(x['results'][0]['geometry']['location']['lng'])
    listToStr1 = ' '.join([str(elem) for elem in lat1])
    listToStr2 = ' '.join([str(ele) for ele in lng1]) 
    return listToStr1+listToStr2
    
    
  
    
    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
