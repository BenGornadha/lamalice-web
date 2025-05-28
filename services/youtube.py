import os
import httpx
from typing import List, Dict
import html
import pickle
import time
from dotenv import load_dotenv

load_dotenv()
TIMEOUT=10

class YouTubeAPIClient:
    
    def __init__(self):
        self._api_key = os.getenv('YOUTUBE_API_KEY', '')
        self._channel_id = os.getenv('YOUTUBE_CHANNEL_ID', '')

    def fetch_videos(self, max_results: int = 3) -> List[Dict]:
        url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'key': self._api_key,
            'channelId': self._channel_id,
            'part': 'snippet',
            'order': 'date',
            'maxResults': 20,
            'type': 'video',
        }
        response = httpx.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        items = response.json().get('items', [])
        videos = []
        for item in items:
            if item['snippet'].get('channelId') != self._channel_id:
                continue
            video_id = item['id']['videoId']
            video_details = self.get_video_details(video_id)
            duration = video_details.get('contentDetails', {}).get('duration', '')
            thumb = item['snippet']['thumbnails']['high']
            width, height = thumb.get('width', 0), thumb.get('height', 0)
            is_vertical = height > width
            if not self.is_short(duration) and not is_vertical:
                videos.append({
                    'title': html.unescape(item['snippet']['title']),
                    'videoId': video_id,
                    'thumbnail': thumb['url'],
                    'publishedAt': item['snippet']['publishedAt'],
                })
            if len(videos) >= max_results:
                break
        return videos

    def get_video_details(self, video_id: str) -> Dict:
        url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
            'id': video_id,
            'part': 'contentDetails',
            'key': self._api_key,
        }
        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
        items = response.json().get('items', [])
        return items[0] if items else {}

    @staticmethod
    def is_short(duration: str) -> bool:
        import re
        match = re.match(r'PT((\d+)M)?((\d+)S)?', duration)
        minutes = int(match.group(2)) if match and match.group(2) else 0
        seconds = int(match.group(4)) if match and match.group(4) else 0
        total_seconds = minutes * 60 + seconds
        return total_seconds < 180

    def get_channel_picture_url(self) -> str:
        url = 'https://www.googleapis.com/youtube/v3/channels'
        params = {
            'part': 'snippet',
            'id': self._channel_id,
            'key': self._api_key,
        }
        response = httpx.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        items = data.get('items', [])
        if items:
            thumbs = items[0]['snippet']['thumbnails']
            return thumbs.get('high', thumbs.get('default', {})).get('url', '')
        return ''

class YouTubeCache:
    CACHE_PATH = 'youtube_videos_cache.pkl'
    CACHE_TTL = 24 * 3600

    def is_valid(self) -> bool:
        if not os.path.exists(self.CACHE_PATH):
            return False
        with open(self.CACHE_PATH, 'rb') as f:
            cache = pickle.load(f)
        return time.time() - cache['timestamp'] < self.CACHE_TTL

    def read(self) -> List[Dict]:
        with open(self.CACHE_PATH, 'rb') as f:
            cache = pickle.load(f)
        return cache['videos']

    def write(self, videos: List[Dict]) -> None:
        with open(self.CACHE_PATH, 'wb') as f:
            pickle.dump({'timestamp': time.time(), 'videos': videos}, f)

class YouTubeService:
    def __init__(self):
        self.api = YouTubeAPIClient()
        self.cache = YouTubeCache()

    def get_latest_videos(self, max_results: int = 3) -> List[Dict]:
        if self.cache.is_valid():
            return self.cache.read()[:max_results]
        videos = self.api.fetch_videos(max_results)
        self.cache.write(videos)
        return videos[:max_results]

    def get_channel_picture_url(self) -> str:
        return self.api.get_channel_picture_url()