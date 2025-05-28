import os
import sys
import pytest
import pickle
import time
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.youtube import YouTubeService, YouTubeCache, YouTubeAPIClient

@pytest.fixture(autouse=True)
def cleanup_cache():
    # Sauvegarde l'état du cache et nettoie avant chaque test
    cache_path = YouTubeCache.CACHE_PATH
    backup = None
    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as f:
            backup = f.read()
        os.remove(cache_path)
    yield
    if backup:
        with open(cache_path, 'wb') as f:
            f.write(backup)
    elif os.path.exists(cache_path):
        os.remove(cache_path)

def test_youtube_api_client_fetches_videos():
    client = YouTubeAPIClient()
    videos = client.fetch_videos(max_results=2)
    assert isinstance(videos, list)
    for v in videos:
        assert 'title' in v and 'videoId' in v and 'thumbnail' in v

def test_youtube_cache_write_and_read():
    cache = YouTubeCache()
    data = [{'title': 'A', 'videoId': '1', 'thumbnail': 't', 'publishedAt': 'now'}]
    cache.write(data)
    assert cache.read() == data

def test_youtube_service_uses_cache(monkeypatch):
    # On simule un cache valide
    cache = YouTubeCache()
    fake_data = [{'title': 'B', 'videoId': '2', 'thumbnail': 't', 'publishedAt': 'now'}]
    cache.write(fake_data)
    monkeypatch.setattr(YouTubeCache, 'is_valid', lambda self: True)
    service = YouTubeService()
    result = service.get_latest_videos(max_results=1)
    assert result[0]['title'] == 'B'

def test_youtube_service_refreshes_cache(monkeypatch):
    # On simule un cache invalide et on mock l'API
    monkeypatch.setattr(YouTubeCache, 'is_valid', lambda self: False)
    monkeypatch.setattr(YouTubeAPIClient, 'fetch_videos', lambda self, max_results: [{'title': 'C', 'videoId': '3', 'thumbnail': 't', 'publishedAt': 'now'}])
    service = YouTubeService()
    result = service.get_latest_videos(max_results=1)
    assert result[0]['title'] == 'C'

def test_get_channel_picture_url():
    service = YouTubeService()
    url = service.get_channel_picture_url()
    assert isinstance(url, str)
    assert url.startswith('http') 