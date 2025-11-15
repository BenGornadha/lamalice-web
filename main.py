import os

from nicegui import app, ui
from pages.home import home_page

app.on_startup(lambda: home_page())

port = int(os.getenv("PORT", "8080"))
ui.run(
    title='LaMaliceCode - Portfolio',
    host="0.0.0.0",
    port=port,
    reload=True,
    dark=False
)
