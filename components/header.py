from nicegui import ui
from components.ui.badge import Badge
from components.ui.button import Button
from config.settings import GAME, SITE


def scroll_to(section_id: str) -> None:
    js = f"document.getElementById('{section_id}')?.scrollIntoView({{ behavior: 'smooth' }});"
    ui.run_javascript(js)


def _render_brand() -> None:
    with ui.row().classes('items-center gap-3 cursor-pointer').on('click', lambda: scroll_to('hero')):
        with ui.element('div').classes(
            'w-9 h-9 rounded-xl bg-slate-900 text-white font-bold text-xs '
            'flex items-center justify-center shadow-xs'
        ):
            ui.label('LM')
        ui.label(SITE['name']).classes('text-lg font-bold tracking-tight text-slate-900')
        with ui.element('div').classes('hidden md:block'):
            Badge('Clean Code · TDD · Architecture', variant='neutral', dot=True)


def _render_navigation() -> None:
    with ui.row().classes('items-center gap-1 flex-wrap justify-end'):
        Button('À propos', on_click=lambda: scroll_to('hero'), variant='ghost')
        Button('Vidéos', on_click=lambda: scroll_to('videos'), variant='ghost')
        Button('Prompts IA', on_click=lambda: scroll_to('prompts'), variant='ghost')
        Button(GAME['name'], on_click=lambda: scroll_to('game'), variant='ghost')
        Button('Contact', on_click=lambda: scroll_to('contact'), variant='primary')


def header() -> None:
    header_classes = 'w-full bg-white/80 backdrop-blur-xl border-b border-slate-200/80 z-50'
    with ui.header().classes(header_classes):
        with ui.row().classes('w-full max-w-6xl mx-auto items-center justify-between py-3 px-6'):
            _render_brand()
            _render_navigation()
