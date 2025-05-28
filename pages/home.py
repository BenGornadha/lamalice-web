from nicegui import ui
from components.background import background
from components.header import header
from components.about import about_section
from components.videos import videos_section
from components.projects_contact import projects_contact_section

def home_page() -> None:
    background()
    with ui.column().classes('w-full items-center'):
        header()
        about_section()
        videos_section()
        projects_contact_section() 