from order import Order
from pytest import param
from settlements import Settlements
from constant import API_TYPE
from urllib.parse import urlencode, parse_qsl, urlparse

BASE_URL = 'https://dev.vip.ksher.net'
token = "7a1e6ffc84010ef6b171803753db1cfb4149f184effe2b540a8b3b0c195d2e88"

print("============ test_success_channels ============")
payment_handle = Settlements(base_url=BASE_URL, apiType=API_TYPE.FINANCE ,token=token)

params ={
    
    # "channel": "truemoney",
    # "mid":"mch35618",
    "limit":50,
    "offset":0,
    "reference_id":"20220315_35618_HZKTLJ",
    "signature": "string",
    "timestamp": "string"
    
}
# resp = payment_handle.channels()
# data = resp.json()
# print(f"\n data:{data}")

# resp = payment_handle.settlements(yyyymmdd="20220315", params=params)
# data = resp.json()
# print(f"\n data:{data}")

resp = payment_handle.settlement_order(params=params)
data = resp.json()
print(f"\n data:{data}")

# resp = payment_handle.order(yyyymmdd="20220314", params=params)
# data = resp.json()
# print(f"\n data:{data}")

# print("============ START test case: CSCANB ============")
# payment_handle = Order(base_url=BASE_URL, apiType=API_TYPE.CSCANB ,token=token)

# data ={
#     "mid":"35618",
#     "amount": 100,
#     "note": "string",
#     "signature": "string",
#     "channel": "truemoney",
#     "timestamp": "string",
#     "merchant_order_id": "test_truemoney",
# #     "device_id":"test4",
# #     "operator_id":"42600"
# }

# resp = payment_handle.create(data)
# data = resp.json()
# print(f"\n data:{data}")


# print("============ START test case: REDIRECT ============")
# payment_handle = Order(base_url=BASE_URL, apiType=API_TYPE.REDIRECT ,token=token)
# data ={
#         "mid":"38026",
#         "amount": 100,
#         "merchant_order_id": "test6",
#         "mobile_number":"asdf asd",
#         # "product_name":"aaasd",
#         # "channel":"card",
#         "redirect_url": "https://www.google.com",
#         "redirect_url_fail": "http://www.yahoo.com",
#         "timestamp":"20220228123307",
#         "signature": "string"
# }
# resp = payment_handle.create(data)
# data = resp.json()
# print(f"\n data:{data}")

# print("============ START test case: query ============")
# payment_handle = Order(base_url=BASE_URL, apiType=API_TYPE.CSCANB ,token=token)
# data = {
#         # "mid": "mch37969",
#             "signature": "string",
#             "timestamp": "20210921155002"
#         }

# resp = payment_handle.query(order_id="20220308062842",params=data)
# data = resp.json()
# print(f"\n data:{data}")

# print("============ START test case: check webhook ============")
# payment_handle = Order(base_url=BASE_URL, apiType=API_TYPE.CSCANB ,token=token)
# webhook_url="https://webhook.site/0f304897-e9ab-4036-99e9-1afc837312a1"
# params = {
#             "code": "StatusChange",
#             "instance": "testapi",
#             "message": "Order Paid",
#             "type": "Order",
#             "signature":"2B62C99FE9204469DDEAA618ED52B6D918280C97CED50956D7EF5A18A077F836"
#         }
# isValid = payment_handle.checkSignature(url=webhook_url, data=params)
# print(f"\n isValid: {isValid}")

# print("============ START test case: create webhook sign ============")
# payment_handle = Order(base_url=BASE_URL, apiType=API_TYPE.CSCANB ,token=token)
# webhook_url="https://api.foodnana.net/api/ksher/webhook"
# params = {
#             "code": "StatusChange",
#             "instance": "testapi1",
#             "message": "Order Paid",
#             "type": "Order",
#             "signature":"aaa"
#         }
# sign = payment_handle._make_sign(url=webhook_url, data=params)
# print(f"\n sign webhook: {sign}")

# example = "https://webhook.site/e0f0debc-fb41-4f94-b818-28263bd96e21?code=StatusChange&instance=test_linepay02&message=Order%20Paid&signature=2697F5A7FCE95F7241195DB67AAB97A42DD51C784A42AF4B01ABA92F9383351E&type=Order"
# parsed_url = urlparse(example)
# data= dict(parse_qsl(parsed_url.query))
# print(data)
# # signature = data.pop('signature',None)
# webhook_url="https://webhook.site/0ecf640f-b6ed-4e65-bb64-eaaa1d4c7d0b"
# resp = payment_handle.checkSignature(webhook_url, data)
# print(f"\n resp:{resp}")

# ORDER_API = '/api/v1/redirect/orders'
# endpoint = ORDER_API+'/{}'.format("abc59729")
# data={
#   "timestamp": "20210812185105",
#   "locked": False,
#   "id": "233",
#   "acquirer": "Ksher",
#   "amount": 1,
#   "channel_order_id": "4200001140202108121895751199",
#   "error_message": "Successful",
#   "reserved2": "False",
#   "status": "Paid",
#   "cleared": False,
#   "mid": "False",
#   "currency": "MYR",
#   "order_type": "Sale",
#   "channel": "wechat",
#   "acquirer_order_id": "90020210812184922947463",
#   "api_name": "Redirect",
#   "signature": "ADF6889E5BFA2C6F988FB3F28DB90ED8D649A3BC0B0466041E0874872CFF4046",
#   "merchant_order_id": "abc59729",
#   "reserved1": "2108121749215203",
#   "note": "False",
#   "gateway_order_id": "s38028233",
#   "reserved3": "False",
#   "order_date": "2021-08-12 10:49:20.949101",
#   "reserved4": "False",
#   "reference": "https://gateway.ksher.com/ua?order_uuid=f370cbaafb5a11ebac7652540075451d",
#   "error_code": "SUCCESS",
#   "force_clear": False,
#   "log_entry_url": "https://s38028.vip.ksher.net/web#action=153&view_type=form&model=rest.log&id=1031"
# }
# endpoint="/api/v1/finance/settlements/20220301"
# data={
#     "data": {},
#     "error_code": "SUCCESS",
#     "error_message": "Successful",
#     "mid": "35618",
#     "signature": "15517F5B9B175C21F9C83764D4442D056204CE07B509E9D5DA43DBD982198E35",
#     "timestamp": "1647331731"
# }
# resp = payment_handle.checkSignature(endpoint, data)
# print(f"\n resp:{resp}")