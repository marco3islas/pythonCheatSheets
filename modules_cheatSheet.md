# Módulo glob

## Importar el módulo

```python
import glob
```

- Buscar archivos en un directorio
Python

```python
files = glob.glob('/ruta/al/directorio/*.txt')
```

- Filtrar archivos con patrones
Python

```python
txt_files = glob.glob('*.txt')
```

### Módulo csv
- Importar el módulo
Python

```python
import csv
```

- Leer un archivo CSV
Python

```python
with open('archivo.csv', 'r') as file:
csv_reader = csv.reader(file)
for row in csv_reader:
print(row)
```

- Escribir en un archivo CSV Python

    ```python
    data = [["Nombre", "Edad"], ["Alice", 30], ["Bob", 25]]
    with open('datos.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    ```

### Módulo shutil
- Importar el módulo Python

    ```python
    import shutil
    ```

- Copiar un archivo Python

    ```python
    shutil.copy('origen.txt', 'destino.txt')
    ```

- Mover un archivo Python

    ```python
    shutil.move('origen.txt', 'destino.txt')
    ```

- Eliminar un archivo o directorio Python

    ```python
    shutil.rmtree('directorio_a_eliminar')
    ```

### Módulo json
- Importar el módulo

    ```python
    import json
    ```

- Leer un archivo JSON

    ```python
    with open('datos.json', 'r') as file:
    data = json.load(file)
    ```

- Escribir en un archivo JSON

    ```python
    data = {"nombre": "Alice", "edad": 30}
    with open('datos.json', 'w') as file:
    json.dump(data, file)
    ```

### Módulo webbrowser
- Importar el módulo

    ```python
    import webbrowser
    ```

- Abrir una URL en el navegador predeterminado

    ```python
    webbrowser.open('https://www.ejemplo.com')
    ```

- Abrir una URL en un navegador específico

    ```python
    webbrowser.get('firefox').open('https://www.ejemplo.com')
    ```

- Buscar en Google

    ```python
    webbrowser.open('https://www.google.com/search?q=python')
    ```

