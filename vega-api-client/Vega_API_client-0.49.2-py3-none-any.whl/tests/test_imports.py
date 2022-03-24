import vegaapiclient as vac


def test_api():
    assert "v1" in dir(vac.vega.api)


def test_checkpoint():
    assert "v1" in dir(vac.vega.checkpoint)


def test_commands():
    assert "v1" in dir(vac.vega.commands)


def test_events():
    assert "v1" in dir(vac.vega.events)


def test_oracles():
    assert "v1" in dir(vac.vega.oracles)


def test_snapshot():
    assert "v1" in dir(vac.vega.snapshot)


def test_tm():
    assert "replay" in dir(vac.vega.tm)


def test_wallet():
    assert "v1" in dir(vac.vega.wallet)
