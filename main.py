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
'2A CDA DEL DEPORTE 24 7+JESUS DEL MONTE+HUIXQUILUCAN+EM+52764',
'JOSE RODRIGUEZ 29+OBRERO CAMPESINA+XALAPA+VER+91020',
'FTE DE HADAS 9 2+LOMAS DE TECAMACHALCO+HUIXQUILUCAN+EM+52780',
'AV MARINA NAL 60 TORRE CAPRI+DEPTO 1801 TACUBA+MIGUEL HIDALGO+CDMX+11410',
'CAPRICORNIO 55+IZCALLI STA CLARA+ECATEPEC DE MORELOS+EM+55238',
'ITALIA 3000+DEL CARMEN+MONTERREY+NL+64710',
'CTO VALLE DEL CAUCASO 2972+COL VALLE ALTO+CULIACAN+SIN+80050',
'AVE JUAREZ 5107+POPULAR+CHIHUAHUA+CHI+31040',
'FTE DE LOS MURMULLOS 42+LOMAS DE LAS PALMAS+HUIXQUILUCAN+EM+52788',
'CONTRALORES 18+SIFON+IZTAPALAPA+CDMX+09400',
'PRIV LUIS GOMEZ Z 32+FERROCARRILERA+URUAPAN+MICH+60150',
'HOLBEIN 51 T 302+SAN JUAN+BENITO JUAREZ+CDMX+03730',
'FUENTE DEL MIRADOR 12+LOMAS DE TECAMACHALCO SEC FUENTES+NAUCALPAN DE JUAREZ+EM+53950',
'AV CAMPO REAL 1621 INT 2 5+FRACC EL REFUGIO+QUERETARO+QRO+76146',
'HACIENDA MOLINITO 126+BALCONES DEL CAMPESTRE+LEON+GTO+37138',
'AV CANAL DE GARAY 2A 20 1A+TRIANGULO DE LAS AGUJAS+IZTAPALAPA+CDMX+09885',
'AV CENTENARIO 2761 DEPTO 402 TORRE B+BOSQUES DE TARANGO+ALVARO OBREGON+CDMX+01580',
'MONEDITA DE ORO 26+BENITO JUAREZ+NEZAHUALCOYOTL+EM+57000',
'RINCONADA DE BEJAR 1733+COL LAS ALAMEDAS+ZAPOPAN+JAL+45079',
'CONCEPCION BEISTEGUI 206 INT 503+DEL VALLE+BENITO JUAREZ+CDMX+03103']





    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 25
    lng1=[None] * 25
    for i in range(25):
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
