from nicegui import ui

def Card() -> ui.card:
    """
    A minimalist card with subtle hover effects.
    """
    return ui.card().classes('w-full p-0 gap-0 rounded-2xl bg-white shadow-sm hover:shadow-md transition-shadow duration-300 border border-gray-100')
