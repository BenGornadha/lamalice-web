from nicegui import ui
from components.ui.section import Section
from config.settings import GAME

# Badges officiels servis par Google et Apple (pas de copie locale à maintenir).
# ponytail: les deux images ont des marges internes différentes, d'où les hauteurs asymétriques.
PLAY_BADGE = 'https://play.google.com/intl/en_us/badges/static/images/badges/fr_badge_web_generic.png'
APP_STORE_BADGE = 'https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/fr-fr'
PIXELPICKED_BADGE = 'https://api.pixelpicked.com/api/badges/1tD1LsRJHQh/live.png'

def game_section() -> None:
    with Section(id='game', bg_color='bg-white'):
        with ui.row().classes('w-full items-center gap-12 flex-wrap md:flex-nowrap'):
            if GAME['image_url']:
                ui.image(GAME['image_url']).classes('w-full md:w-1/2 rounded-2xl shadow-xl object-cover')

            with ui.column().classes('flex-1 gap-4'):
                ui.label('Side project').classes('text-sm font-semibold uppercase tracking-widest text-gray-400')
                ui.label(GAME['name']).classes('text-3xl md:text-4xl font-bold tracking-tight text-gray-900')
                ui.label(GAME['tagline']).classes('text-lg text-gray-500')
                ui.label(GAME['description']).classes('text-base text-gray-600 leading-relaxed whitespace-pre-line')

                # ponytail: <img> brut, ui.image (q-img) collapse la largeur des badges
                ui.html(
                    f'<div class="flex items-center gap-2 mt-4">'
                    f'<a href="{GAME["play_store_url"]}" target="_blank" rel="noopener">'
                    f'<img src="{PLAY_BADGE}" alt="Disponible sur Google Play" class="h-[68px] w-auto"></a>'
                    f'<a href="{GAME["app_store_url"]}" target="_blank" rel="noopener">'
                    f'<img src="{APP_STORE_BADGE}" alt="Télécharger dans l\'App Store" class="h-[46px] w-auto"></a>'
                    f'</div>'
                ).classes('w-full')

                # Badge de vérification PixelPicked (dimensions imposées par eux)
                ui.html(
                    f'<a href="{GAME["pixelpicked_url"]}" target="_blank" rel="noopener">'
                    f'<img src="{PIXELPICKED_BADGE}" width="250" height="54" alt="Approved on PixelPicked"></a>'
                ).classes('w-full mt-2')
