from collections import namedtuple
import csv
import math
#import mapas
from mapas import*
from coordenadas import*
CentroSanitario=namedtuple("centro","nombre,localidad,latitud,longitud,estado,num_camas,\
                           tiene_acceso_discapasitados,tiene_uci")

def a_booleano(a)->bool:
    res = None
    if a!= None:
        a= a.strip().lower()
        if a=="true":
            res=True
        elif a=='false':
            res=False
    return res

def lee_centros(ruta:str)->list:
    centros= []
    with open(ruta, mode='rt', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for nombre,localidad,latitud,longitud,estado,num_camas,\
                           tiene_acceso_discapasitados,tiene_uci in lector:
            coordenadas=Coordenadas(float(latitud), float(longitud))
            centros.append((nombre.strip(),localidad.strip(),coordenadas, estado.strip(), int(num_camas),\
                             a_booleano(tiene_acceso_discapasitados), a_booleano(tiene_uci)))
    return centros

def calcular_total_camas_centros_accesibles(lista:list[CentroSanitario])->int:
    res = 0
    for p in lista:
        if p[5]:
            res = res + p[4]
    return res

def obtener_centros_con_uci_cercanos_a(lista_centros:list[CentroSanitario], tupla_coordenadas:Coordenadas, umbral:float)->list:
    res=[]
    for centro in lista_centros:
        if calcular_distancia(tupla_coordenadas, centro[2])<=umbral:
            hospital=(centro[0], centro[1], centro[2])
            res.append(hospital)
    return res

def generar_mapa(centros:list[tuple[str, str, Coordenadas]], archivo_html:str)->None:
    lista_coordenadas=[]
    for _,_,coordenadas in centros:
        lista_coordenadas.append(coordenadas)
    coordenada_centro=calcula_media_coordenadas(lista_coordenadas)
    mapa = crea_mapa(coordenada_centro)
    for nombre, localidad, coordenadas in centros:
        etiqueta = f"{nombre} ({localidad})"
        agrega_marcador(mapa, coordenadas, etiqueta, "red")
    guarda_mapa(mapa, archivo_html)
