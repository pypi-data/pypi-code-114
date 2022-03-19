from stringtoolsfpat import StringToolsFpat


def test_lower():
    assert StringToolsFpat.lower("TEST") == "test"


def test_upper():
    assert StringToolsFpat.upper("TEST") == "TEST"
