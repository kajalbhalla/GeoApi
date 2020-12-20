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
    place=['EJIDO DEL SAUZ 217+MONTE BLANCO B+CELAYA+GTO+38099',
'AV SANTA FE NUM 546+DEPTO 25 C+CUAJIMALPA DE MORELOS+CDMX+05348',
'SANTIAGO 46+SAN MARCOS RESIDENCIAL+HERMOSILLO+SON+83170',
'JUAN C DORIA NORTE 1017+MORELOS+VICTORIA+TAM+87050',
'BAHIA DE SAN IGNACIO 183 DEPTO 2+FRACC INDEPENDENCIA+AHOME+SIN+81245',
'LAGO D ZUMPANGO 137+DESARROLLO SN PABLO 5+QUERETARO+QRO+76130',
'TURQUEZA 160 COTO 3+BONANZA RESIDENCIAL+TLAJOMULCO DE ZUNIGA+JAL+45645']









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
