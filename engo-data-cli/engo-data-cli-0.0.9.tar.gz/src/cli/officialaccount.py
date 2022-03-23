from hashlib import md5
import json
import random
import re
import time
import wechatpy
from wechatpy.client.api import WeChatMaterial, WeChatMessage

class OfficialAccount:
    client:wechatpy.WeChatClient
    # a,b,c,d,e,f,g,h,i,j,k
    alphabet:list[str] = ['0ZU1zjjUKYTu0OBYbBCRzKz2lrvHiip6aD5aoDpuyvA', '0ZU1zjjUKYTu0OBYbBCRzLPk3OrDwiroVlfP3xeFDAE', '0ZU1zjjUKYTu0OBYbBCRzEA0DIjUCV4QAuBPoGxY7-c', '0ZU1zjjUKYTu0OBYbBCRzOl3YXqu0WGDx52uvAK2FCU', '0ZU1zjjUKYTu0OBYbBCRzKIiGl1N893F8sMi2dXzAzk', '0ZU1zjjUKYTu0OBYbBCRzJBESGLHgLm_D6FQDrpCkCk', '0ZU1zjjUKYTu0OBYbBCRzNZSlSZlirTJQBLBI18hyRQ', '0ZU1zjjUKYTu0OBYbBCRzG7O_tOzALQ3Yy1lwCc8-nQ', '0ZU1zjjUKYTu0OBYbBCRzPUgS2SxbKX-4itT9Piwi7k', '0ZU1zjjUKYTu0OBYbBCRzGi3_SUp_QlKVxlpAz-Op_g', '0ZU1zjjUKYTu0OBYbBCRzAme8NTzeh-UpjNRDn3AMbY']

    def __init__(self, client = wechatpy.WeChatClient):
        self.client = client

    def articleUpload(self, filePath:str = "data/20200823-special.json"):
        m = WeChatMaterial(self.client)
        with open(filePath, 'r') as f:
            data = json.load(f)
            items = self.__getTodaysList(data)
            if len(items) > 0:
                if not self.__article_Exists(items[0]['title']):
                    payload = self.__createArticlesPayload(items)
                    # result = m.add_articles(payload) deprecated
                    result = m.add_drafts(payload)
                    print(result)
                else:
                    print('Skipped as it is already existed')
            else:
                print('There is no news for today')

    # This approach only available after the annual pay of 300 CNY per year
    # def __dailyNotify(self, media_id:str):
        # m = WeChatMessage(self.client)
        # result = m.send_mass_article(group_or_users='-caryyu-', media_id=media_id, preview=True)
        # print(result)

    def __getTodaysList(self, items:list[dict]) -> list[dict]:
        regex = r'(.+)\((\d+\/\d+\/\d+)\)'

        result = []
        for item in items:
            match = re.search(regex, item['navigation'])

            date = None
            if match != None:
                txt:str = match.groups()[1]
                date = time.strptime(txt,'%Y/%m/%d')

            today = time.strftime('%Y/%m/%d')
            target = time.strftime('%Y/%m/%d', date) if date is not None else ''
            # print('{target} {today}'.format(today=today, target=target))
            if target == today:
                result.append(item)

        return result

    def __getRandomBannerMediaId(self):
        m = WeChatMaterial(self.client)
        body = m.batchget('image')
        if body['item_count'] > 0:
            banners = [i for i in body['item'] if i['name'] == 'banner']
            banner = banners[random.randint(0, len(banners) - 1)]
            return banner['media_id']
        raise Exception('Cannot find any available images')

    def getAlphabet(self):
        m = WeChatMaterial(self.client)
        body = m.batchget('image')
        if body['item_count'] > 0:
            imgs = body['item']
            imgs = sorted(imgs, key=lambda x: x['name'])
            items = [i['media_id'] for i in imgs if i['name'] in 'abcdefghijk']
            return items

        raise Exception('Cannot find any alphabets')

    def __createArticlesPayload(self, items:list[dict]) -> list[dict]:
        result = []
        for i in range(len(items)):
            item = items[i]
            mediaId = self.__getRandomBannerMediaId() if i == 0 else self.alphabet[i-1]
            result.append({
                'title': item['title'][0:64],
                'content': self.__addMiniProgramJump(item['title'], item['content']),
                'thumb_media_id': mediaId,
                'show_cover_pic': 0
            })
        return result
        
    def __article_Exists(self, title:str) -> bool:
        m = WeChatMaterial(self.client)
        body = m.batchget('news')
        for i in range(body['item_count']):
            articles = body['item'][i]['content']['news_item']
            articles = [i for i in articles if i['title'] == title[0:64]]
            return len(articles) > 0
        return False

    def __addMiniProgramJump(self, title:str, content:str) -> str:
        digest = md5(title.encode(encoding='utf-8')).hexdigest()
        appid = 'wx3573152086573b1b'
        path = 'pages/content/content?digest={digest}'.format(digest=digest)
        return '''
        <p><a data-miniprogram-appid="{appid}" data-miniprogram-path="{path}" href="">VOA 英语听力酷 | 音频收听</a></p>
        <p>{title}</p>
        {content}
        '''.format(title=title, appid=appid, path=path, content=content)

