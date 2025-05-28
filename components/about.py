from nicegui import ui
from config.settings import SITE
from components.section_separator import SectionSeparator
from services.youtube import YouTubeService

def about_section() -> None:
    with ui.column().classes('w-full items-center py-12').props('id="about-section"'):
        # Photo de profil YouTube (plus grande)
        photo_url = YouTubeService().get_channel_picture_url()
        if photo_url:
            ui.image(photo_url).classes('w-48 h-48 rounded-full shadow-lg border-4 border-white mb-4 object-cover')
        ui.label('Qui suis-je ?').classes('text-2xl font-semibold text-gray-800 mb-2')
        SectionSeparator()
        ui.label(f"Créateur de contenu passionné par le Clean Code, le TDD, les principes SOLID et l'art du Python élégant.\n\nIci, je partage mes vidéos, formations et projets pour aider la communauté à écrire du code plus propre et plus robuste.").classes('text-center text-gray-600 max-w-xl') 