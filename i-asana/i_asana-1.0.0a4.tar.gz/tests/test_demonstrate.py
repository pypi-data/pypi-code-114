"""Test functions for i_asana.py.
"""
from aracnid_logger import Logger
import pytest

import i_asana as asn

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
project_id = '1201859291658493'  # BrewOps

@pytest.fixture(name='asana')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return asn.AsanaInterface()

def test_get_project_by_id(asana):
    """Tests project get functionality.
    """
    result = asana.client.projects.get_project(project_id)

    assert result['gid'] == project_id
    assert result['name'] == 'BrewOps'

def test_get_tasks_for_project(asana):
    """Tests get_tasks_for_project functionality.
    """
    tasks = asana.client.tasks.get_tasks_for_project(project_id)
    for task in tasks:
        assert task
        logger.info(task['name'])

def test_get_section_id_from_task(asana):
    """Tests get_task functionality.
    """
    task = asana.client.tasks.get_task('1201958049378915')
    section_id = task['memberships'][0]['section']['gid']
    section_name = task['memberships'][0]['section']['name']

    assert section_id
    assert section_name == 'Fermenting'

    task = asana.client.tasks.get_task('1201958049378904')
    section_id = task['memberships'][0]['section']['gid']
    section_name = task['memberships'][0]['section']['name']

    assert section_id
    assert section_name == 'Serving'
