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
def apig():
    #api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    #url="https://maps.googleapis.com/maps/api/geocode/json?"
    dt=[1,2,3,4,5]
    Input_df=pd.DataFrame(dt)
    #res_ob=requests.get(url+"address="+Input_df[0]+"&key="+api_key)
    #x=res_ob.json()
    num=Input_df.tolist()
    listToStr1 = ' '.join([str(elem) for elem in num])
    return listToStr1


    

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
