from nicegui import ui
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section
from config.settings import GAME, SITE


def contact_section() -> None:
    with Section(id='contact'):
        with Card(extra_classes='p-8 md:p-12'):
            with ui.column().classes('w-full items-center text-center gap-4'):
                Badge('Contact & Réseaux', variant='neutral', dot=True)
                ui.label('Restons en contact').classes('text-3xl md:text-4xl font-extrabold tracking-tight text-slate-900')
                ui.label("Un projet d'architecture logicielle, une question ou un retour sur mes vidéos ? Écris-moi.").classes(
                    'text-base md:text-lg text-slate-500 max-w-xl'
                )
                with ui.row().classes('gap-3 flex-wrap justify-center pt-2'):
                    Button(SITE['email'], href=f"mailto:{SITE['email']}", variant='primary', icon='mail')
                    Button('LinkedIn', href=SITE['linkedin_url'], variant='secondary', icon='north_east')
                    Button('GitHub', href=SITE['github_url'], variant='secondary', icon='code')
                    Button('YouTube', href=SITE['youtube_url'], variant='secondary', icon='play_circle')
                    Button('Discord', href=GAME['discord_url'], variant='ghost', icon='forum')
