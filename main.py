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
    place=['SENDERO DEL CAPITEL 54+MILENIO III+QUERETARO+QRO+76060',
'C CARTAGENA 7207+FRACC PUERTA DE HIERRO+CHIHUAHUA+CHI+31207',
'CDA LA PAZ 34 DEPTO 04+ESCANDON I SECCION+MIGUEL HIDALGO+CDMX+11800',
'CLLE LUIS DAVID 23+MIXCOAC+BENITO JUAREZ+CDMX+03910',
'PASEO DE LAS GALDIOLAS 316+FRACCIONAMIENTO LA FLORIDA+NAUCALPAN DE JUAREZ+EM+53160',
'M ESCOBEDO 193 T PUERTA DEL MAR D 1006+ANAHUAC I+MIGUEL HIDALGO+CDMX+11320',
'Calle universidad de coahuila 812+villa universidad+SAN NICOLAS DE LOS GARZA+NL+66420']









    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 7
    lng1=[None] * 7
    for i in range(7):
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
