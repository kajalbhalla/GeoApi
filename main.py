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
    place=['VALLE DEL SONORA 19+VALLE DE ARAGON 3RA SECCION PO+ECATEPEC DE MORELOS+EM+55280',
'RUBEN DARIO 15+DELEGACION ALVARO OBREGON+ALVARO OBREGON+CDMX+01260',
'CJON DEL PUENTE 5+FRACC RINCON DE BELLAVISTA+ATIZAPAN DE ZARAGOZA+EM+52990',
'SENDERO DE LOS LAURELES 62+PUERTA DE HIERRO+ZAPOPAN+JAL+45116',
'JINETES 5 INT B+HACIENDA DE CRISTO+NAUCALPAN DE JUAREZ+EM+53138',
'Paseo Mirador 417+Miravalle+SAN LUIS POTOSI+SLP+78214',
'SUPER MANZANA 1 MANZANA 60 LOTE 5+UNIDH B EJTO CONSTITUCIONALES+IZTAPALAPA+CDMX+09220',
'CAPULIN 1372+COLONIA DEL FRESNO+GUADALAJARA+JAL+44900']









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
