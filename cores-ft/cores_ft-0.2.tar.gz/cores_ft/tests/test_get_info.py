import pytest
from unittest import mock

from cores_ft.get_info import get_lm_sensors_info, read_cpuinfo
from cores_ft.output_msg import mount_msg_output


@pytest.fixture
def cpuinfo():
    core0 = 'cpu MHz         : 2195.050'
    core1 = 'cpu MHz         : 2000.050'
    core2 = 'cpu MHz         :   95.050'

    return '\n'.join((core0, core1, core2))


@pytest.fixture
def sensors():
    core0 = 'Core 0:        +62.0°C  (high = +85.0°C, crit = +105.0°C)'
    core1 = 'Core 1:        +60.0°C  (high = +85.0°C, crit = +105.0°C)'
    core2 = 'Core 3:        +50.0°C  (high = +85.0°C, crit = +105.0°C)'

    return '\n'.join((core0, core1, core2))


def test_read_cpuinfo(mocker, cpuinfo):

    mock_open = mock.mock_open(read_data=cpuinfo)

    mocker.patch('builtins.open', mock_open)

    freq = read_cpuinfo()

    assert len(freq) == 3
    assert freq == {'core_0': 2.19505, 'core_1': 2.00005, 'core_2': 0.09505}


def test_get_info_sensors(mocker, sensors):

    mock_open = mock.mock_open(read_data=sensors)

    mocker.patch('builtins.open', mock_open)

    temp = get_lm_sensors_info()

    assert len(temp) == 3
    assert temp == {'core_0': '+62.0°C', 'core_1': '+60.0°C',  'core_2': '+50.0°C'}


def test_print_msg(mocker, cpuinfo, sensors):

    mock_open = mock.mock_open(read_data=cpuinfo)

    mocker.patch('builtins.open', mock_open)

    freq = read_cpuinfo()

    mock_open = mock.mock_open(read_data=sensors)

    mocker.patch('builtins.open', mock_open)

    temp = get_lm_sensors_info()

    excepted = '| core_0 : 2.1951 Ghz +62.0°C |\n| core_1 : 2.0000 Ghz +60.0°C |\n| core_2 : 0.0950 Ghz +50.0°C |'
    assert mount_msg_output(freq, temp) == excepted


def test_print_msg_without_sensors(mocker, cpuinfo, sensors):

    mock_open = mock.mock_open(read_data=cpuinfo)

    mocker.patch('builtins.open', mock_open)

    freq = read_cpuinfo()

    temp = []

    excepted = '| core_0 : 2.1951 Ghz |\n| core_1 : 2.0000 Ghz |\n| core_2 : 0.0950 Ghz |'

    assert mount_msg_output(freq, temp) == excepted
