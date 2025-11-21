from nicegui import ui
from typing import Callable, Optional, Literal
from config.settings import COLORS

Variant = Literal['primary', 'secondary', 'ghost']

def Button(text: str, on_click: Optional[Callable] = None, variant: Variant = 'primary', icon: Optional[str] = None, href: Optional[str] = None) -> ui.button:
    """
    A minimalist button component with Apple-style variants.
    """
    base_classes = 'rounded-full px-6 py-2 text-sm font-medium transition-all duration-200 ease-in-out'
    
    if variant == 'primary':
        # Dark button (or Accent color)
        classes = f'{base_classes} bg-gray-900 text-white hover:bg-gray-800 shadow-sm hover:shadow-md'
    elif variant == 'secondary':
        # Light gray button
        classes = f'{base_classes} bg-gray-100 text-gray-900 hover:bg-gray-200'
    else: # ghost
        # Text only, hover effect
        classes = f'{base_classes} text-gray-600 hover:text-gray-900 hover:bg-gray-50'

    if href:
        # Use ui.link for native navigation (better for SEO, middle-click, mailto)
        # We wrap the content in a link but style it like a button
        with ui.link(target=href).classes(classes + ' no-underline flex items-center justify-center gap-2') as link:
            if icon:
                ui.icon(icon).classes('text-lg')
            ui.label(text)
        return link

    # Default button behavior
    btn = ui.button(text, on_click=on_click, icon=icon).classes(classes)
    
    # Remove default NiceGUI styling to have full control
    btn.props('flat unelevated no-caps')
    
    return btn
