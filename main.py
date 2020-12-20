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
    place=['FTE DE HADAS 9 2+LOMAS DE TECAMACHALCO+HUIXQUILUCAN+EM+52780',
'AV MARINA NAL 60 TORRE CAPRI+DEPTO 1801 TACUBA+MIGUEL HIDALGO+CDMX+11410',
'CAPRICORNIO 55+IZCALLI STA CLARA+ECATEPEC DE MORELOS+EM+55238',
'ITALIA 3000+DEL CARMEN+MONTERREY+NL+64710',
'CTO VALLE DEL CAUCASO 2972+COL VALLE ALTO+CULIACAN+SIN+80050',
'AVE JUAREZ 5107+POPULAR+CHIHUAHUA+CHI+31040',
'FTE DE LOS MURMULLOS 42+LOMAS DE LAS PALMAS+HUIXQUILUCAN+EM+52788',
'CONTRALORES 18+SIFON+IZTAPALAPA+CDMX+09400']









    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 8
    lng1=[None] * 8
    for i in range(8):
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
