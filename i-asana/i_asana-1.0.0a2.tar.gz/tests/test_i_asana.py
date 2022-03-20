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

def test_init_asana(asana):
    """Tests Asana initialization.
    """
    assert asana

    asana.client.options['client_name'] = 'brewbot'
    me = asana.client.users.me()

    assert me['workspaces'][0]['name'] == 'lakeannebrewhouse.com'

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
