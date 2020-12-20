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
    place=['Paseo de Heracles 111+Las Ceibas+BAHIA DE BANDERAS+NAY+63735',
'AV MEXICO COYOACAN 371 TA 603+XOCO+BENITO JUAREZ+CDMX+03330',
'AGATA 840+MARIANO OTERO+ZAPOPAN+JAL+45067',
'C PIRULES 5+FRACC HACIENDA TECATE O+TECATE+BCN+21400',
'SUR 16 A 31BIS CASA F+AGRICOLA ORIENTAL+IZTACALCO+CDMX+08500',
'JARDIN DE LAS BUGAMBILIAS 26+JARDINES DE CHAPALITA+ZAPOPAN+JAL+45010',
'AVE MAGDALENA CONTRERAS 385 CASA A 1+COL SAN JERONIMO LIDICE+LA MAGDALENA CONTRERAS+CDMX+10200',
'HILARIO C SALAS 28+GUADALUPE RODRIGUEZ+XALAPA+VER+91055',
'PONIENTE 145 735+MEXICO NUEVO+MIGUEL HIDALGO+CDMX+11260',
'C ISIDRO FABELA ED L DEPTO 403+U HAB VILLAS JARDIN+TULTITLAN+EM+54913',
'DE TODOS LOS SANTOS 155+STA ANA TEPETITLAN+ZAPOPAN+JAL+45230',
'Calz Lucio Blanco 385 A109+San Juan Tlihuaca+AZCAPOTZALCO+CDMX+02400']









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
