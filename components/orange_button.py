from nicegui import ui
from config.settings import COLORS
from typing import Callable, Optional

def OrangeButton(text: str, on_click: Optional[Callable] = None, outline: bool = True, icon: Optional[str] = None) -> None:
    classes = 'font-semibold rounded-full px-6'
    if outline:
        classes += ' border border-orange-500 bg-white text-orange-500'
    else:
        classes += ' bg-orange-500 text-white'
    ui.button(text, on_click=on_click, color=COLORS['primary'], icon=icon).classes(classes) 