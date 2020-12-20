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
    place=['CTO SAN LORENZO OTE 316 A+RDCIAL BUGAMBILIAS+PUEBLA+PUE+72580',
'Canelo 3035+Bosques del Contry+GUADALUPE+NL+67174',
'CALZ LAS ROMERIAS 93 5+COLINA DEL SUR+ALVARO OBREGON+CDMX+01430',
'NIGERIA 521+FRACC PRADERAS DE LEON+CHIHUAHUA+CHI+31313',
'AV 36 PONIENTE 3102 A+COL NUEVA AURORA+PUEBLA+PUE+72070',
'GUILLERMO MASSIEU H 96 CASA 17+LA ESCALERA+GUSTAVO A MADERO+CDMX+07320',
'PROL JARDINES DE ACACIA 2386+JARDINES DE SANTA TERESA+CHAPULTEPEC+EM+52244',
'AV CUAUHTEMOC 741 6+NARVARTE PONIENTE+BENITO JUAREZ+CDMX+03020',
'CLL MARIANO ESCOBEDO 15+CENTRO+TEQUIXQUIAC+EM+55650',
'PASEO DE LAS HIGERAS 194+PASEOS DE TAXQUENA+COYOACAN+CDMX+04250',
'MISION DE COYAME 6110+FRACC EL CAMPANARIO+CHIHUAHUA+CHI+31213',
'ACUEDUCTO 465+EL LECHUGAL+SANTA CATARINA+NL+66350',
'MARACAIBO 2922 INTERIOR 4+COLOMOS PROVIDENCIA+GUADALAJARA+JAL+44660',
'SENDERO DEL CAPITEL 54+MILENIO III+QUERETARO+QRO+76060',
'C CARTAGENA 7207+FRACC PUERTA DE HIERRO+CHIHUAHUA+CHI+31207',
'CDA LA PAZ 34 DEPTO 04+ESCANDON I SECCION+MIGUEL HIDALGO+CDMX+11800',
'CLLE LUIS DAVID 23+MIXCOAC+BENITO JUAREZ+CDMX+03910',
'PASEO DE LAS GALDIOLAS 316+FRACCIONAMIENTO LA FLORIDA+NAUCALPAN DE JUAREZ+EM+53160',
'M ESCOBEDO 193 T PUERTA DEL MAR D 1006+ANAHUAC I+MIGUEL HIDALGO+CDMX+11320',
'Calle universidad de coahuila 812+villa universidad+SAN NICOLAS DE LOS GARZA+NL+66420']








    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 20
    lng1=[None] * 20
    for i in range(20):
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
