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
    place=['BLV DE LOS REYES 6202 3+FRACC ALAMO+SAN ANDRES CHOLULA+PUE+72821',
'COYOACAN 1617 EDIF C DEPTO PB3+DEL VALLE SUR+BENITO JUAREZ+CDMX+03104',
'CDA SAN AGUSTIN 2+FRACC CAMPESTRE SAN GIL+SAN JUAN DEL RIO+QRO+76815',
'BAHIA DE ESTAMBUL 101+PASEOS DE LA CASTELLANA+LEON+GTO+37549',
'VALLE DE SANTA CATALINA 17331+FRACC VALLE DE SAN PEDRO+CHIHUAHUA+CHI+31125',
'C CONTADERO 6+BARR LA JOYA+YURIRIA+GTO+38940',
'EULOGIO ESMAURRIZAR NO 154+FRACC VALLE DE TEQUISQUIAPAN+SAN LUIS POTOSI+SLP+78238',
'AV ESC NAVAL MILIT 132 E9 D503+SN FCO CULHUACAN+COYOACAN+CDMX+04440',
'PRIV 2 DE ABRIL 1222+SAN PIO X+MONTERREY+NL+64710',
'AV PASEO DE LA REFORMA 505 PISO 28+CUAUHTEMOC+CUAUHTEMOC+CDMX+06500',
'C PLAYA LA MARQUEZA 3532+COL PRIMAVERA+MONTERREY+NL+64830',
'7A CALLE OTE 123+COL MIGUEL ALEMAN+SAN NICOLAS DE LOS GARZA+NL+66470',
'AV LIBERTAD 118 404+PEDREGAL DE CARRASCO+COYOACAN+CDMX+04700']









    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 13
    lng1=[None] * 13
    for i in range(13):
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
