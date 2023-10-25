# Cheat Sheet de PySimpleGUI

## Instalación
#### Para instalar PySimpleGUI, utiliza pip:

    ```bash
    pip install PySimpleGUI
    ```

## Importar
```python
import PySimpleGUI as sg
```
## Crear una Ventana Básica

    ```python
    layout = [
    [sg.Text("Hola, mundo!")],
    [sg.Button("OK")]
    ]

    window = sg.Window("Mi Ventana", layout)
    ```

## Event Loop

    ```python
    while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "OK":
    break
    ```

## Elementos de Interfaz Texto

    ```python
    sg.Text("Hola, mundo!")
    ```

## Botón

    ```python
    sg.Button("OK")
    ```

## Cuadro de Texto

    ```python
    sg.InputText()
    ```

## Etiqueta

    ```python
    sg.Text("Etiqueta:")
    ```

## Cuadro de Selección

    ```python
    sg.Listbox(values=["Opción 1", "Opción 2"], size=(20, 2))
    ```

## Barra de Progreso

    ```python
    sg.ProgressBar(max_value=100, size=(20, 20))
    ```

## Ventanas Emergentes
- Mensaje de Alerta

```python
sg.popup("¡Hola, mundo!")
```

- Diálogo de Archivo

```python
filename = sg.popup_get_file("Selecciona un archivo")
```

 - Diálogo de Carpeta

     ```python
     folder = sg.popup_get_folder("Selecciona una carpeta")
     ```

