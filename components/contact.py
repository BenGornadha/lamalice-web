from nicegui import ui
from components.ui.section import Section
from components.ui.button import Button
from config.settings import SITE

def contact_section() -> None:
    with Section(id='contact'):
        with ui.column().classes('w-full items-center text-center gap-6'):
            ui.label('Restons en contact').classes('text-3xl font-bold tracking-tight text-gray-900')
            ui.label('Un projet ? Une question ? N\'hésitez pas à m\'écrire.').classes('text-lg text-gray-500')
            
            Button(SITE['email'], href=f"mailto:{SITE['email']}", variant='secondary', icon='mail')
            
            with ui.row().classes('gap-6 mt-8'):
                # Social Icons (Text links for minimalism)
                ui.link('LinkedIn', SITE['linkedin_url']).classes('text-gray-500 hover:text-gray-900 transition-colors')
                ui.link('GitHub', SITE['github_url']).classes('text-gray-500 hover:text-gray-900 transition-colors')
                ui.link('Twitter', SITE['tiktok_url']).classes('text-gray-500 hover:text-gray-900 transition-colors') # Assuming tiktok is the other one mentioned
