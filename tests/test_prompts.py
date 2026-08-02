import pytest
from components.prompts import prompts_section, PROMPTS

def test_prompts_section_runs():
    try:
        prompts_section()
    except Exception as e:
        pytest.fail(f'prompts_section() a levé une exception : {e}')

def test_prompts_have_content():
    assert len(PROMPTS) == 2
    for prompt in PROMPTS:
        assert prompt['title']
        assert prompt['description']
        assert len(prompt['content']) > 100
