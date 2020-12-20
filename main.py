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
    place=['PASEO LOS JARDINES 27 6+PASEOS DE TAXQUENA+COYOACAN+CDMX+04250',
'MELCHOR OCAMPO 238 7+CUAHUTEMOC+CUAUHTEMOC+CDMX+06500',
'PROVIDENCIA 1521+DEL VALLE CENTRO+BENITO JUAREZ+CDMX+03100',
'CALLE RETORNO 67 NO 12+AVANTE+COYOACAN+CDMX+04460',
'AV JARDIN SAN MATEO 95 23+SANTA CRUZ ACATLAN+NAUCALPAN DE JUAREZ+EM+53150',
'GRACIANO SANCHEZ M173 L23+SANTA MARTHA ACATITLA+IZTAPALAPA+CDMX+09510',
'BOULEVARD LUIS DONALDO COLOSIO SM 305+MZ01 LT3 02 U P JAGUARES INTERIOR 9+BENITO JUAREZ+QR+77560',
'CALLE ROBLES 529+COLONIA EL EZQUIVEL+TLAJOMULCO DE ZUNIGA+JAL+45640',
'AV 606 NUM 92+UHAB SN JUAN DE ARAGON 3S+GUSTAVO A MADERO+CDMX+07970',
'HACIENDA CARLOME 121+ECHEGARAY+NAUCALPAN DE JUAREZ+EM+53300',
'AV CANADA DE MARICHES NUM 303+CANADA REFUGIO+LEON+GTO+37358',
'CALLE 11 19+UHAB STA CRUZ MEYEHUALCO+IZTAPALAPA+CDMX+09290']










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
