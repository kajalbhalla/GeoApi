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
'VALLE DE SILLA 2808+VALLE DE CHAPULTEPEC+GUADALUPE+NL+67140',
'NORTE 80 A 6623+SAN PEDRO EL CHICO+GUSTAVO A MADERO+CDMX+07480',
'FLORES NOCHEBUENA 102 108+VILLA SUR FRACC+AGUASCALIENTES+AGS+20296',
'AVE DE LAS CARRETAS 120 INT 60 3+COLINA DEL SUR+ALVARO OBREGON+CDMX+01430',
'CTO VILLA MILAN 185+LA CANTERA+CELAYA+GTO+38020',
'AV 19 PONIENTE 1510 1+COL SANTIAGO+PUEBLA+PUE+72410',
'C RIO SAN JUAN 112+COL NUEVA AMERICANA+PIEDRAS NEGRAS+COA+26070']








    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 13
    lng1=[None] * 13
    for i in range(13):
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
