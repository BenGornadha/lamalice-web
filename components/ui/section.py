from nicegui import ui
from typing import Optional

def Section(bg_color: str = 'transparent', id: Optional[str] = None) -> ui.column:
    """
    A standard section container with consistent padding and max-width.
    """
    with ui.row().classes(f'w-full justify-center {bg_color}').props(f'id="{id}"' if id else ''):
        # The inner container controls the max-width and padding
        return ui.column().classes('w-full max-w-screen-xl px-6 py-24 gap-12')

def SectionHeader(title: str, subtitle: str) -> ui.column:
    """
    A standard section header: title + subtitle.
    """
    with ui.column().classes('gap-2') as column:
        ui.label(title).classes('text-3xl font-bold tracking-tight text-gray-900')
        ui.label(subtitle).classes('text-lg text-gray-500')
    return column
