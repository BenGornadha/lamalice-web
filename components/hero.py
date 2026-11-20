from typing import Dict
from nicegui import ui
from components.header import scroll_to
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section
from config.settings import HERO_PILLARS, SITE, STACK_TAGS


def _safe_channel_picture(youtube_service) -> str:
    fallback = SITE.get('avatar_url', '')
    try:
        return youtube_service.get_channel_picture_url() or fallback
    except Exception:
        return fallback


def _render_avatar(photo_url: str) -> None:
    ui.image(photo_url).classes(
        'w-32 h-32 md:w-36 md:h-36 rounded-3xl object-cover '
        'border-4 border-white shadow-xl ring-1 ring-slate-900/5 shrink-0'
    )


def _render_pitch_card() -> None:
    with Card(extra_classes='lg:col-span-7 p-8 md:p-10 flex flex-col justify-between gap-8'):
        with ui.column().classes('gap-5'):
            Badge(f"{SITE['author']} · {SITE['tagline']}", variant='neutral', dot=True)
            ui.label(SITE['headline']).classes(
                'text-4xl md:text-6xl font-extrabold tracking-tight text-slate-900 leading-[1.1]'
            )
            ui.label(SITE['bio']).classes('text-base md:text-lg text-slate-600 leading-relaxed max-w-2xl')
        with ui.row().classes('gap-3 flex-wrap items-center pt-2'):
            Button('Me contacter sur LinkedIn', href=SITE['linkedin_url'], variant='primary', icon='north_east')
            Button('Explorer mes vidéos', on_click=lambda: scroll_to('videos'), variant='secondary', icon='play_circle')
            Button('GitHub', href=SITE['github_url'], variant='ghost', icon='code')


def _render_profile_tile(photo_url: str) -> None:
    with Card(extra_classes='col-span-2 p-6 md:p-7 flex items-center'):
        with ui.row().classes('w-full items-center gap-6 no-wrap'):
            _render_avatar(photo_url)
            with ui.column().classes('gap-2 min-w-0'):
                ui.label(SITE['handle']).classes('text-xl font-extrabold text-slate-900 tracking-tight')
                ui.label('Créateur Tech YouTube & développeur de Hero Line TD.').classes(
                    'text-sm text-slate-500 leading-snug'
                )
                with ui.row().classes('gap-1.5 flex-wrap pt-1'):
                    for tag in STACK_TAGS:
                        Badge(tag, variant='mono')


def _render_pillar_tile(pillar: Dict[str, str]) -> None:
    with Card(extra_classes='p-6 flex flex-col justify-between gap-3 bento-lift'):
        ui.label(pillar['index']).classes('text-xs font-mono font-semibold text-[#0066CC] tracking-wider')
        with ui.column().classes('gap-1'):
            ui.label(pillar['title']).classes('text-base font-bold text-slate-900')
            ui.label(pillar['description']).classes('text-xs text-slate-500 leading-relaxed')


def hero(youtube_service) -> None:
    photo_url = _safe_channel_picture(youtube_service)
    with Section(id='hero', spacing='pt-10 pb-14 md:pt-14 md:pb-20'):
        with ui.element('div').classes('w-full grid grid-cols-1 lg:grid-cols-12 gap-5 items-stretch'):
            _render_pitch_card()
            with ui.element('div').classes('lg:col-span-5 grid grid-cols-1 sm:grid-cols-2 gap-5'):
                _render_profile_tile(photo_url)
                for pillar in HERO_PILLARS:
                    _render_pillar_tile(pillar)
