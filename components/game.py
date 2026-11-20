from nicegui import ui
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section
from config.settings import GAME, GAME_STATS

PLAY_BADGE = 'https://play.google.com/intl/en_us/badges/static/images/badges/fr_badge_web_generic.png'
APP_STORE_BADGE = 'https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/fr-fr'
PIXELPICKED_BADGE = 'https://api.pixelpicked.com/api/badges/1tD1LsRJHQh/live.png'


def _render_store_badges() -> None:
    ui.html(
        f'<div class="flex flex-wrap items-center gap-3 mt-2">'
        f'<a href="{GAME["play_store_url"]}" target="_blank" rel="noopener">'
        f'<img src="{PLAY_BADGE}" alt="Disponible sur Google Play" class="h-[64px] w-auto"></a>'
        f'<a href="{GAME["app_store_url"]}" target="_blank" rel="noopener">'
        f'<img src="{APP_STORE_BADGE}" alt="Télécharger dans l\'App Store" class="h-[44px] w-auto"></a>'
        f'<a href="{GAME["pixelpicked_url"]}" target="_blank" rel="noopener">'
        f'<img src="{PIXELPICKED_BADGE}" width="210" height="45" alt="Approved on PixelPicked" class="h-[44px] w-auto"></a>'
        f'</div>'
    ).classes('w-full')


def _render_game_pitch() -> None:
    with ui.column().classes('lg:col-span-7 gap-4'):
        with ui.row().classes('items-center gap-2 flex-wrap'):
            Badge('Side Project · Mobile Game', variant='neutral')
            Badge('Gratuit sur Android & iOS', variant='success', dot=True)
        ui.label(GAME['name']).classes('text-3xl md:text-4xl font-extrabold tracking-tight text-slate-900')
        ui.label(GAME['tagline']).classes('text-lg font-medium text-[#0066CC]')
        ui.label(GAME['description']).classes('text-sm md:text-base text-slate-600 leading-relaxed whitespace-pre-line')
        _render_store_badges()
        with ui.row().classes('pt-1'):
            Button('Rejoindre le Discord Hero Line TD', href=GAME['discord_url'], variant='secondary', icon='forum')


def _render_stats_bento() -> None:
    with ui.column().classes('lg:col-span-5 gap-4'):
        if GAME['image_url']:
            ui.image(GAME['image_url']).classes('w-full rounded-2xl shadow-lg object-cover')
        with ui.element('div').classes('w-full grid grid-cols-2 sm:grid-cols-3 gap-3'):
            for stat in GAME_STATS:
                with ui.column().classes(
                    'rounded-2xl bg-slate-50/90 border border-slate-200/80 p-4 items-center text-center gap-1 bento-lift'
                ):
                    ui.label(stat['value']).classes('text-2xl font-extrabold text-[#0066CC] tracking-tight')
                    ui.label(stat['label']).classes('text-xs font-medium text-slate-500')
        with ui.element('div').classes('rounded-2xl bg-slate-900 text-white p-5'):
            ui.label('MÉCANIQUE CLÉ').classes('text-xs font-mono text-blue-400 tracking-widest')
            ui.label(GAME.get('quote', GAME['tagline'])).classes('text-sm font-medium leading-relaxed mt-1')


def game_section() -> None:
    with Section(id='game'):
        with Card(extra_classes='p-7 md:p-10'):
            with ui.element('div').classes('w-full grid grid-cols-1 lg:grid-cols-12 gap-8 items-center'):
                _render_game_pitch()
                _render_stats_bento()
