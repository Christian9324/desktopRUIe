import sys
sys.path.insert(0, '..')

import requests
from ..db.models import Pais, Municipio, Fuerza, PuntosInter, Usuario
from . import config

base_url = config.base_url

def getAllPaisesApi():
    url_paises = config.getAllPaises
    list_pais = []
    try:
         respuesta = requests.get(base_url+url_paises)
         resp_json = respuesta.json()

         for item in  resp_json:
              list_pais.append(Pais(nombre_pais=item['nombre_pais'], iso3=item['iso3']))
    except:
         print("no se pudo acceder al servicio getAllPaises")

    return list_pais

def getAllMunicipiosApi():
    url_service = config.getAllMunicipios
    list_datos = []
    try:
         respuesta = requests.get(base_url + url_service)
         resp_json = respuesta.json()

         for item in  resp_json:
              list_datos.append(Municipio(estado=item['estado'], estadoAbr=item['estadoAbr'], nomMunicipio=item['nomMunicipio']))
    except:
         print("no se pudo acceder al servicio obtener los municipios")

    return list_datos

def getAllFuerzaApi():
    url_service = config.getAllFuerza
    list_datos = []

    respuesta = requests.get(base_url + url_service)
    resp_json = respuesta.json()

    try:
        for item in resp_json:
            list_datos.append(
                Fuerza(
                    oficinaR=item['oficinaR'],
                    numPunto=item['numPunto'],
                    nomPuntoRevision=item['nomPuntoRevision'],
                    tipoP=item['tipoP'],
                    ubicacion=item['ubicacion'],
                    coordenadasTexto=item['coordenadasTexto'],
                    latitud=float(item['latitud']),
                    longitud=float(item['longitud']),
                    personalINM=item['personalINM'],
                    personalSEDENA=item['personalSEDENA'],
                    personalMarina=item['personalMarina'],
                    personalGuardiaN=item['personalGuardiaN'],
                    personalOTROS=item['personalOTROS'],
                    vehiculos=item['vehiculos'],
                    seccion=item['seccion'],
                )
            )
    except:
        print("no se pudo acceder al servicio y obtener el estado de fuerza")
    
    return list_datos

def getAllPuntosIApi():
    url_service = config.getAllPuntosInter
    list_datos = []
    try:
         respuesta = requests.get(base_url + url_service)
         resp_json = respuesta.json()

         for item in  resp_json:
              list_datos.append(PuntosInter(nombrePunto=item['nombrePunto'], 
                                       estadoPunto=item['estadoPunto'], 
                                       tipoPunto=item['tipoPunto'], 
                                       ))
    except:
         print("no se pudo acceder al servicio y obtener los puntos")

    return list_datos

def verifyUserApi(datosG):

    datos = {'nickname': datosG.nickname, 'password': datosG.password}
    url_service = config.verificar_usuario
    
    try:
         respuesta = requests.post(base_url + url_service, json=datos)
         data_resp = respuesta.json()

         
    except:
         print("no se pudo acceder al servicio y obtener los puntos")

    return Usuario(idUser = 1, 
                   nickname=data_resp["nickname"], 
                   nombre=data_resp["nombre"], 
                   apellido=data_resp["apellido"],
                   password = data_resp["password"], 
                   estado= data_resp["estado"], 
                   tipo=data_resp["tipo"])