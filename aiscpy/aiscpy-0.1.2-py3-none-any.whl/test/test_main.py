from aiscpy.core import QueryingToDB

B = QueryingToDB('''
                         SELECT Shape, A FROM `W-M-S-HP_shapes_AISC`
                         WHERE Shape= 'W44X335'
                         ''', fetchone=True)

def test_init_queryingToDB():
    A = QueryingToDB('''
                         SELECT * FROM `W-M-S-HP_shapes_AISC`
                         WHERE Shape= 'W44X335'
                         ''', fetchone=True)
    assert A.queryToList == ["W","W44X335",98.5,44,1.03,15.9,1.77,2.56,2.625,1.3125,38.75,5.5,335,4.5,38.0,31100,1410,17.8,1620,1200,150,3.49,236,4.24,42.3,74.7,535000,168,1180,278,805]
    
    assert B.queryToList == ["W44X335", 98.5]
    assert B.keysQuery == ["Shape", "A"]
    assert B.fetchoneStatus == True
    assert B.toDict() =={"Shape": "W44X335", "A": 98.5}
    