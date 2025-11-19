from nicegui import ui
from typing import Optional

def Section(bg_color: str = 'transparent', id: Optional[str] = None) -> ui.column:
    """
    A standard section container with consistent padding and max-width.
    """
    with ui.row().classes(f'w-full justify-center {bg_color}').props(f'id="{id}"' if id else ''):
        # The inner container controls the max-width and padding
        return ui.column().classes('w-full max-w-screen-xl px-6 py-24 gap-12')
