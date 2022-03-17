import json
from .BaseAPI import BaseAPI

class WalletTokenAPI (BaseAPI) :
    def __init__(self, walletKey: str, secretKey: str, cryptoSymbol: str, tokenSymbol: str) :
        headers = {
            'X-Wallet-Key': merchantKey,
            'X-Secret-Key'  : secretKey,
        }
        super(WalletTokenAPI, self).__init__(suffix="wallet/{}/token/{}".format(cryptoSymbol, tokenSymbol), headers=headers)
    
    def getBalance(self) :
        return self.executeRequest('GET', 'balance')
    
    def estimateFee(self, destinations: list, feePerByte: float = None, extraField: str = None) :
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
    
