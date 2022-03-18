import sqlite3


typeShapes = ['W', 'M', 'S', 'HP', 'WT', 'MT', 'ST',
              'Plates', 'L', 'HSS', 'Pipe', 'C', 'MC', '2L'
              ]

W_M_S_HP_shapes_AISC = ['W', 'M', 'S', 'HP']
C_MC_shapes_AISC = ['C', 'MC']
WT_MT_ST_shapes_AISC = ['WT', 'MT', 'ST']
L_shapes_AISC = ['L']
_2L_shapes_AISC = ['2L']
HSS_shapes_AISC = ['HSS']
HSS_Pipe_shapes_AISC = ['Pipe'] #Not found functionality for one section in two tables [HSS]...
Plates_shapes_AISC = ['Plates']

nameTables = ['`W-M-S-HP_shapes_AISC`',  '`C-MC_shapes_AISC`',  '`WT-MT-ST_shapes_AISC`',  '`L_shapes_AISC`',  '`2L_shapes_AISC`',  '`HSS_shapes_AISC`', '`HSS-Pipe_shapes_AISC`',  '`Plates_shapes_AISC`']

nameTablesDict = {
    '`W-M-S-HP_shapes_AISC`': W_M_S_HP_shapes_AISC,
    '`C-MC_shapes_AISC`': C_MC_shapes_AISC,
    '`WT-MT-ST_shapes_AISC`': WT_MT_ST_shapes_AISC,
    '`L_shapes_AISC`': L_shapes_AISC,
    '`2L_shapes_AISC`': _2L_shapes_AISC,
    '`HSS_shapes_AISC`': HSS_shapes_AISC,
    '`HSS-Pipe_shapes_AISC`': HSS_shapes_AISC,
    '`Plates_shapes_AISC`': Plates_shapes_AISC
}

