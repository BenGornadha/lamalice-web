from nicegui import ui
from components.section_separator import SectionSeparator
from components.social_links import social_links


def about_section(youtube_service) -> None:
    with ui.column().classes('w-full items-center py-12').props('id="about-section"'):

        photo_url =youtube_service.get_channel_picture_url()

        if photo_url:
            ui.image(photo_url).classes('w-48 h-48 rounded-full shadow-lg border-4 border-white mb-4 object-cover')
        ui.label('Qui suis-je ?').classes('text-2xl font-semibold text-gray-800 mb-2')
        SectionSeparator()
        ui.label(f"Software Engineer et créateur de contenu passionné par le Clean Code, le TDD, les principes SOLID et l'art du Python élégant.\n\nIci, je partage mes vidéos et projets pour aider la communauté à écrire du code plus propre et plus robuste.").classes('text-center text-gray-600 max-w-xl')
        social_links()