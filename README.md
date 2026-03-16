#  Catálogo de Productos con Flet

Proyecto desarrollado en **Python** utilizando el framework **Flet** para crear una aplicación de catálogo de productos tecnológicos con componentes reutilizables.

Este proyecto fue realizado como **Proyecto Integrador de la Unidad 2**.

---

#  Objetivo del Proyecto

Crear una aplicación que muestre un **catálogo de productos tecnológicos** utilizando un **componente reutilizable** que permita mostrar múltiples productos sin repetir código.

---

#  Vista general del proyecto

A continuación se muestra cómo se ve la aplicación final ejecutándose.

<img width="1576" height="887" alt="image" src="https://github.com/user-attachments/assets/aa79a4f2-d833-4f3f-96b6-730cb972744f" />



En esta interfaz podemos observar:

- Encabezado de la tienda
- Tarjetas de productos
- Imagen del producto
- Nombre
- Descripción
- Precio
- Botones de acción

---

#  Paso 1: Creación del entorno de trabajo

Primero se creó una carpeta para el proyecto:

```
Catalogo
```

Después se creó un entorno virtual:

```
python -m venv .venv
```

Luego se activó el entorno virtual:

```
.venv\Scripts\activate
```

Esto permite instalar dependencias sin afectar otros proyectos.

---

#  Paso 2: Instalación de Flet

Con el entorno virtual activo se instaló Flet:

```
pip install flet
```

Flet permite crear **interfaces gráficas usando Python**.

---

#  Paso 3: Estructura del proyecto

La estructura inicial del proyecto quedó así:

```
catalogo-productos-flet/

assets/

main.py
tarjeta_producto.py
README.md
```

La carpeta `assets` se utiliza para almacenar **las imágenes de los productos** que aparecen en el catálogo.

---

#  Paso 4: Creación del componente reutilizable

Para evitar repetir código se creó una clase llamada:

```
TarjetaProducto
```

Esta clase **hereda de `ft.Container`**.

Cada tarjeta incluye:

- Imagen
- Nombre del producto
- Descripción
- Precio
- Botones de acción

---

#  Ejemplo de una tarjeta de producto

Así se ve una tarjeta individual dentro del catálogo.

<img width="306" height="386" alt="image" src="https://github.com/user-attachments/assets/822b4d5b-b8d0-43ff-bfb3-d1b04f127b07" />


---

#  Código del componente reutilizable

Archivo:

```
tarjeta_producto.py
```

```python
import flet as ft

class TarjetaProducto(ft.Container):

    def __init__(self, nombre, descripcion, precio, imagen):
        super().__init__()

        self.width = 250
        self.border_radius = 15
        self.padding = 10
        self.bgcolor = ft.Colors.WHITE

        self.shadow = ft.BoxShadow(
            blur_radius=10,
            spread_radius=1,
            color=ft.Colors.BLACK12
        )

        self.content = ft.Column(
            controls=[

                ft.Image(
                    src=imagen,
                    width=200,
                    height=150,
                    fit="contain"
                ),

                ft.Text(
                    nombre,
                    size=18,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    descripcion,
                    size=12,
                    color=ft.Colors.GREY
                ),

                ft.Text(
                    f"$ {precio}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
                        ft.ElevatedButton("Agregar al carrito")
                    ]
                )
            ]
        )
```

---

#  Paso 5: Modelo de datos

Los productos se almacenan en un arreglo de diccionarios.

Cada producto contiene:

- id
- nombre
- descripcion
- precio
- ruta_imagen

---

# 🖥 Paso 6: Interfaz principal

Archivo:

```
main.py
```

```python
import os
import flet as ft
from tarjeta_producto import TarjetaProducto

productos = [
    {
        "id": 1,
        "nombre": "Laptop Gamer",
        "descripcion": "Procesador i7 y 16GB RAM",
        "precio": 25000,
        "ruta_imagen": "laptop.jpg"
    },
    {
        "id": 2,
        "nombre": "Smartphone",
        "descripcion": "Pantalla AMOLED y 128GB",
        "precio": 12000,
        "ruta_imagen": "telefono.jpg"
    },
    {
        "id": 3,
        "nombre": "Audífonos Bluetooth",
        "descripcion": "Cancelación de ruido",
        "precio": 1500,
        "ruta_imagen": "audifonos.jpg"
    },
    {
        "id": 4,
        "nombre": "Smartwatch",
        "descripcion": "Monitor de salud",
        "precio": 3000,
        "ruta_imagen": "reloj.jpg"
    },
    {
        "id": 5,
        "nombre": "Tablet",
        "descripcion": "Pantalla 10 pulgadas",
        "precio": 8000,
        "ruta_imagen": "tablet.jpg"
    }
]

def main(page: ft.Page):

    page.title = "Catálogo Tecnológico"
    page.bgcolor = ft.Colors.GREY_100
    page.scroll = "auto"

    tarjetas = []

    for producto in productos:

        tarjeta = TarjetaProducto(
            producto["nombre"],
            producto["descripcion"],
            producto["precio"],
            producto["ruta_imagen"]
        )

        tarjetas.append(tarjeta)

    page.add(
        ft.Column(
            controls=[

                ft.Text(
                    "🛒 Tienda de Tecnología",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Row(
                    wrap=True,
                    spacing=20,
                    controls=tarjetas
                )

            ]
        )
    )

# --- SECCIÓN MODIFICADA PARA RENDER ---
if __name__ == "__main__":
    # Render asigna un puerto dinámico; si no existe, usamos el 8000
    port = int(os.environ.get("PORT", 8000))
    
    ft.app(
        target=main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER, # Obligatorio para Render
        host="0.0.0.0",               # Obligatorio para Render
        port=port
)
```

---

#  Vista de las tarjetas repetidas

El uso de un componente reutilizable permite mostrar múltiples productos automáticamente.

<img width="1003" height="410" alt="image" src="https://github.com/user-attachments/assets/01a88ecc-eab0-481d-9663-e18764ef8fe2" />


---

#  Archivo requirements.txt

Para ejecutar el proyecto en servidores o entornos externos se utiliza un archivo llamado:

```
requirements.txt
```

Contenido:

```
flet
```

Este archivo permite instalar automáticamente las dependencias necesarias del proyecto.

---

#  Estructura final del repositorio

```
catalogo-productos-flet/

assets/
   laptop.jpg
   telefono.jpg
   audifonos.jpg
   reloj.jpg
   tablet.jpg

imagenes/
   catalogo.png
   tarjeta.png
   tarjetas.png

main.py
tarjeta_producto.py
requirements.txt
README.md
```

---

#  Ejecución del proyecto

Instalar dependencias:

```
pip install -r requirements.txt
```

Ejecutar el programa:

```
python main.py
```

---

#  Tecnologías utilizadas

- Python
- Flet
- Visual Studio Code
- GitHub
