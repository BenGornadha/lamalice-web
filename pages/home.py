from nicegui import ui
from components.background import background
from components.header import header
from components.about import about_section
from components.videos import videos_section
from components.projects_contact import projects_contact_section
from services.youtube.youtube import YouTubeService
from infrastructure.persistence.cache import YouTubeCache
from services.youtube.api_client import YouTubeAPIClient

def home_page() -> None:
    youtube_service = YouTubeService(api_client=YouTubeAPIClient(), cache=YouTubeCache())

    background()
    with ui.column().classes('w-full items-center'):
        header()
        about_section(youtube_service)
        videos_section(youtube_service)
        projects_contact_section() 