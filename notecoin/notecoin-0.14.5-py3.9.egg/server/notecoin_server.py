import uvicorn
from fastapi import FastAPI
from notecoin.okex.server.const import account_account, market_tickers
from notecoin.strategy.sell_strategy import AutoSeller

seller = AutoSeller()

app = FastAPI()
app.include_router(account_account)
app.include_router(market_tickers)
app.include_router(seller)

# uvicorn notecoin_server:app --host '0.0.0.0' --port 8444 --reload
# uvicorn notecoin_server:app --host '0.0.0.0' --port 8444
# uvicorn notecoin_server: app - -host '0.0.0.0' - -port 8444

uvicorn.run(app, host='0.0.0.0', port=8444)
