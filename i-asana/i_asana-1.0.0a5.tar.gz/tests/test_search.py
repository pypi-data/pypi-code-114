"""Test functions for i_asana.py.
"""
from datetime import date, datetime, timedelta
from aracnid_logger import Logger
import pytest
from pytz import utc

import i_asana as asn

# initialize logging
logger = Logger(__name__).get_logger()

# initialize module variables
PROJECT_ID = '1202019477793832'  # TEST
SECTION_ID = '1202019477793835'

@pytest.fixture(name='asana')
def fixture_asana_interface():
    """Pytest fixture to initialize and return the AsanaInterface object.
    """
    return asn.AsanaInterface()

def test_read_subtasks(asana):
    """Tests read_subtasks() function.
    """
    task_id = '1202019477793844'
    task_list = asana.read_subtasks(task_id=task_id)

    assert task_list
    assert task_list[0]['name'] == 'READ: subtask-1'

def test_read_subtask_by_name(asana):
    """Tests read_subtask_by_name() function.
    """
    task_id = '1202019477793844'
    task = asana.read_subtask_by_name(
        task_id=task_id,
        name='READ: subtask-2'
    )

    assert task
    assert task['gid'] == '1202019477793847'
