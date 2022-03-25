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

def test_init_asana(asana):
    """Tests Asana initialization.
    """
    assert asana

    asana.client.options['client_name'] = 'brewbot'
    me = asana.client.users.me()

    assert me['workspaces'][0]['name'] == 'lakeannebrewhouse.com'

def test_create_task_no_due_date(asana):
    """Tests create_task() function.
    """
    task = asana.create_task(
        name='CREATE: no-due-date',
        project_id=PROJECT_ID
    )

    assert task

def test_create_task_due_date(asana):
    """Tests create_task() function.
    """
    start_date = date.today()
    due_date = start_date + timedelta(days=5)
    due_start_str = start_date.isoformat()

    task = asana.create_task(
        name='CREATE: start-date',
        start=start_date,
        due=due_date,
        project_id=PROJECT_ID
    )

    assert task
    assert task['start_on'] == due_start_str

def test_create_task_due_datetime(asana):
    """Tests create_task() function.
    """
    due_datetime = datetime.now().replace(microsecond=0).astimezone()
    due_datetime_str = due_datetime.astimezone(utc).isoformat()

    task = asana.create_task(
        name='CREATE: due-datetime',
        due=due_datetime,
        project_id=PROJECT_ID
    )

    assert task
    assert task['due_at'][0:19] == due_datetime_str[0:19]

def test_create_task_start_date(asana):
    """Tests create_task() function.
    """
    due_date = date.today()
    due_date_str = due_date.isoformat()

    task = asana.create_task(
        name='CREATE: due-date',
        due=due_date,
        project_id=PROJECT_ID
    )

    assert task
    assert task['due_on'] == due_date_str

def test_create_task_in_section(asana):
    """Tests create_task() function.
    """
    task = asana.create_task(
        name='CREATE: in-section',
        project_id=PROJECT_ID,
        section_id=SECTION_ID
    )

    assert task
    assert task['memberships'][0]['section']['gid'] == SECTION_ID

def test_create_subtask_in_task(asana):
    """Tests create_task() function.
    """
    parent_id = '1202019477793842'
    task = asana.create_task(
        name='CREATE: subtask',
        project_id=PROJECT_ID,
        section_id=SECTION_ID,
        parent_id=parent_id
    )

    assert task
    assert task['parent']['gid'] == parent_id

def test_read_task(asana):
    """Tests read_task() function.
    """
    task_id = '1202021989637892'
    task = asana.read_task(task_id=task_id)

    assert task
    assert task['name'] == 'READ: no-due-date'

def test_get_due_date(asana):
    """Tests the ged_due_date() function.
    """
    task_id = '1202019477793837'
    task = asana.read_task(task_id=task_id)
    due_date = asana.get_due_date(task)

    assert due_date
    assert isinstance(due_date, date)

def test_get_due_datetime(asana):
    """Tests the ged_due_datetime() function.
    """
    task_id = '1202019477793839'
    task = asana.read_task(task_id=task_id)
    due_datetime = asana.get_due_datetime(task)

    assert due_datetime
    assert task.get('due_at')
    assert isinstance(due_datetime, datetime)

def test_get_due_datetime_no_due_at(asana):
    """Tests the ged_due_datetime() function.
    """
    task_id = '1202019477793837'
    task = asana.read_task(task_id=task_id)
    due_datetime = asana.get_due_datetime(task)

    assert due_datetime
    assert not task.get('due_at')
    assert isinstance(due_datetime, datetime)
    assert due_datetime.hour == 12
    assert due_datetime.minute == 0

def test_update_task(asana):
    """Tests update_task() function.
    """
    task = asana.create_task(
        name='UPDATE: created',
        project_id=PROJECT_ID
    )
    assert task['name'] == 'UPDATE: created'

    task_id = task['gid']
    task = asana.update_task(
        task_id=task_id,
        fields={
            'name': 'UPDATE: updated'
        }
    )

    assert task['name'] == 'UPDATE: updated'

def test_delete_task(asana):
    """Tests delete_task() function.
    """
    task = asana.create_task(
        name='DELETE: created',
        project_id=PROJECT_ID
    )
    assert task['name'] == 'DELETE: created'

    task_id = task['gid']
    task = asana.delete_task(task_id=task_id)
