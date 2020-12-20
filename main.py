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
    place=['MONUMENTO A LA REVOLUCION 154+METROPOLITANA 2A SECC+NEZAHUALCOYOTL+EM+57740',
'AV LOMAS DEL RIO PONIENTE 64+LOMAS DEL RIO+NAUCALPAN DE JUAREZ+EM+53830',
'HA DE SANTIAGO NO 17+PRADOS DEL ROSARIO+AZCAPOTZALCO+CDMX+02410',
'RMA 803+ZONA CENTRO+DOCTOR GONZALEZ+NL+66750',
'RANCHO SAN MATEO 102+SANTA CECILIA+COYOACAN+CDMX+04930',
'2A CDA DEL DEPORTE 24  7+JESUS DEL MONTE+HUIXQUILUCAN+EM+52764','JOSE RODRIGUEZ 29+OBRERO CAMPESINA+XALAPA+VER+91020']









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
