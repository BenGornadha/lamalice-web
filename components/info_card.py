from nicegui import ui
from typing import Optional, Callable
from config.settings import COLORS
from components.orange_button import OrangeButton

def InfoCard(title: str, description: str, button_text: Optional[str] = None, on_button_click: Optional[Callable] = None) -> None:
    with ui.card().classes('w-80 bg-white shadow-md'):
        ui.label(title).classes(f'text-lg font-bold text-[{COLORS["primary"]}]')
        ui.label(description).classes('text-gray-500')
        if button_text:
            OrangeButton(button_text, on_click=on_button_click) 