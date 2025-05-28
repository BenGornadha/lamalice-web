import pytest
from components.header import header

def test_header_runs():
    try:
        header()
    except Exception as e:
        pytest.fail(f'header() a levé une exception : {e}') 