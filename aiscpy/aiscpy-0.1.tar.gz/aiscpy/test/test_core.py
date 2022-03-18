from aiscpy.core import selectTable

def test_select_table():
    table1 = selectTable('W')
    table2 = selectTable('M')
    table3 = selectTable('S')
    table4 = selectTable('HP')
    
    assert table1 == '`W-M-S-HP_shapes_AISC`'
    assert table2 == '`W-M-S-HP_shapes_AISC`'
    assert table3 == '`W-M-S-HP_shapes_AISC`'
    assert table4 == '`W-M-S-HP_shapes_AISC`'
    