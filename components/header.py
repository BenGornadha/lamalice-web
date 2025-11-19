from nicegui import ui
from config.settings import SITE
from components.ui.button import Button

def scroll_to(id: str):
    ui.run_javascript(f"document.getElementById('{id}').scrollIntoView({{ behavior: 'smooth' }});")

def header() -> None:
    with ui.header().classes('w-full bg-white/80 backdrop-blur-md border-b border-gray-200 z-50'):
        with ui.row().classes('w-full max-w-screen-xl mx-auto items-center justify-between py-4 px-6'):
            # Logo / Brand
            ui.label(SITE['name']).classes('text-xl font-semibold tracking-tight text-gray-900')
            
            # Navigation
            with ui.row().classes('gap-2'):
                Button('À propos', on_click=lambda: scroll_to('hero'), variant='ghost')
                Button('Vidéos', on_click=lambda: scroll_to('videos'), variant='ghost')
                Button('Contact', on_click=lambda: scroll_to('contact'), variant='ghost')