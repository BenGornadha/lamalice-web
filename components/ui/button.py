from typing import Callable, Literal, Optional
from nicegui import ui

Variant = Literal['primary', 'secondary', 'accent', 'ghost']

BASE_CLASSES = (
    'rounded-full px-5 py-2.5 text-sm font-semibold '
    'transition-all duration-200 ease-out cursor-pointer'
)

VARIANT_CLASSES = {
    'primary': 'bg-slate-900 text-white hover:bg-slate-800 shadow-sm hover:shadow-md',
    'secondary': 'bg-white text-slate-900 border border-slate-200/90 hover:bg-slate-50 hover:border-slate-300 shadow-2xs',
    'accent': 'bg-[#0066CC] text-white hover:bg-[#0055B3] shadow-sm hover:shadow-md',
    'ghost': 'text-slate-600 hover:text-slate-900 hover:bg-slate-100/80 px-4 py-2',
}


def _build_classes(variant: Variant) -> str:
    variant_style = VARIANT_CLASSES.get(variant, VARIANT_CLASSES['primary'])
    return f'{BASE_CLASSES} {variant_style}'


def _render_link(text: str, href: str, classes: str, icon: Optional[str]) -> ui.link:
    open_new_tab = href.startswith('http')
    link_classes = f'{classes} no-underline inline-flex items-center justify-center gap-2'
    with ui.link(target=href, new_tab=open_new_tab).classes(link_classes) as link:
        if icon:
            ui.icon(icon).classes('text-base')
        ui.label(text)
    return link


def Button(
    text: str,
    on_click: Optional[Callable] = None,
    variant: Variant = 'primary',
    icon: Optional[str] = None,
    href: Optional[str] = None,
):
    classes = _build_classes(variant)
    if href:
        return _render_link(text, href, classes, icon)
    btn = ui.button(text, on_click=on_click, icon=icon).classes(classes)
    btn.props('flat unelevated no-caps')
    return btn
