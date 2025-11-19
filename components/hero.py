from nicegui import ui
from components.ui.section import Section
from components.ui.button import Button
from config.settings import SITE

def hero(youtube_service) -> None:
    with Section(id='hero'):
        with ui.column().classes('w-full items-center text-center'):
            # Profile Picture
            photo_url = youtube_service.get_channel_picture_url()
            if photo_url:
                ui.image(photo_url).classes('w-56 h-56 rounded-full mb-8 shadow-sm object-cover')
            
            # Headlines
            ui.label("Hello, I'm Benjamin.").classes('text-5xl md:text-7xl font-bold tracking-tighter text-gray-900 mb-4')
            ui.label("Software Engineer & Content Creator.").classes('text-xl md:text-2xl text-gray-500 font-medium mb-8')
            
            # Bio
            ui.label("Passionné par le Clean Code, le TDD et l'architecture logicielle.\nJe partage mes connaissances pour aider les développeurs à écrire du code plus robuste.").classes('text-lg text-gray-600 max-w-2xl leading-relaxed mb-10 whitespace-pre-line')
            
            # CTAs
            with ui.row().classes('gap-4'):
                Button('Me contacter sur LinkedIn', href=SITE['linkedin_url'], variant='primary')
                Button('Voir mes vidéos', on_click=lambda: ui.run_javascript("document.getElementById('videos').scrollIntoView({ behavior: 'smooth' });"), variant='secondary')
