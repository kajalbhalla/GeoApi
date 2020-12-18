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
    place=['PRIV LUIS GOMEZ Z 32+FERROCARRILERA+URUAPAN+MICH+60150',
'HOLBEIN 51 T 302+SAN JUAN+BENITO JUAREZ+CDMX+03730',
'FUENTE DEL MIRADOR 12+LOMAS DE TECAMACHALCO SEC FUENTES+NAUCALPAN DE JUAREZ+EM+53950',
'AV CAMPO REAL 1621 INT 2 5+FRACC EL REFUGIO+QUERETARO+QRO+76146',
'HACIENDA MOLINITO 126+BALCONES DEL CAMPESTRE+LEON+GTO+37138',
'AV CANAL DE GARAY 2A 20 1A+TRIANGULO DE LAS AGUJAS+IZTAPALAPA+CDMX+09885',
'AV CENTENARIO 2761 DEPTO 402 TORRE B+BOSQUES DE TARANGO+ALVARO OBREGON+CDMX+01580',
'MONEDITA DE ORO 26+BENITO JUAREZ+NEZAHUALCOYOTL+EM+57000',
'RINCONADA DE BEJAR 1733+COL LAS ALAMEDAS+ZAPOPAN+JAL+45079']









    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 9
    lng1=[None] * 9
    for i in range(9):
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
