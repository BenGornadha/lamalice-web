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

    def get_latest_videos(self, max_results: int = 3) -> List[Dict]:
        if self.cache.is_valid():
            return self.cache.read()[:max_results]
        videos = self.api.fetch_videos(max_results)
        self.cache.write(videos)
        return videos[:max_results]

    def get_channel_picture_url(self) -> str:
        return self.api.get_channel_picture_url()