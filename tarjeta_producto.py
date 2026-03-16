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