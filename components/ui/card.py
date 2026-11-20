from nicegui import ui

BASE_CARD_CLASSES = (
    'w-full p-0 gap-0 rounded-3xl bg-white/95 backdrop-blur-xs '
    'shadow-[0_2px_16px_-4px_rgba(15,23,42,0.06)] '
    'hover:shadow-[0_16px_36px_-8px_rgba(15,23,42,0.10)] '
    'transition-all duration-300'
)


def Card(featured: bool = False, extra_classes: str = '') -> ui.card:
    border = 'border-2 border-[#0066CC]/40' if featured else 'border border-slate-200/80'
    card = ui.card().classes(f'{BASE_CARD_CLASSES} {border} {extra_classes}'.strip())
    card.props('flat')
    return card
