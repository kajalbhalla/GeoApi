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
    place=['JUAN SANCHEZ AZCONA 1322+DEL VALLE+BENITO JUAREZ+CDMX+03100',
'PRIV MAGNOLIAS 2B+SANTA PAULA+TONALA+JAL+45425',
'ESCORPIO 124+PRADO CHURUBUSCO+COYOACAN+CDMX+04230',
'PEDREGAL DE LA ENSENADA+SUR 5443+MONTERREY+NL+64898',
'SHETLAND 375+COSMOPOLITA+AZCAPOTZALCO+CDMX+02670',
'J LUIS LAGRANGE 207 701+POLANCO+MIGUEL HIDALGO+CDMX+11510',
'HUAPANGO 54+COLINAS DEL SUR+ALVARO OBREGON+CDMX+01430',
'CALLE MONTE SINAI 19 MZ 80 SMZ 310+RESIDENCIAL CUMBRES+BENITO JUAREZ+QR+77560',
'AV UNIVERSIDAD 2014 ED CUBA DEPTO 103+UNIDAD INTEGRACION LATINOAMERICANA+COYOACAN+CDMX+04350',
'AHORRO POSTAL 75 EDF A DPTO 301+COL POSTAL+BENITO JUAREZ+CDMX+03410',
'CACTUS 109+GARAMBULLO+QUERETARO+QRO+76115',
'LAMINADORES 130+TRABAJADORES DEL HIERRO+AZCAPOTZALCO+CDMX+02650']








    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 12
    lng1=[None] * 12
    for i in range(12):
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
