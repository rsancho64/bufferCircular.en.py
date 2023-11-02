# bufferCircular.en.py

un buffer circular implementado 
sobre un array lineal (una lista python)

Ilustracion de la evolucion:

```
 012345678
[.........] vacio inicialmente
[x........] tras entrada
[xx.......] tras entrada
[xxx......] tras entrada
[xxxx.....] tras entrada
[xxxxx....] tras entrada
[.xxxx....] tras salida
[..xxx....] tras salida
[..xxxx...] tras entrada
..
[....xxxxx] 
[x...xxxxx] tras entrada
[xx..xxxxx] tras entrada
[xxx.xxxxx] tras entrada
[xxxxxxxxx] tras entrada: queda lleno
```

# implementacion 

Se expresan (y no se manejan) dos excepciones:
    intento de salida cuando esta vacio
    intento de entrada cuando esta lleno

```python
tam = 9
```

- [ ] programar la creacion del buffer con append(none)
- [ ] programar el manejo del buffer con 
  - [ ] dos indices globales: `nextIN` y `nextOUT`

```python
nextIN = 0
nextOUT = None
```

  - [ ] dos funciones para manejarlos: `nextIN` y `nextOUT`

```python
def entrada (buffer, dato):
    pass

def salida (buffer):
    return item
```
