from nicegui import ui
from components.ui.section import Section
from components.ui.card import Card
from components.ui.button import Button

def videos_section(youtube_service) -> None:
    with Section(id='videos', bg_color='bg-gray-50'):
        with ui.column().classes('w-full gap-8'):
            # Section Header
            with ui.row().classes('w-full justify-between items-end'):
                with ui.column().classes('gap-2'):
                    ui.label('Dernières Vidéos').classes('text-3xl font-bold tracking-tight text-gray-900')
                    ui.label('Tutoriels et partages sur le développement Python.').classes('text-lg text-gray-500')
                
                Button('Voir la chaîne', href='https://www.youtube.com/@lamalicecode', variant='ghost', icon='arrow_forward')

            # Videos Grid
            videos = youtube_service.get_latest_videos()
            with ui.grid(columns=3).classes('w-full gap-6'):
                for video in videos:
                    # Card is clickable
                    with Card().classes('cursor-pointer group') as card:
                        # We use a transparent button overlay or just javascript onclick for the whole card
                        # NiceGUI cards aren't natively clickable links, so we wrap content or use JS.
                        # Here we'll use a simple onclick handler on the card.
                        card.on('click', lambda v=video: ui.open(f"https://www.youtube.com/watch?v={v['videoId']}"))
                        
                        # Thumbnail container with overflow hidden for zoom effect
                        with ui.element('div').classes('w-full aspect-video overflow-hidden relative'):
                            ui.image(video['thumbnail']).classes('w-full h-full object-cover transition-transform duration-500 group-hover:scale-105')
                        
                        # Content
                        with ui.column().classes('p-5 gap-2'):
                            ui.label(video['title']).classes('text-base font-semibold leading-snug text-gray-900 line-clamp-2 group-hover:text-blue-600 transition-colors')
                            ui.label('Regarder maintenant').classes('text-sm font-medium text-gray-400 group-hover:text-blue-600 transition-colors mt-2')