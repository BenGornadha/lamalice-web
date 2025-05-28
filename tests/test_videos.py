import pytest
from components.videos import videos_section

def test_videos_section_runs():
    try:
        videos_section()
    except Exception as e:
        pytest.fail(f'videos_section() a levé une exception : {e}') 