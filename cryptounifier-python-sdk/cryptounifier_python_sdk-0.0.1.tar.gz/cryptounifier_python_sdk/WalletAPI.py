import json
from .BaseAPI import BaseAPI

class WalletAPI (BaseAPI) :
    def __init__(self, merchantKey: str, secretKey: str, cryptoSymbol: str) :
        headers = {
            'X-Wallet-Key': merchantKey,
            'X-Secret-Key'  : secretKey,
        }
        super(WalletAPI, self).__init__(suffix="wallet/{}".format(cryptoSymbol), headers=headers)
    
    def getBlockchainInfo(self) :
        return self.executeRequest('GET', 'blockchain-info')
    
    def getTransactionInfo(self, txid: str) :
        return self.executeRequest('GET', 'transaction-info', 
                                    {'txid':txid})
    
    def getDepositAddresses(self) :
        return self.executeRequest('GET', 'deposit-addresses')
    
    def getBalance(self) :
        return self.executeRequest('GET', 'balance')
    
    def validateAddresses(self, addresses: list) :
        return self.executeRequest('POST', 'validate-addresses', 
                                        {'addresses':json.dumps(addresses)})
    
    def estimateFee(self, destinations:list, feePerByte:float = None, extraField: str = None) :
        return self.executeRequest('POST', 'estimate-fee', {
                                    'destinations' : json.dumps(destinations),
                                    'fee_per_byte' : feePerByte,
                                    'extra_field'  : extraField,
                                    })
    
    def sendTransaction(self, destinations: list, feePerByte: float = None, extraField: str = None) :
        return self.executeRequest('POST', 'send-transaction', {
                                    'destinations' : json.dumps(destinations),
                                    'fee_per_byte' : feePerByte,
                                    'extra_field'  : extraField,
                                })
    
