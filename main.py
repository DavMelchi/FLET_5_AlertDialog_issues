import flet as ft
from page_1 import page_1_page
from page_2 import page_2_page

def main(page: ft.Page):

    t = ft.Tabs(
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=page_1_page(page)
                ),
            ),
            ft.Tab(
                text="Tab 2",
                icon=ft.icons.SETTINGS,
                content=page_2_page(page),

            ),
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main)