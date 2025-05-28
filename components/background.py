from nicegui import ui
from config.settings import COLORS

def background() -> None:
    # Gradient principal
    ui.html(f'''
    <div style="
        position: fixed;
        inset: 0;
        z-index: -1;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(120deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
        opacity: 0.12;
    "></div>
    ''')
    # Wave SVG overlay
    ui.html('''
    <svg style="position: fixed; top: 0; left: 0; width: 100vw; height: 220px; z-index: -1;" viewBox="0 0 1440 220" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-opacity="0.18" d="M0,160 C360,220 1080,80 1440,160 L1440,0 L0,0 Z" fill="#ff7f32"/>
      <path fill-opacity="0.10" d="M0,120 C480,200 960,40 1440,120 L1440,0 L0,0 Z" fill="#23272f"/>
    </svg>
    ''') 