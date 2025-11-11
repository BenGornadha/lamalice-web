from nicegui import ui
from config.settings import SITE
from components.info_card import InfoCard
from components.section_separator import SectionSeparator

def projects_contact_section() -> None:
    with ui.column().classes('w-full items-center py-12 bg-gray-50').props('id="formations-section"'):
        # ui.label('Formations & Projets').classes('text-2xl font-semibold text-gray-800 mb-2')
        # SectionSeparator()
        with ui.row().classes('gap-8'):
          #   InfoCard(title='Formation Clean Code', description='Bientôt disponible !')
            InfoCard(title='Projet Open Source', description='À découvrir prochainement.')
        ui.label('Contact').classes('text-2xl font-semibold text-gray-800 mt-8 mb-2').props('id="contact-section"')
        SectionSeparator()
        ui.label(f'Pour toute demande : {SITE["email"]}').classes('text-gray-600') 