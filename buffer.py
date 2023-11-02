#! /usr/bin/python3

# globales globales globales globales globales !!!
# solo [podemos manejar con ellas] un buffer:
tam = 5
nextIN = 0
nextOUT = None

def entrada(buffer, dato):
    """acoplada a globales"""
    buffer[nextIN] = dato
    if not nextOUT: nextOUT = nextIN
    return nextIN+1 
    pass

def salida(buffer):
    """acoplada a globales"""
    answer = buffer[nextOUT]
    buffer[nextOUT] = None   ## solo para depurar
    nextOUT+1
    return answer

i = 0 #global
def avanzaEnEspacioCircular(tam):
    nextPos = (i+1)%tam   # esencia del avance circular: coregir %tam
    return nextPos

def nextPos(tam,pos):
    return (pos+1)%tam  # esencia del avance circular: coregir %tam

if __name__ == '__main__':

    # crear el buffer -de capacid variable-:

    buffer = []
    for i in range(tam):
        buffer.append(None)
    print(buffer)

    # estudio del avance circular
    i = 0
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    i = avanzaEnEspacioCircular(tam)
    print(f"i: {i}")

    print()

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    i = nextPos(tam,i)
    print(f"i: {i}")

    # usar el buffer

    # nextIN = entrada(buffer, 11)
    # print(buffer)

    # nextIN = entrada(buffer, 11)
    # print(buffer)

    # nextIN = entrada(buffer, 11)
    # print(buffer)

    # item = salida(buffer)
    # print(buffer, item)


    # ## desbordaria:
    # # nextIN = entrada(buffer, 11)
    # # print(buffer)


