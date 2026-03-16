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

    page.title = "Tienda Tecnológica"
    page.bgcolor = ft.Colors.GREY_100
    page.scroll = "auto"

    tarjetas = []

    for p in productos:

        tarjeta = TarjetaProducto(
            p["nombre"],
            p["descripcion"],
            p["precio"],
            p["ruta_imagen"]
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


ft.app(target=main, assets_dir="assets")