from typing import Optional
from nicegui import ui


def Section(
    bg_color: str = 'transparent',
    id: Optional[str] = None,
    spacing: str = 'py-14 md:py-20',
) -> ui.column:
    row = ui.row().classes(f'w-full justify-center {bg_color}')
    if id:
        row.props(f'id="{id}"')
    with row:
        return ui.column().classes(f'w-full max-w-6xl px-6 {spacing} gap-8')


def SectionHeader(title: str, subtitle: str, eyebrow: Optional[str] = None) -> ui.column:
    with ui.column().classes('gap-1.5') as column:
        if eyebrow:
            ui.label(eyebrow).classes('text-xs font-mono font-semibold uppercase tracking-widest text-[#0066CC]')
        ui.label(title).classes('text-3xl md:text-4xl font-bold tracking-tight text-slate-900')
        ui.label(subtitle).classes('text-base md:text-lg text-slate-500 max-w-2xl leading-relaxed')
    return column
