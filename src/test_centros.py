from centros import*

def test_lee_centros(datos):
    print("###Test lee centros###")
    print(f"Leídos {len(datos)} registros.")
    print("\nMostrando los 3 primeros:", datos[:3])
    print("\nMostrando los 3 últimos:", datos[-3:])

def test_calcular_total_camas_centros_accesibles(datos):
    print("\n###Test calcular total camas centros accesibles###")
    print("Numero total de camas accesibles para discapacitados: ", \
          calcular_total_camas_centros_accesibles(datos))

def test_obtener_centros_con_uci_cercanos_a(centros, coordenadas, umbral):
    print("\n###test obtener centros con uci cercanos a###")
    res=obtener_centros_con_uci_cercanos_a(centros, coordenadas, umbral)
    print(f"hay {len(res)} centros")
    for c in res:
        print(c)
    generar_mapa(res, "Proyectos Python\WSPython\git\lp04-centros-sanitarios-hadiminou\out\mapa.html")
    print(f"\nlos centros mas cercanos a las coordenadas {coordenadas}, teniendo un umbral de {umbral} km son: {res}")

if __name__=="__main__":
    datos=lee_centros('Proyectos Python\WSPython\git\lp04-centros-sanitarios-hadiminou\data\centrosSanitarios.csv')
    test_lee_centros(datos)
    test_calcular_total_camas_centros_accesibles(datos)
    test_obtener_centros_con_uci_cercanos_a(datos, Coordenadas(4.545454, 845.54656), 1144)
