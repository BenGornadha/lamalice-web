import pytest
from components.videos import videos_section


class FakeYouTubeService:
    def get_latest_videos(self, max_results=3):
        return [{'videoId': '1', 'title': 'Titre', 'thumbnail': 'http://thumb'}]


def test_videos_section_runs():
    try:
        videos_section(FakeYouTubeService())
    except Exception as e:
        pytest.fail(f'videos_section() a levé une exception : {e}')
