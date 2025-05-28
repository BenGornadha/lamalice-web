from nicegui import ui
from config.settings import SITE
from components.orange_button import OrangeButton

def scroll_to_section(section_id: str) -> None:
    ui.run_javascript(f"document.getElementById('{section_id}').scrollIntoView({{ behavior: 'smooth' }});")

def header() -> None:
    with ui.row().classes('w-full justify-between items-center py-6 px-8 shadow-sm'):
        ui.label(SITE['name']).classes('text-3xl font-bold text-orange-500')
        ui.label(SITE['tagline']).classes('text-lg text-gray-600')
        with ui.row().classes('gap-4'):
            OrangeButton('Accueil', on_click=lambda: scroll_to_section('about-section'))
            OrangeButton('Vidéos', on_click=lambda: scroll_to_section('videos-section'))
            OrangeButton('Formations', on_click=lambda: scroll_to_section('formations-section'))
            OrangeButton('Contact', on_click=lambda: scroll_to_section('contact-section')) 