import datetime
import queue
import time

from chipmunkdb.ChipmunkDb import ChipmunkDb

import coinlib.dataWorker_pb2 as statsModel
import coinlib.dataWorker_pb2_grpc as stats
import threading
import inspect
import pandas as pd
import asyncio
import simplejson as json
from coinlib.WorkerJobProcess import WorkerJobProcess
from coinlib.Registrar import Registrar
from coinlib.statistics.StatisticMethodJob import StatisticMethodJob

class SymbolWorker(WorkerJobProcess):


    def __init__(self, workerJob, factory):
        self.symbolWorkerConfig = None
        self.waitingQueue = None
        self.symbolWorkerProcessInfo = None
        self.symbolWorkerRegistrationInfo = None
        super(SymbolWorker, self).__init__(workerJob, factory)

    def initialize(self):
        self.registrar = Registrar()
        self.symbolWorkerInterface = stats.SymbolBrokerWorkerStub(self.getChannel())
        if self.symbolWorkerConfig is None:
            symbolWorkerConfigGlobal = self.symbolWorkerInterface.GetConfig(self.workerJob)
            if symbolWorkerConfigGlobal.HasField("infoConfig"):
                self.symbolWorkerConfig = symbolWorkerConfigGlobal.infoConfig
            if symbolWorkerConfigGlobal.HasField("consumeConfig"):
                self.symbolWorkerConfig = symbolWorkerConfigGlobal.consumeConfig
            if symbolWorkerConfigGlobal.HasField("historicalConfig"):
                self.symbolWorkerConfig = symbolWorkerConfigGlobal.historicalConfig
            if symbolWorkerConfigGlobal.HasField("consumeOrderbookConfig"):
                self.symbolWorkerConfig = symbolWorkerConfigGlobal.consumeOrderbookConfig

            self.symbolWorkerRegistrationInfo = self.registrar.symbolBrokerCallbacks["method_"+self.symbolWorkerConfig.symbolBrokerIdentifier]
            self.symbolWorkerProcessInfo = self.symbolWorkerRegistrationInfo["process"]
        pass

    def onErrorHappened(self, message):

        indicatorError = statsModel.SymbolBrokerError()
        indicatorError.error.message = str(message)
        indicatorError.worker.CopyFrom(self.workerJob)

        self.logger().error("Error in symbol broker - "+str(message))

        self.symbolWorkerInterface.OnSymbolBrokerErrorOccured(indicatorError)

    def error(self, message):
        self.onErrorHappened(message)
        return False

    def setConfig(self, configuration):
        self.symbolWorkerConfig = configuration
        pass

    def runSymbolWorker(self):
        pass

    def getOptions(self):
        return json.loads(self.symbolWorkerConfig.options)

    def run(self):

        t = threading.Thread(target=self.runSymbolWorker, args=[], daemon=True)

        t.start()

        try:
           t.join()
        except Exception as e:
           self.onErrorHappened(str(e))
           pass

        return True

class SymbolBrokerTickerSymbolData:
    open = None
    close = None
    datetime = None
    high = None
    low = None
    volume = None
    trades = None
    timeframe = None
    symbol = None
    closeTime = None
    symbol_id = None
    isFinal = False

class ExchangeInfoRequest:
    options = {}

class HistoricalSymbolRequest:
    options = {}
    start = None
    end = None
    quoteAsset = None
    baseAsset = None
    symbol_id = None
    exchange_id = None
    timeframe = None
    contractType = None
    assetType = None

class OrderBookConsumer:
    options = {}
    quoteAsset = None
    baseAsset = None
    symbol_id = None
    exchange_id = None
    timeframe = None
    contractType = None
    assetType = None

class MarketDataConsumer:
    options = {}
    quoteAsset = None
    baseAsset = None
    symbol_id = None
    exchange_id = None
    timeframe = None
    contractType = None
    assetType = None

class SymbolWorkerFetchHistoricalData(SymbolWorker):

    def getRunnerProcess(self):
        return self.symbolWorkerProcessInfo["downloadHistorical"]

    def sendDataFrame(self, df: pd.DataFrame):
        """Saving the Dataframe.
           Keyword arguments:
                index: should be your "close" datetime
                open: Open price
                high:  High Price
                low: Low Price
                close: Close Price
                volume: Volumes
                (trades: Optional: Trades count)

        """
        domain = None
        if self.symbolWorkerConfig.chartData.chart_prefix is not None and self.symbolWorkerConfig.chartData.chart_prefix != "":
            domain = self.symbolWorkerConfig.chartData.chart_prefix

        if self.chipmunkDb is None:
            host = self.registrar.get_chipmunkdb_host(self.symbolWorkerConfig.chartData.chipmunkdbHost);
            self.chipmunkDb = ChipmunkDb(host)

        if self.symbolWorkerConfig.returnData:

            brokerSymbolData = statsModel.SymbolBrokerFetchData()
            brokerSymbolData.worker.CopyFrom(self.workerJob)

            list = df.to_records()
            for e in list:
                d = statsModel.SymbolBrokerMarketData()
                d.open = e[1]
                d.close = e[4]
                d.high = e[2]
                d.low = e[3]
                ts = pd.to_datetime(str(e[0]))
                d.closeTime = datetime.datetime.strftime(ts, "%Y-%m-%dT%H:%M:%S.%fZ")
                d.volume = e[5]
                brokerSymbolData.data.append(d)

            self.symbolWorkerInterface.onBrokerFetchSymbolDataReceived(brokerSymbolData)

        else:

            df.rename(columns={'open': 'main:open', 'close': 'main:close', 'high': 'main:high', 'low': 'main:low', 'trades':'main:trades', 'volume':'main:volume'}, inplace=True)

            self.chipmunkDb.save_as_pandas(df, self.symbolWorkerConfig.chartData.workspace_id, mode="dropbefore", domain=domain)

        return True

    def runSymbolWorker(self):
        try:
            process = self.getRunnerProcess()

            req = HistoricalSymbolRequest()
            req.options = self.getOptions()
            req.start = self.symbolWorkerConfig.start
            req.end = self.symbolWorkerConfig.end
            req.quoteAsset = self.symbolWorkerConfig.quoteAsset
            req.baseAsset = self.symbolWorkerConfig.baseAsset
            req.symbol_id = self.symbolWorkerConfig.client_symbol_id
            req.exchange_id = self.symbolWorkerConfig.exchange_id
            req.timeframe = self.symbolWorkerConfig.timeframe
            req.contractType = self.symbolWorkerConfig.contractType
            req.assetType = self.symbolWorkerConfig.assetType


            if (inspect.iscoroutinefunction(process)):
                async def runandwait():
                    try:
                        task = asyncio.ensure_future(process(req, self))
                        await task
                    except Exception as e2:
                        raise e2

                loop = asyncio.new_event_loop()
                ret = loop.run_until_complete(runandwait())
            else:
                ret = process(req, self)

        except Exception as e:

            self.onErrorHappened(str(e))

class SymbolWorkerConsumeMarketData(SymbolWorker):
    consumerStopped = False

    def getRunnerProcess(self):
        return self.symbolWorkerProcessInfo["consumeLive"]

    def canceled(self):
        return self.consumerStopped

    def sendSymbolTicker(self, ticker: SymbolBrokerTickerSymbolData):

        d = statsModel.SymbolBrokerMarketData()
        d.worker.CopyFrom(self.workerJob)
        d.open = ticker.open
        d.close = ticker.close
        d.high = ticker.high
        d.low = ticker.low
        d.volume = ticker.volume
        d.trade = ticker.trades
        d.datetime = ticker.datetime
        d.closeTime = ticker.closeTime
        d.symbol = ticker.symbol
        d.isfinal = ticker.isFinal
        d.symbol_id = ticker.symbol_id

        self.symbolWorkerInterface.onMarketDataReceived(d)

        return True

    def wait_for_stop_thread(self):

        s = statsModel.SymbolBrokerStopConsumerListener()
        s.worker.CopyFrom(self.workerJob)

        try:
            if (self.waitingQueue != None):
                self.waitingQueue.put(None)
            self.waitingQueue = None
            self.waitingQueue = queue.SimpleQueue()
            self.commandStream = self.symbolWorkerInterface.waitForCommands(iter(self.waitingQueue.get, None))
            self.waitingQueue.put(s)
            for d in self.commandStream:
                if d.stopped:
                    self.consumerStopped = True
        except Exception as e:
            self.logger().info(str(e))
            self.consumerStopped = True

    def run_process_in_thread(self, process, req):
        t = threading.Thread(target=self.wait_for_stop_thread, args=())
        t.start()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(process(req, self))
        loop.close()
        return True

    def runSymbolWorker(self):
        process = self.getRunnerProcess()

        req = MarketDataConsumer()
        req.options = self.getOptions()
        req.quoteAsset = self.symbolWorkerConfig.quoteAsset
        req.baseAsset = self.symbolWorkerConfig.baseAsset
        req.symbol_id = self.symbolWorkerConfig.client_symbol_id
        req.exchange_id = self.symbolWorkerConfig.exchange_id
        req.timeframe = self.symbolWorkerConfig.timeframe
        req.exchange_id = self.symbolWorkerConfig.exchange_id
        req.contractType = self.symbolWorkerConfig.contractType
        req.assetType = self.symbolWorkerConfig.assetType

        t = threading.Thread(target=self.run_process_in_thread, args=(process, req))
        t.start()

        pass

class SymbolWorkerBrokerInfo(SymbolWorker):

    def saveBrokerInfo(self, exchanges, symbols):
        brokerSymbolInfo = statsModel.SymbolBrokerInfo()
        for e in exchanges:
            brokerSymbolInfo.exchanges.append(e)

        for s in symbols:
            brokerSymbolInfo.symbols.append(s)
        brokerSymbolInfo.worker.CopyFrom(self.workerJob)
        return self.symbolWorkerInterface.onBrokerSymbolInfoReceived(brokerSymbolInfo)

    def getRunnerProcess(self):
        return self.symbolWorkerProcessInfo["brokerInfoProcess"]

    def runSymbolWorker(self):
        process = self.getRunnerProcess()

        try:

            req = ExchangeInfoRequest()
            req.options = self.getOptions()

            if (inspect.iscoroutinefunction(process)):
                async def runandwait():
                    try:
                        task = asyncio.ensure_future(process(req, self))
                        result = await task
                    except Exception as e2:
                        raise e2

                loop = asyncio.new_event_loop()
                ret = loop.run_until_complete(runandwait())
            else:
                ret = process(req, self)


        except Exception as e:
            self.onErrorHappened(str(e))

