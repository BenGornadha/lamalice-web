from nicegui import ui
from components.info_card import InfoCard
from components.section_separator import SectionSeparator
from services.youtube import YouTubeService

def videos_section() -> None:
    with ui.column().classes('w-full items-center py-12').props('id="videos-section"'):
        ui.label('Mes dernières vidéos YouTube').classes('text-2xl font-semibold text-gray-800 mb-2')
        SectionSeparator()
        videos = YouTubeService().get_latest_videos()
        with ui.row().classes('gap-8'):
            for video in videos:
                with ui.card().classes('w-80 bg-white shadow-md cursor-pointer'):
                    ui.image(video['thumbnail']).classes('rounded-lg w-full h-44 object-cover')
                    ui.label(video['title']).classes('text-lg font-bold text-gray-800 mt-2')
                    ui.html(f'<a href="https://www.youtube.com/watch?v={video["videoId"]}" target="_blank" rel="noopener noreferrer" class="block w-full text-center rounded-full mt-2 px-6 py-2 font-semibold bg-red-600 text-white hover:bg-red-700 transition">Voir sur YouTube</a>') 