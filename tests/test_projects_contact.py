import pytest
from components.projects_contact import projects_contact_section

def test_projects_contact_section_runs():
    try:
        projects_contact_section()
    except Exception as e:
        pytest.fail(f'projects_contact_section() a levé une exception : {e}') 