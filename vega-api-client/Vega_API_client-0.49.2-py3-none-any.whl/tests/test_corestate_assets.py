import vegaapiclient as vac


def test_ListAssets(corenode_corestate):
    req = vac.vega.api.v1.corestate.ListAssetsRequest()
    assets = corenode_corestate.ListAssets(req).assets
    assert len(assets) > 0
    asset_id = assets[0].id

    req = vac.vega.api.v1.corestate.ListAssetsRequest(asset=asset_id)
    assets = corenode_corestate.ListAssets(req).assets
    assert len(assets) == 1
    assert assets[0].id == asset_id
