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
    place=['OVIEDO 1+FRACCIONAMIENTO VISTA ESMERALDA+ATIZAPAN DE ZARAGOZA+EM+52930',
'COLOMBIA 301 A+COL AMERICAS+TOLUCA+EM+50130',
'CDA SAN FERNANDO 4+FRACC REFORMA AGUA AZUL+PUEBLA+PUE+72430',
'RIO GUADALQUIVIR 6 502+CUAUHTEMOC+CUAUHTEMOC+CDMX+06500',
'L DA VINCI 33 103+MIXCOAC+BENITO JUAREZ+CDMX+03910',
'PORFIRIO DIAZ 136 B+SAN MATEO TLALTENANGO+CUAJIMALPA DE MORELOS+CDMX+05600',
'CALLE 28 100+CENTRO+CARMEN+CAM+24100',
'16 DE SEPTIEMBRE 34+SAUCILLO+MINERAL DE LA REFORMA+HGO+42186',
'SAN MIGUEL 206 EXT A+LLANITO+AGUASCALIENTES+AGS+20240',
'AV 508 193+SN JUAN DE ARAGON 2A SECC+GUSTAVO A MADERO+CDMX+07969',
'4TA PRIVADA DE ROCIOS 305+VILLA DE LAS FLORES+COACALCO DE BERRIOZABAL+EM+55710',
'ALAMO PLATEADO 496BI+LOS ALAMOS+NAUCALPAN DE JUAREZ+EM+53230']









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
