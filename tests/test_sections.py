from components.hero import hero, _safe_channel_picture
from components.game import game_section
from components.contact import contact_section
from components.ui.badge import Badge
from components.ui.button import Button
from components.ui.card import Card
from components.ui.section import Section, SectionHeader
from config.settings import GAME_STATS, SITE
from pages.home import home_page


class StubHeroYouTubeService:
    def get_channel_picture_url(self) -> str:
        return 'https://example.com/avatar.jpg'

    def get_latest_videos(self, max_results: int = 3):
        return [
            {
                'videoId': 'nFhj-jDsG_s',
                'title': 'Mes 7 conseils pour faire du "Clean Vibe Code"',
                'thumbnail': 'https://example.com/thumb.jpg',
                'publishedAt': '2026-08-01T08:00:29Z',
            }
        ]


class FailingHeroYouTubeService:
    def get_channel_picture_url(self) -> str:
        raise RuntimeError('API error')


def test_hero_runs_with_picture():
    hero(StubHeroYouTubeService())


def test_hero_runs_when_api_fails():
    fallback_url = _safe_channel_picture(FailingHeroYouTubeService())
    assert fallback_url.startswith('https://')
    assert fallback_url == SITE['avatar_url']
    hero(FailingHeroYouTubeService())


def test_game_section_runs_and_has_stats():
    assert len(GAME_STATS) == 6
    for stat in GAME_STATS:
        assert stat['value']
        assert stat['label']
    game_section()


def test_contact_section_runs():
    assert SITE['email']
    contact_section()


def test_ui_primitives_run():
    Badge('Clean Code', variant='neutral', dot=True)
    Badge('Nouveau', variant='accent')
    Button('Action', variant='primary')
    Button('Lien', href='https://example.com', variant='secondary', icon='north_east')
    Card(featured=True)
    Section(id='test-sec')
    SectionHeader('Titre', 'Sous-titre', eyebrow='Eyebrow')


def test_home_page_runs_with_injected_service():
    home_page(StubHeroYouTubeService())

