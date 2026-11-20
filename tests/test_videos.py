import pytest
from components.videos import videos_section, format_published_date


class FakeYouTubeService:
    def get_latest_videos(self, max_results=3):
        return [
            {
                'videoId': '1',
                'title': 'Titre 1',
                'thumbnail': 'http://thumb1',
                'publishedAt': '2026-08-01T08:00:29Z',
            },
            {
                'videoId': '2',
                'title': 'Titre 2',
                'thumbnail': 'http://thumb2',
                'publishedAt': '2026-03-02T16:08:54Z',
            },
        ]


class EmptyYouTubeService:
    def get_latest_videos(self, max_results=3):
        return []


def test_videos_section_runs():
    videos_section(FakeYouTubeService())


def test_videos_section_handles_empty_list():
    videos_section(EmptyYouTubeService())


def test_format_published_date_iso():
    assert format_published_date('2026-08-01T08:00:29Z') == '01 août 2026'
    assert format_published_date('2026-03-02T16:08:54Z') == '02 mars 2026'


def test_format_published_date_fallback():
    assert format_published_date('') == ''
    assert format_published_date('now') == ''

