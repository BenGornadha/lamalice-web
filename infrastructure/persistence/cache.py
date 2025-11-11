import os
import pickle
import time
from typing import List, Dict


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
