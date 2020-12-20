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
    place=['CARR MEX TOLUCA 5454 DEPT 502 C+EL YAQUI+CUAJIMALPA DE MORELOS+CDMX+05320',
'CTO SAN LORENZO OTE 316 A+RDCIAL BUGAMBILIAS+PUEBLA+PUE+72580',
'Canelo 3035+Bosques del Contry+GUADALUPE+NL+67174',
'CALZ LAS ROMERIAS 93 5+COLINA DEL SUR+ALVARO OBREGON+CDMX+01430',
'NIGERIA 521+FRACC PRADERAS DE LEON+CHIHUAHUA+CHI+31313',
'AV 36 PONIENTE 3102 A+COL NUEVA AURORA+PUEBLA+PUE+72070']





    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 6
    lng1=[None] * 6
    for i in range(6):
        res_ob=requests.get(url+'address='+place[i]+'&key='+api_key)
        x=res_ob.json()
        #lat1.append(str(x['results'][0]['geometry']['location']['lat']))
        lat1[i]=str(x['results'][0]['geometry']['location']['lat'])
        lng1[i]=str(x['results'][0]['geometry']['location']['lng'])
    listToStr1 = ",LAT: \n".join([str(elem) for elem in lat1])
    listToStr2 = ",LNG: \n".join([str(ele) for ele in lng1]) 
    tryl = listToStr1+listToStr2
    return tryl

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
