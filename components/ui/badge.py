from typing import Literal
from nicegui import ui

BadgeVariant = Literal['neutral', 'accent', 'success', 'mono']

VARIANT_STYLES = {
    'neutral': 'bg-slate-100/90 text-slate-700 border border-slate-200/80 font-medium',
    'accent': 'bg-blue-600 text-white border border-blue-600 font-semibold shadow-2xs',
    'success': 'bg-emerald-50 text-emerald-800 border border-emerald-200 font-medium',
    'mono': 'bg-slate-100/80 text-slate-700 border border-slate-200/70 font-mono',
}


def Badge(text: str, variant: BadgeVariant = 'neutral', dot: bool = False) -> ui.row:
    style = VARIANT_STYLES.get(variant, VARIANT_STYLES['neutral'])
    classes = f'inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs {style}'
    with ui.row().classes(classes) as badge:
        if dot:
            ui.element('span').classes('w-2 h-2 rounded-full bg-emerald-500 shrink-0')
        ui.label(text)
    return badge
