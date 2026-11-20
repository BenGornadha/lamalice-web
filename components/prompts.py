from typing import Dict
from nicegui import ui
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section, SectionHeader
from config.prompts import PROMPTS


def _copy_prompt(content: str) -> None:
    ui.clipboard.write(content)
    ui.notify('Prompt copié dans le presse-papier !', type='positive')


def _build_prompt_dialog(prompt: Dict) -> ui.dialog:
    with ui.dialog() as dialog, Card(extra_classes='max-w-2xl w-full p-6 md:p-8 gap-4'):
        with ui.row().classes('w-full items-start justify-between gap-4 no-wrap'):
            with ui.column().classes('gap-1'):
                ui.label(prompt['title']).classes('text-xl font-bold text-slate-900')
                ui.label(prompt['description']).classes('text-xs text-slate-500')
            ui.button(icon='close', on_click=dialog.close).props('flat round dense')
        with ui.element('div').classes(
            'w-full max-h-96 overflow-y-auto rounded-2xl bg-slate-50 p-4 border border-slate-200/80'
        ):
            ui.label(prompt['content']).classes('text-xs font-mono text-slate-700 whitespace-pre-wrap leading-relaxed')
        with ui.row().classes('w-full justify-end gap-2 pt-2'):
            Button('Fermer', on_click=dialog.close, variant='ghost')
            Button('Copier le prompt', on_click=lambda: _copy_prompt(prompt['content']), variant='primary', icon='content_copy')
    return dialog


def _render_prompt_tags(tags: list) -> None:
    if not tags:
        return
    with ui.row().classes('w-full gap-1.5 flex-wrap'):
        for tag in tags:
            Badge(tag, variant='mono')


def _render_prompt_preview(content: str) -> None:
    box_classes = 'w-full max-h-52 overflow-y-auto rounded-2xl bg-slate-50/90 p-4 border border-slate-200/80'
    with ui.element('div').classes(box_classes):
        ui.label(content).classes('text-xs font-mono text-slate-700 whitespace-pre-wrap leading-relaxed')


def prompt_card(prompt: Dict) -> None:
    dialog = _build_prompt_dialog(prompt)
    with Card(extra_classes='p-6 md:p-7 flex flex-col justify-between gap-5 bento-lift'):
        with ui.column().classes('w-full gap-3'):
            with ui.row().classes('w-full items-start justify-between gap-2'):
                ui.label(prompt['title']).classes('text-lg font-bold text-slate-900')
                if prompt.get('badge'):
                    Badge(prompt['badge'], variant='neutral')
            ui.label(prompt['description']).classes('text-sm text-slate-500')
            _render_prompt_tags(prompt.get('tags', []))
            _render_prompt_preview(prompt['content'])
        with ui.row().classes('w-full items-center justify-between gap-2 pt-3 border-t border-slate-100'):
            Button('Lire en plein écran', on_click=dialog.open, variant='ghost', icon='open_in_full')
            Button('Copier', on_click=lambda: _copy_prompt(prompt['content']), variant='primary', icon='content_copy')


def prompts_section() -> None:
    with Section(id='prompts'):
        SectionHeader(
            'Mes Prompts Système',
            "Les instructions que j'injecte au quotidien dans mes assistants IA pour garantir un code propre, modulaire et testé.",
            eyebrow='Boîte à outils IA',
        )
        with ui.element('div').classes('w-full grid grid-cols-1 lg:grid-cols-2 gap-6'):
            for prompt in PROMPTS:
                prompt_card(prompt)
