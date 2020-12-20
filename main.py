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
    place=['CERRADA DE ATLAMAYA 11+COL ATLAMAYA+ALVARO OBREGON+CDMX+01080',
'CLAVEL 35 11+SAN JERONIMO LIDICE+LA MAGDALENA CONTRERAS+CDMX+10200',
'BALCONES 19471+OTAY GALERIAS+TIJUANA+BCN+22436',
'CIRCUITO DEL MAR ORIENTE 102+FRACC TIERRA RESIDENCIAL COL LA MAGDALE+ZAPOPAN+JAL+45200',
'CIENFUEGOS 720+LINDAVISTA+GUSTAVO A MADERO+CDMX+07300',
'2 CDA DE VAZCO DE QUIROGA 44+LOMAS DE SANTA FE+ALVARO OBREGON+CDMX+01219']











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
