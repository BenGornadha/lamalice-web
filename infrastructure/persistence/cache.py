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
            
    def get_timestamp(self) -> float:
        if not os.path.exists(self.CACHE_PATH):
            return 0.0
        try:
            with open(self.CACHE_PATH, 'rb') as f:
                cache = pickle.load(f)
            return cache.get('timestamp', 0.0)
        except:
            return 0.0

    def touch(self) -> None:
        """Updates the timestamp without changing the data (if possible), or writes empty if missing."""
        if os.path.exists(self.CACHE_PATH):
            try:
                videos = self.read()
            except:
                videos = []
        else:
            videos = []
        self.write(videos)
