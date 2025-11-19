import os
from nicegui import app, ui
from apscheduler.schedulers.background import BackgroundScheduler
from pages.home import home_page
from services.youtube.youtube import YouTubeService
from infrastructure.persistence.cache import YouTubeCache
from services.youtube.api_client import YouTubeAPIClient

# Initialize services for background tasks
youtube_service = YouTubeService(api_client=YouTubeAPIClient(), cache=YouTubeCache())

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the job to run every day at 9:00 AM
    scheduler.add_job(lambda: youtube_service.refresh_cache(force=True), 'cron', hour=9, minute=0)
    scheduler.start()
    print("Scheduler started: YouTube cache will refresh daily at 9:00 AM.")

app.on_startup(start_scheduler)
app.on_startup(lambda: home_page())

port = int(os.getenv("PORT", "8080"))
ui.run(
    title='LaMaliceCode - Portfolio',
    host="0.0.0.0",
    port=port,
    reload=False,
    dark=False
)
