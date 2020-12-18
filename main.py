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
    place=['CALLEJON ALIJADORES 0 114+TIERRA COLORADA+CENTRO+TAB+86029',
'LAGUNA DE MEXICANOS 2909+SAN FELIPE QUINTA ETAPA+CHIHUAHUA+CHI+31204',
'JOSE ANTONIO TORRES 626 2+VISTA ALEGRE+CUAUHTEMOC+CDMX+06860',
'INDIANA 25 D 406+NAPOLES+BENITO JUAREZ+CDMX+03810',
'Feliz 1861 MZ42 LT1 etapa 4+los treboles+ZAPOPAN+JAL+45200',
'Velicata  43 Parque Queretaro+LOMAS DE ANGELOPOLIS III+SAN ANDRES CHOLULA+PUE+72830',
'AV LAREDO MZ 1 BIS LT 11+CARACOL+VENUSTIANO CARRANZA+CDMX+15630',
'MIGUEL N LIRA 122+RINCON DEL CONTRY+GUADALUPE+NL+67140',
'AV AQUILES SERDAN 430 ED HIGUERAS 604+ANGEL ZIMBRON+AZCAPOTZALCO+CDMX+02099',
'Jose Mararia Olloqui 48 505+Del Valle+BENITO JUAREZ+CDMX+03100',
'SAN GERONIMO 229+LOS GAVILANES PONIENTE+TLAJOMULCO DE ZUNIGA+JAL+45645',
'ALTAVISTA PONIENTE N 272 INTERIOR 190+FRACCIONAMIENTO ALTAVISTA RESIDENCIAL+ZAPOPAN+JAL+45133',
'MISION DE SANTO TOMAS 61+JARDINES COLONIALES+SAN PEDRO GARZA GARCIA+NL+66230',
'AVE MADRID 903+SAN ISIDRO+TORREON+COA+27100',
'ANASTACIO BUSTAMANTE 3+COL SAN JUAN+TULTITLAN+EM+54900',
'Juan Augusto Ingres 120 Dep C212+Santa Maria Nonoalco+BENITO JUAREZ+CDMX+03700',
'CALLE 1521 16+U HAB SAN JUAN DE ARAGON+GUSTAVO A. MADERO+CDMX+07918',
'VIVEROS DE TECOYOTITLA 34+VIVEROS DE LA LOMA+TLALNEPANTLA DE BAZ+EM+54080',
'SUR 114 18+COVE+ALVARO OBREGON+CDMX+01120',
'CHIMALHUACAN 60+LOMAS DE CRISTO+TEXCOCO+EM+56225',
'MONTMARTRE 264+RESIDENCIAL CHIPINQUE+SAN PEDRO GARZA GARCIA+NL+66297',
'Violeta 360 interior 205+San carlos+GUADALAJARA+JAL+44460',
'RIO MOLOLOA 4+MPIOBELLAVISTA NAY+TEPIC+NAY+63500',
'LIBERTAD LT 12 MZ 110+MODERNA+EMPALME+SON+85330',
'PROL BOSQUES DE LA REFORMA 1440 TORRE 1+DEPTO 202 COL BOSQUES DE LAS LOMAS+CUAJIMALPA DE MORELOS+CDMX+05120',
'PRIVADA LUNA 4+FRACC LAS FUENTES+XALAPA+VER+91097',
'LITERATOS 115+EL MARQUES+QUERETARO+QRO+76047',
'Alamo 104+radica residencial+APODACA+NL+66600',
'CALLE 15 NO 87 12 14 ITZIMNA+ITZIMNA PRIV PEREZ+MERIDA+YUC+97100',
'EDIF 18 NO 0 DPTO 402+INFO FARALLON OBISPO+ACAPULCO DE JUAREZ+GRO+39690',
'RTNO DE NUEVA ANDALUCIA 28+FRACC TERRANOVA+TARIMBARO+MICH+58880',
'AV NACIONES UNIDAS 7000 5+LOMAS DEL VALLE+ZAPOPAN+JAL+45110',
'CUARTA CERRADA DE SAN AGUSTIN 166+EL CAMPANARIO+QUERETARO+QRO+76146',
'ARQUIMIDES CABALLERO 109+BOULEVARES+AGUASCALIENTES+AGS+20288',
'FERNANDO ALENCASTRE 99 501+LOMAS DE CHAPULTEPEC+MIGUEL HIDALGO+CDMX+11000',
'AV SAN IGNACIO 3688 9+JARDINES DE SAN IGNACIO+ZAPOPAN+JAL+45040',
'MORELIA 45  309+ROMA NORTE+CUAUHTEMOC+CDMX+06700',
'CANARIAS 704+PORTALES SUR+BENITO JUAREZ+CDMX+03300',
'LLANURA 150+LOS PASTORES+NAUCALPAN DE JUAREZ+EM+53340',
'JOSE MA IBARRA NO 211+FELIPE CARRILLO+GENERAL ESCOBEDO+NL+66050',
'MONCAYO PABLO 114+COLINA DE SAN JERONIMO+MONTERREY+NL+64630',
'CTO MADRIGAL 1998 7+REAL SAN JAVIER+ZAPOPAN+JAL+45110',
'AGUACATE NUM 5274+VALLE VERDE 1 SEC+MONTERREY+NL+64360',
'JARDIN DE LAS MORAS 1013+FRACC ZARAGOZA+JUAREZ+CHI+32563',
'AV CUAUHTEMOC 3+SANTA MARIA ATLIHUETZIAN+YAUHQUEMEHCAN+TLA+90459',
'10 18+RUSTICA XALOSTOC+ECATEPEC DE MORELOS+EM+55340',
'CANAL HUEXOCOAPA 34+BARRIO 18+XOCHIMILCO+CDMX+16034',
'JESUS DEL MONTE 39 PLAZA VICTORIA B 704+JESUS DEL MONTE+HUIXQUILUCAN+EM+52764',
'C ABEDUL 206+BARR ALAMEDA+MONTERREY+NL+64100',
'RIO SENA 82+CUAUHTEMOC+CUAUHTEMOC+CDMX+06500']


    api_key="AIzaSyD9zIRT7YEXqFymHsxUEN4U18BLZYeW4hY"
    url="https://maps.googleapis.com/maps/api/geocode/json?"
    lat1=[None] * 50
    lng1=[None] * 50
    for i in range(50):
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
