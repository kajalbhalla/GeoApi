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
    place=['NEVADO DE TOLUCA 28+LOMAS DE OCCIPACO+NAUCALPAN DE JUAREZ+EM+53247',
'C 43 NORTE 206+AQUILES SERDAN+PUEBLA+PUE+72140',
'PASEO DE LAS BRISAS 4084+LOMAS ALTAS+ZAPOPAN+JAL+45128',
'VALLE DE JIMENEZ 195+FRACC VALLE DE ARAGON+NEZAHUALCOYOTL+EM+57100',
'PASO DE LOS TOROS 1811 109+EL REFUGIO+QUERETARO+QRO+76146',
'PUERTO JUAREZ 27+AMPL PILOTO ADOLFO LOPEZ MATEO+ALVARO OBREGON+CDMX+01290',
'VALLE DE SILLA 2808+VALLE DE CHAPULTEPEC+GUADALUPE+NL+67140']









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
