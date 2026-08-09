import os
import sys
import pytest
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.youtube.youtube import YouTubeService
from services.youtube.api_client import YouTubeAPIClient
from infrastructure.persistence.cache import YouTubeCache


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


def _fake_response(payload):
    resp = Mock()
    resp.json.return_value = payload
    resp.raise_for_status.return_value = None
    return resp


class StubAPIClient:
    def fetch_videos(self, max_results=3):
        return [{'title': 'C', 'videoId': '3', 'thumbnail': 't', 'publishedAt': 'now'}]

    def get_channel_picture_url(self):
        return 'http://pic'


def test_youtube_api_client_fetches_videos(monkeypatch):
    monkeypatch.setenv('YOUTUBE_CHANNEL_ID', 'chan')
    client = YouTubeAPIClient()
    search = {'items': [{
        'id': {'videoId': 'abc'},
        'snippet': {
            'channelId': 'chan',
            'title': 'Ma vid&eacute;o',
            'publishedAt': '2026-01-01T00:00:00Z',
            'thumbnails': {'high': {'url': 'http://thumb', 'width': 1280, 'height': 720}},
        },
    }]}
    details = {'items': [{'contentDetails': {'duration': 'PT10M0S'}}]}
    with patch('services.youtube.api_client.httpx.get',
               side_effect=[_fake_response(search), _fake_response(details)]):
        videos = client.fetch_videos(max_results=2)
    assert isinstance(videos, list)
    assert videos
    for v in videos:
        assert 'title' in v and 'videoId' in v and 'thumbnail' in v


def test_youtube_cache_write_and_read():
    cache = YouTubeCache()
    data = [{'title': 'A', 'videoId': '1', 'thumbnail': 't', 'publishedAt': 'now'}]
    cache.write(data)
    assert cache.read() == data


def test_youtube_service_uses_cache():
    cache = YouTubeCache()
    cache.write([{'title': 'B', 'videoId': '2', 'thumbnail': 't', 'publishedAt': 'now'}])
    service = YouTubeService(StubAPIClient(), cache)
    result = service.get_latest_videos(max_results=1)
    assert result[0]['title'] == 'B'


def test_youtube_service_refreshes_cache():
    # Pas de fichier de cache : invalide, timestamp 0 -> refresh via l'API stub
    service = YouTubeService(StubAPIClient(), YouTubeCache())
    result = service.get_latest_videos(max_results=1)
    assert result[0]['title'] == 'C'


def test_get_channel_picture_url():
    payload = {'items': [{'snippet': {'thumbnails': {'high': {'url': 'http://pic'}}}}]}
    with patch('services.youtube.api_client.httpx.get', return_value=_fake_response(payload)):
        url = YouTubeAPIClient().get_channel_picture_url()
    assert isinstance(url, str)
    assert url.startswith('http')
