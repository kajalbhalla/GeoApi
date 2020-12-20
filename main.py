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
    place=['PROL JARDINES DE ACACIA 2386+JARDINES DE SANTA TERESA+CHAPULTEPEC+EM+52244',
'AV CUAUHTEMOC 741 6+NARVARTE PONIENTE+BENITO JUAREZ+CDMX+03020',
'CLL MARIANO ESCOBEDO 15+CENTRO+TEQUIXQUIAC+EM+55650',
'PASEO DE LAS HIGERAS 194+PASEOS DE TAXQUENA+COYOACAN+CDMX+04250',
'MISION DE COYAME 6110+FRACC EL CAMPANARIO+CHIHUAHUA+CHI+31213',
'ACUEDUCTO 465+EL LECHUGAL+SANTA CATARINA+NL+66350',
'MARACAIBO 2922 INTERIOR 4+COLOMOS PROVIDENCIA+GUADALAJARA+JAL+44660']





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
