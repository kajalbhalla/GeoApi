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
    place=['AV JUAREZ 2318 405+LA PAZ+PUEBLA+PUE+72160',
'RUBEN DARIO 61 901+BOSQUES DE CHAPULTEPEC+MIGUEL HIDALGO+CDMX+11580',
'AV SAN JERONIMO 389 1102 T PALATINO+LA OTRA BANDA+ALVARO OBREGON+CDMX+01090',
'MINEROS 54+COL REAL DEL MONTE+ALVARO OBREGON+CDMX+01130',
'PASEO DE LAS FLORES MZ 22 LT 12+PARAISO CONUTRY CLUB+EMILIANO ZAPATA+MOR+62765',
'CALLE DE LA ROSA 21+AMADOR SALAZAR+YAUTEPEC+MOR+62733','Av Rodolfo Gaona ED 70 Ent B depto 104+Lomas de Sotelo ezq calle 9+MIGUEL HIDALGO+CDMX+11200']




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
