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
    place=['5 F POR 44 Y 46 394+RESIDENCIAL PENSIONES+MERIDA+YUC+97219',
'MINORCA 43+LAS GRANJAS+HERMOSILLO+SON+83250',
'HUETZIN 4 INT 2+COL SANTA ISABEL TOLA+GUSTAVO A MADERO+CDMX+07010',
'C IGNACIO CENTENO 133+ZONA DE ORO I+CELAYA+GTO+38020',
'CARACOLES 24 SM 501 M 16 L3+SM 501 PARAISO REAL+BENITO JUAREZ+QR+77533',
'CARR MEX TOLUCA 5454 DEPT 502 C+EL YAQUI+CUAJIMALPA DE MORELOS+CDMX+05320',
'CTO SAN LORENZO OTE 316 A+RDCIAL BUGAMBILIAS+PUEBLA+PUE+72580',
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
'MARACAIBO 2922 INTERIOR 4+COLOMOS PROVIDENCIA+GUADALAJARA+JAL+44660']











    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 19
    lng1=[None] * 19
    for i in range(19):
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
