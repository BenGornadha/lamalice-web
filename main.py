from nicegui import app, ui
from pages.home import home_page

app.on_startup(lambda: home_page())

ui.run(title='LaMaliceCode - Portfolio', dark=False, reload=False)
