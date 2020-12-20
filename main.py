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
    place=['CALZ LA VIRGEN 3000 36 16+UH CULHUACAN STUNAM+COYOACAN+CDMX+04908',
'XOCHICALCO 39 4DEP 02+NARVARTE+BENITO JUAREZ+CDMX+03020',
'MAYASA 1968+COLOMOS PROVIDENCIA+GUADALAJARA+JAL+44660',
'CLL ADOLFO LUIS CORTINEZ NO 9+COL PROGRESISTA+IZTAPALAPA+CDMX+09240',
'AGRONOMOS 404 INT 5D+TECNOLOGICO+MONTERREY+NL+64700',
'C MALAGA 205+FRACC VINEDOS+DELICIAS+CHI+33068',
'CLL RAFAELA LOPEZ DE RAYON 121+BUROCRATA+QUERETARO+QRO+76070',
'AV OJO DE AGUA 36 A+CENTRO+PENJAMO+GTO+36900',
'CAMPO TRES BRAZOS 29+AMPL SAN ANTONIO+AZCAPOTZALCO+CDMX+02720',
'5 F POR 44 Y 46 394+RESIDENCIAL PENSIONES+MERIDA+YUC+97219']









    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 10
    lng1=[None] * 10
    for i in range(10):
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
