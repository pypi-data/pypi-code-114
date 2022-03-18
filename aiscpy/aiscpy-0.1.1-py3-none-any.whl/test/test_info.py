from aiscpy.core import updateTablesName

def test_info_tables():
    tables = updateTablesName()
    assert tables == ['W-M-S-HP_shapes_AISC',  'C-MC_shapes_AISC',  'WT-MT-ST_shapes_AISC',  'L_shapes_AISC',  '2L_shapes_AISC',  'HSS_shapes_AISC',  'HSS-Pipe_shapes_AISC',  'Plates_shapes_AISC']