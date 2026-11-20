from datetime import datetime
from typing import Optional
from nicegui import ui
from components.contact import contact_section
from components.game import game_section
from components.header import header
from components.hero import hero
from components.prompts import prompts_section
from components.ui.theme import apply_global_theme
from components.videos import videos_section
from config.settings import SITE
from infrastructure.persistence.cache import YouTubeCache
from services.youtube.api_client import YouTubeAPIClient
from services.youtube.youtube import YouTubeService


def _render_footer() -> None:
    year = datetime.now().year
    with ui.row().classes('w-full justify-center py-8 border-t border-slate-200/80 bg-white/70 backdrop-blur-xs'):
        with ui.row().classes('w-full max-w-6xl px-6 items-center justify-between flex-wrap gap-2'):
            ui.label(f"© {year} {SITE['name']} ({SITE['author']}). Tous droits réservés.").classes(
                'text-xs text-slate-400'
            )
            ui.label('Propulsé par Python & NiceGUI · Clean Code Edition').classes(
                'text-xs font-mono text-slate-400'
            )


def home_page(youtube_service: Optional[YouTubeService] = None) -> None:
    apply_global_theme()
    service = youtube_service or YouTubeService(api_client=YouTubeAPIClient(), cache=YouTubeCache())
    header()
    with ui.column().classes('w-full min-h-screen gap-0 p-0 m-0 justify-between'):
        with ui.column().classes('w-full gap-0'):
            hero(service)
            videos_section(service)
            prompts_section()
            game_section()
            contact_section()
        _render_footer()
