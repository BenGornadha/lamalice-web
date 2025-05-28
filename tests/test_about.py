import pytest
from components.about import about_section

def test_about_section_runs():
    try:
        about_section()
    except Exception as e:
        pytest.fail(f'about_section() a levé une exception : {e}') 