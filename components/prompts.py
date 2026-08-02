from nicegui import ui
from components.ui.section import Section, SectionHeader
from components.ui.card import Card
from config.prompts import PROMPTS

def prompts_section() -> None:
    with Section(id='prompts', bg_color='bg-white'):
        with ui.column().classes('w-full gap-8'):
            SectionHeader('Mes Prompts', "Les prompts que j'utilise au quotidien avec mes assistants IA.")

            with ui.grid(columns='repeat(auto-fit, minmax(320px, 1fr))').classes('w-full gap-6'):
                for prompt in PROMPTS:
                    prompt_card(prompt)

def prompt_card(prompt: dict) -> None:
    def copy() -> None:
        ui.clipboard.write(prompt['content'])
        ui.notify('Prompt copié !', type='positive')

    with Card():
        with ui.column().classes('w-full p-5 gap-3'):
            with ui.row().classes('w-full items-center justify-between no-wrap'):
                ui.label(prompt['title']).classes('text-base font-semibold text-gray-900')
                ui.button(icon='content_copy', on_click=copy).props('flat round dense').classes('text-gray-400 hover:text-gray-900')

            ui.label(prompt['description']).classes('text-sm text-gray-500')

            with ui.element('div').classes('w-full max-h-80 overflow-y-auto rounded-xl bg-gray-50 p-4 border border-gray-100'):
                ui.label(prompt['content']).classes('text-xs text-gray-700 whitespace-pre-wrap leading-relaxed')
