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
    place=['PRV ZAMORA 3 2+PUEBLO SAN ANDRES TOTOLTEPEC+TLALPAN+CDMX+14400',
'JACARANDAS 301+FRACC LAS FUENTES+PIEDRAS NEGRAS+COA+26000',
'C JUAN ESCUTIA 89+COL CENTRO+SAHUAYO+MICH+59000',
'CLL 14 126+MONTECRISTO+MERIDA+YUC+97133',
'C DEL CANAL 8+EL PARAISO ATLACHOLOAYA+XOCHITEPEC+MOR+62790',
'6 DE OCTUBRE 94+PLANETARIO LINDAVISTA+GUSTAVO A MADERO+CDMX+07739',
'C INDEPENDENCIA 1240+COL CENTRO+SAN LUIS POTOSI+SLP+78000',
'AV 5 NTE C 48 Y C50 D 1 MZ 268 LT 04+LUIS DONALDO COLOSIO+SOLIDARIDAD+QR+77728',
'4TA CDA CAPRI 25+LOMAS ESTRELLA 1RA SECC+IZTAPALAPA+CDMX+09890',
'TEXTITLAN 40 EDIF A DEPTO PH 7+SANTA URSULA COAPA+COYOACAN+CDMX+04650',
'C ADMINISTRACION 112+FRACC TOLLANCINGO+TULANCINGO DE BRAVO+HGO+43648',
'CERRADA D LOS ESCRITORES 4926+FRACC PORTALEGRE+CULIACAN+SIN+80058']









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
