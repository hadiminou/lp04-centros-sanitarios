from coordenadas import*

def test_calcular_distancia(coordenada1, coordenada2):
    print("###test calcular distancia###")
    print(f"la distancia entre {coordenada1} y {coordenada2} es: {calcular_distancia(coordenada1, coordenada2)}")
    
def test_calcula_media_coordenadas(lista_coordenadas:Coordenadas):
    print("\n###test calcula media coordenadas###")
    print("promedio de las coordenadas dadas es: ",calcula_media_coordenadas(lista_coordenadas))

if __name__=="__main__":
    test_calcular_distancia(Coordenadas(25.2334, 13.3858894), Coordenadas(-233.2334, -34.23434))
    test_calcula_media_coordenadas([Coordenadas(3214.4321324, -12.4324), Coordenadas(-233.2334, -34.23434), Coordenadas(36.18825555644049, -5.923467895802184)])