from components.prompts import prompts_section
from config.prompts import PROMPTS


def test_prompts_section_runs():
    prompts_section()


def test_prompts_have_content_and_metadata():
    assert PROMPTS
    for prompt in PROMPTS:
        assert prompt['title']
        assert prompt['description']
        assert len(prompt['content']) > 100
        assert prompt.get('badge')
        assert isinstance(prompt.get('tags'), list)
        assert len(prompt['tags']) >= 3

