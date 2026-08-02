from components.prompts import prompts_section
from config.prompts import PROMPTS

def test_prompts_section_runs():
    prompts_section()

def test_prompts_have_content():
    assert PROMPTS
    for prompt in PROMPTS:
        assert prompt['title']
        assert prompt['description']
        assert len(prompt['content']) > 100
