#! /usr/bin/python3

class circularBuff:

    def __init__(self,tam) -> None:
        self.nextIn = 0
        self.nextOut = None
        self.buffer = []
        for i in range(tam):
            self.buffer.append(None)

    def __str__(self) -> str:
        return self.buffer.__str__()

    def entrada(self, dato):
        print(f"{self} -> ", end="")
        self.buffer[self.nextIn] = dato
        if not self.nextOut: self.nextOut = self.nextIn
        self.nextIn + 1
        print(f"{self}")

    def salida(self,buffer):
        print(f"{self} -> ", end="") 
        item = buffer[self.nextOut]
        self.nextOut+1
        print(f"{self} -> {item}")        
        return item

    def esLleno(self) -> bool: 
        pass

# def avanzaEnEspacioCircular(tam):
#     nextPos = (i+1)%tam   # esencia del avance circular: coregir %tam
#     return nextPos

# def nextPos(tam,pos):
#     return (pos+1)%tam  # esencia del avance circular: coregir %tam

if __name__ == '__main__':

    # crear el buffer -de capacid variable-:
    cB1 = circularBuff(4)
    print(cB1)

    cB1.entrada(11)
    cB1.entrada(22)  # FIX 22 EN MALA POSICION

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


