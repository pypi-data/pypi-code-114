import json
from .BaseAPI import BaseAPI

class MerchantAPI (BaseAPI) :
    def __init__(self, merchantKey: str, secretKey: str) :
        headers = {
            'X-Merchant-Key': merchantKey,
            'X-Secret-Key'  : secretKey,
        }
        super(MerchantAPI, self).__init__(suffix='merchant', headers=headers)
    
    def invoiceInfo(self, invoiceHash: str) :
        return self.executeRequest('GET', 'invoice-info', {
            'invoice_hash' : invoiceHash,
        })
    
    def processInvoices(self, invoiceHashes: list) :
        return self.executeRequest('POST', 'process-invoices', {
            'invoice_hashes' : invoiceHashes,
        })
    
    def forwardInvoices(self, invoiceHashes: list) :
        return self.executeRequest('POST', 'forward-invoices', {
            'invoice_hashes' : invoiceHashes,
        })
    
    def generateInvoiceAddress(self, invoiceHash: str, cryptocurrency: str) :
        return self.executeRequest('POST', 'generate-invoice-address', {
            'invoice_hash'   : invoiceHash,
            'cryptocurrency' : cryptocurrency,
        })
    
    def createInvoice(self, cryptocurrencies: list, currency: str = None, targetValue: float = None, title: str = None, description: str = None) :
        return self.executeRequest('POST', 'create-invoice', {
            'cryptocurrencies' : json.dumps(cryptocurrencies),
            'currency'         : currency,
            'target_value'     : targetValue,
            'title'            : title,
            'description'      : description,
        })
    
    def estimateInvoicePrice(self, cryptocurrencies: list, currency: str = None, targetValue:float = None) :
        return self.executeRequest('POST', 'estimate-invoice-price', {
            'cryptocurrencies' : json.dumps(cryptocurrencies),
            'currency'         : currency,
            'target_value'     : targetValue,
        })
    
    def recoverInvoicePrivateKey(self, invoiceHash: str, cryptocurrency: str) :
        return self.executeRequest('POST', 'recover-invoice-private-key', {
            'invoice_hash'   : invoiceHash,
            'cryptocurrency' : cryptocurrency,
        })
    
