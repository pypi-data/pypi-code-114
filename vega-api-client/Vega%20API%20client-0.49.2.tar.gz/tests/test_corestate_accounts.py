import vegaapiclient as vac


def test_ListAccounts(corenode_corestate):
    req = vac.vega.api.v1.corestate.ListAccountsRequest()
    accounts = corenode_corestate.ListAccounts(req).accounts
    assert len(accounts) > 0
