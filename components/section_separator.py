from nicegui import ui
from config.settings import COLORS

def SectionSeparator() -> None:
    ui.separator().classes(f'w-12 bg-[{COLORS["primary"]}] mb-4') 