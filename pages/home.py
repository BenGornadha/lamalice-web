from nicegui import ui
from components.header import header
from components.hero import hero
from components.videos import videos_section
from components.contact import contact_section
from services.youtube.youtube import YouTubeService
from infrastructure.persistence.cache import YouTubeCache
from services.youtube.api_client import YouTubeAPIClient
from config.settings import COLORS

def home_page() -> None:
    # Set global theme colors
    ui.colors(primary=COLORS['accent'], secondary=COLORS['text_secondary'], accent=COLORS['accent'])
    
    # Initialize services
    youtube_service = YouTubeService(api_client=YouTubeAPIClient(), cache=YouTubeCache())

    # Page Layout
    header()
    
    # We use a column with full width and specific background
    with ui.column().classes('w-full min-h-screen gap-0 p-0 m-0').style(f'background-color: {COLORS["background"]}'):
        # Main Content
        with ui.column().classes('w-full gap-0'):
            hero(youtube_service)
            videos_section(youtube_service)
            contact_section()
            
        # Footer (Simple copyright)
        with ui.row().classes('w-full justify-center py-8 border-t border-gray-200 bg-white'):
            ui.label('© 2024 LaMaliceCode. All rights reserved.').classes('text-xs text-gray-400')