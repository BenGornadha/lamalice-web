from nicegui import ui
from config.settings import COLORS

GLOBAL_HEAD_HTML = f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --lm-bg: {COLORS['background']};
    --lm-accent: {COLORS['accent']};
  }}
  html {{
    scroll-behavior: smooth;
    scroll-padding-top: 5.5rem;
  }}
  body {{
    background-color: var(--lm-bg);
    background-image:
      radial-gradient(at 15% 10%, rgba(0, 102, 204, 0.06) 0px, transparent 45%),
      radial-gradient(at 85% 25%, rgba(15, 23, 42, 0.04) 0px, transparent 45%);
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: {COLORS['text_primary']};
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  .font-mono {{
    font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace !important;
  }}
  :where(a:any-link, button):focus-visible {{
    outline: 2px solid var(--lm-accent);
    outline-offset: 2px;
  }}
  @media (prefers-reduced-motion: no-preference) {{
    .bento-lift {{
      transition: transform 0.24s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.24s ease;
    }}
    .bento-lift:hover {{
      transform: translateY(-3px);
    }}
  }}
</style>
"""


def apply_global_theme() -> None:
    ui.colors(
        primary=COLORS['accent'],
        secondary=COLORS['text_secondary'],
        accent=COLORS['accent'],
    )
    ui.add_head_html(GLOBAL_HEAD_HTML)
