import os
import httpx
from typing import List, Dict
import html
import pickle
import time
from dotenv import load_dotenv

from services.youtube.api_client import YouTubeAPIClient

from infrastructure.persistence.cache import YouTubeCache

load_dotenv()
TIMEOUT=10


class YouTubeService:
    def __init__(self, api_client: YouTubeAPIClient, cache: YouTubeCache) -> None:
        self.api = api_client
        self.cache = cache

    def refresh_cache(self, force: bool = False) -> None:
        """
        Forces a cache refresh by calling the API.
        Protected by a minimum interval to avoid spamming the API on failures.
        """
        MIN_UPDATE_INTERVAL = 60 * 5  # 5 minutes minimum between updates
        last_update = self.cache.get_timestamp()
        
        if not force and (time.time() - last_update < MIN_UPDATE_INTERVAL):
            print(f"Skipping cache refresh (last update was {time.time() - last_update:.0f}s ago)")
            return

        print("Refreshing YouTube cache...")
        try:
            videos = self.api.fetch_videos(max_results=50) # Fetch more to be safe
            self.cache.write(videos)
            print("YouTube cache refreshed successfully.")
        except Exception as e:
            print(f"Error refreshing YouTube cache: {e}")
            # Circuit breaker: update timestamp to prevent immediate retry
            self.cache.touch()
            print("Cache touched to prevent immediate retry.")

    def get_latest_videos(self, max_results: int = 3) -> List[Dict]:
        if self.cache.is_valid():
            try:
                return self.cache.read()[:max_results]
            except:
                pass # If read fails, try to refresh
        
        # If cache is invalid, refresh it
        self.refresh_cache()
        
        # Return whatever is in cache (old data or empty if failed)
        try:
            return self.cache.read()[:max_results]
        except:
            return []

    def get_channel_picture_url(self) -> str:
        return self.api.get_channel_picture_url()