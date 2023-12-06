import math
from collections import namedtuple
Coordenadas=namedtuple("Coordenadas","latitud, longitud")

def calcular_distancia(coordenada1:Coordenadas, coordenada2:Coordenadas)->float:
    distancia=math.sqrt((coordenada2.longitud - coordenada2.latitud)**2 + \
                         (coordenada1.longitud - coordenada1.latitud)**2)
    return distancia

def calcula_media_coordenadas(lista_coordenadas:list[Coordenadas])->Coordenadas:
    res=()
    latitud=[]
    longitud=[]
    for i in lista_coordenadas:
        latitud.append(i.latitud)
        longitud.append(i.longitud)
    res=None
    if (len(lista_coordenadas)>0):
        res= Coordenadas(sum(latitud)/len(latitud),sum(longitud)/len(longitud))
    return res