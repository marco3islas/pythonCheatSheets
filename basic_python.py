# Cheat Sheet de Python

## Variables y Tipos de Datos
### Variables
```python
variable = 42
nombre = "Juan"
booleano = True
```

### Tipos de Datos
```python
entero = 42
flotante = 3.14
cadena = "Hola, mundo!"
booleano = True
```

## Estructuras de Control python

### Condicionales
```python
if condicion:
    # código si la condición es verdadera
else:
    # código si la condición es falsa
```

### Bucles
```pyton
for elemento in lista:
# código para cada elemento en la lista

while condicion:
# código mientras la condición sea verdadera
```

## Listas y Diccionarios python

### Listas
```python
mi_lista = [1, 2, 3, 4, 5]
elemento = mi_lista[2]
mi_lista.append(6)
mi_lista.remove(3)
```

### Diccionarios

```python
mi_diccionario = {"clave": "valor", "nombre": "Juan"}
valor = mi_diccionario["clave"]
mi_diccionario["edad"] = 30
```

## Funciones python

```python
def saludar(nombre):
return "Hola, " + nombre

resultado = saludar("Ana")
```
## Módulos y Bibliotecas python

```python
import math
raíz_cuadrada = math.sqrt(25)

from random import randint
número_aleatorio = randint(1, 100)
```

## Excepciones python

```pyton
try:
# código que puede generar una excepción
except TipoDeExcepción as e:
# manejo de la excepción
else:
# código si no se generó una excepción
finally:
# código que se ejecuta siempre
```

## Comentarios python

```python
# Este es un comentario de una línea
```

```python
"""
Este es un comentario
de múltiples líneas
"""
```
