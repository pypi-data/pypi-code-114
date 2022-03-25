from .parser import parse_liberty
from .types import *


def test_select_timing_group():
    data = r"""
pin(Y){ 
    timing() {
        test_label: 1;
        related_pin: "A";
        when: "B";
        cell_rise() {
            test_label: 11;
        }
    }
    timing() {
        test_label: 2;
        related_pin: "A";
        when: "!B";
        cell_rise() {
            test_label: 21;
        }
    }
    timing() {
        test_label: 3;
        related_pin: "B";
        when: "A";
        cell_rise() {
            test_label: 31;
        }
    }
}
"""
    pin_group = parse_liberty(data)
    assert isinstance(pin_group, Group)

    timing_group = select_timing_group(pin_group, related_pin="A")
    assert timing_group['test_label'] == 1

    timing_group = select_timing_group(pin_group, related_pin="A", when='B')
    assert timing_group['test_label'] == 1

    timing_group = select_timing_group(pin_group, related_pin="A", when='!B')
    assert timing_group['test_label'] == 2

    timing_group = select_timing_group(pin_group, related_pin="B")
    assert timing_group['test_label'] == 3

    assert select_timing_table(pin_group, related_pin="A", when='!B', table_name='cell_rise')['test_label'] == 21

