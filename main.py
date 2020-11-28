import requests
import googlemaps
import logging
import time
import json
import pandas as pd
import sys
import geocoder
from flask import Flask
app = Flask(__name__)


@app.route('/')
def apig(Input_df):
    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    #dt={'place': [35, 70, 45, 20]} 
    #Input_df=pd.DataFrame(input)
    res_ob=requests.get(url+"address="+Input_df[0]+"&key="+api_key)
    x=res_ob.json()
    #num=Input_df['place'].tolist()
    #listToStr1 = ' '.join([str(elem) for elem in num])
    return str(x['results'][0]['geometry']['location']['lat'])+","+(str(x['results'][0]['geometry']['location']['lng']))
dt={'place': ["AV JUAREZ 2318 405+LA PAZ+PUEBLA+PUE+72160","MINEROS 54+COL REAL DEL MONTE+ALVARO OBREGON+CDMX+01130"]}
df = pd.DataFrame(dt) 
df['Lat_Long']= df(apig,axis=1)

    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
