from datetime import datetime
from typing import Dict
from nicegui import ui
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section, SectionHeader
from config.settings import SITE

FRENCH_MONTHS = {
    1: 'janv.',
    2: 'févr.',
    3: 'mars',
    4: 'avr.',
    5: 'mai',
    6: 'juin',
    7: 'juil.',
    8: 'août',
    9: 'sept.',
    10: 'oct.',
    11: 'nov.',
    12: 'déc.',
}


def format_published_date(iso_date: str) -> str:
    if not iso_date:
        return ''
    try:
        dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
        return f'{dt.day:02d} {FRENCH_MONTHS[dt.month]} {dt.year}'
    except ValueError:
        return ''


def _video_url(video_id: str) -> str:
    return f'https://www.youtube.com/watch?v={video_id}'


def _render_thumbnail(video: Dict, is_latest: bool) -> None:
    with ui.element('div').classes('w-full aspect-video overflow-hidden relative bg-slate-900 rounded-t-3xl'):
        ui.image(video['thumbnail']).classes(
            'w-full h-full object-cover transition-transform duration-500 group-hover:scale-105'
        )
        if is_latest:
            with ui.element('div').classes('absolute top-3 left-3'):
                Badge('★ Dernière sortie', variant='accent')
        with ui.element('div').classes(
            'absolute bottom-3 right-3 w-10 h-10 rounded-full bg-slate-900/80 text-white '
            'backdrop-blur-xs flex items-center justify-center group-hover:bg-[#0066CC] transition-colors'
        ):
            ui.icon('play_arrow').classes('text-xl')


def _render_video_body(video: Dict, url: str) -> None:
    date_label = format_published_date(video.get('publishedAt', ''))
    with ui.column().classes('p-6 gap-3 flex-1 justify-between'):
        with ui.column().classes('gap-1.5'):
            if date_label:
                ui.label(date_label).classes('text-xs font-mono text-slate-400')
            title_cls = 'text-base font-bold leading-snug text-slate-900 line-clamp-2 group-hover:text-[#0066CC] transition-colors'
            ui.label(video['title']).classes(title_cls)
        ui.link('Regarder sur YouTube →', url, new_tab=True).classes('text-xs font-semibold text-[#0066CC] no-underline mt-1')


def _render_video_card(video: Dict, is_latest: bool) -> None:
    url = _video_url(video['videoId'])
    with Card(featured=is_latest, extra_classes='cursor-pointer group bento-lift flex flex-col justify-between') as card:
        card.on('click', lambda target=url: ui.run_javascript(f"window.open('{target}', '_blank')"))
        _render_thumbnail(video, is_latest)
        _render_video_body(video, url)


def _render_empty_state() -> None:
    with Card(extra_classes='p-8 text-center items-center gap-3'):
        ui.label('Retrouve toutes mes vidéos sur YouTube').classes('text-lg font-bold text-slate-900')
        Button('Ouvrir la chaîne YouTube', href=SITE['youtube_url'], variant='primary', icon='north_east')


def videos_section(youtube_service) -> None:
    videos = youtube_service.get_latest_videos()
    with Section(id='videos'):
        with ui.row().classes('w-full justify-between items-end flex-wrap gap-4'):
            SectionHeader(
                'Dernières Vidéos',
                'Tutoriels et retours concrets sur Python, le Clean Code, le TDD et les agents IA.',
                eyebrow='YouTube · @LaMaliceCode',
            )
            Button('Voir toute la chaîne', href=SITE['youtube_url'], variant='secondary', icon='north_east')
        if not videos:
            _render_empty_state()
            return
        with ui.element('div').classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'):
            for index, video in enumerate(videos):
                _render_video_card(video, is_latest=(index == 0))
