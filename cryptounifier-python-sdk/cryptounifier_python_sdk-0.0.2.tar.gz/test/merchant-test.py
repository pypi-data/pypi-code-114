
from  cryptounifier_python_sdk import MerchantAPI, WalletAPI

# WalletAPI
client = WalletAPI('', '', 'btc')

#balance = client.getBalance()
balance = client.validateAddresses(["ubc"])
print(balance)

# depositAddresses = client.getDepositAddresses()
# print(depositAddresses)

# MerchantAPI
# client_MerchantAPI = MerchantAPI('', '')

# # invoice = client_MerchantAPI.createInvoice(['btc', 'bch', 'eth'])
# # print(invoice)
# invoiceInfo = client_MerchantAPI.invoiceInfo("")
# print(invoiceInfo)