#curl -X POST "https://dev.freeclimb.com/apiserver/Accounts/ACc871a471197a7a51f5aadc9daf4662a89bcfc7e5/Calls/CA4f285634fda2907be0a71caf561d6ccf69a538e5/AppNavs" -d "{\"appNavs\":[{\"key\":\"utter_ask_bp_menu_disconnect\", \"value\":\"disconnect\"}]}" -u "ACc871a471197a7a51f5aadc9daf4662a89bcfc7e5:a8ad5bc9da00536c2d53866b2d720c43bf94d173"
import aiohttp
import asyncio
import logging

CDR_ACCOUNT_ID='ACc871a471197a7a51f5aadc9daf4662a89bcfc7e5'
CDR_ACCOUNT_TOKEN='a8ad5bc9da00536c2d53866b2d720c43bf94d173'
CDR_ENDPOINT='https://dev.freeclimb.com/apiserver'
logger = logging.getLogger(__name__)
# CDR_ACCOUNT_ID='ACf3106bd1184dad58f0e29bca1d448a19e74f379d'
# CDR_ACCOUNT_TOKEN='a33cdb0a5ed880c5238b5dc35aa28626bbc73097'
# CDR_ENDPOINT='https://dev.freeclimb.com/apiserver'

async def send_app_nav_async(conversation_id, app_nav):
    payload = {
        'appNavs': [app_nav]
    }
    async with aiohttp.ClientSession() as session:
        
        try:
            fc_auth = aiohttp.BasicAuth(CDR_ACCOUNT_ID, CDR_ACCOUNT_TOKEN,encoding='UTF-8')
            endpoint = f"{CDR_ENDPOINT}/Accounts/{CDR_ACCOUNT_ID}/Calls/{conversation_id}/AppNavs"
            async with session.request(method='POST',url=endpoint,json=payload,verify_ssl=False,auth=fc_auth) as response:
                print('[{}] - cdr submission: {}'.format(conversation_id, response.status))
        except aiohttp.ClientConnectorError as e:
            print('[{}] - cdr connection error: {}'.format(conversation_id, str(e)))
        except Exception as e:
            print('[{}] - cdr submission failed: {}'.format(conversation_id, str(e)))

async def start():
    await send_app_nav_async('CA7bd14e4bc5e207846240c327acbe5f7ec1282eed', {'key': 'end_disconnect', 'value': 'disconnect'})

asyncio.run(start())