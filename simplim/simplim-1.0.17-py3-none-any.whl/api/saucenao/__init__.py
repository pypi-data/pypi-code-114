r"""@2020 HARDRELICE. All Rights Reserved.
 ╻ ╻ ┏━┓ ┏━┓ ┏━┓ ┏━┓ ┏━╸ ╻   ╻  ┏━╸ ┏━╸ TM
 ┣━┫ ┣━┫ ┣━┛ ┃ ┃ ┣━┛ ┣━╸ ┃   ┃  ┃   ┣━╸
 ╹ ╹ ╹ ╹ ╹ ╹ ┗━┛ ╹ ╹ ┗━╸ ┗━╸ ╹  ┗━╸ ┗━╸

A tool using website <https://saucenao.com/> & its search method <https://saucenao.com/search.php/> to search & match anime pics
"""

import requests as rq
from bs4 import BeautifulSoup as bs

link = 'https://saucenao.com/search.php?url='
#url = 'http://c2cpicdw.qpic.cn/offpic_new/2733937760/122527455-3725687086-E6B4900521AB2A7FCC0B848E4D45212E/0'

def search(url,number):
	headers={
		'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
		'Cookie': '_ga=GA1.2.502580561.1589195122; __gads=ID=59eee674f521772a:T=1589195132:S=ALNI_MbatBgMvK-5EkecB6ashZXvgmeaGg; __cfduid=d5f98d910e9a188235feee3f6d18b52fe1589195133; _gid=GA1.2.593944264.1589449165; __utma=4212273.502580561.1589195122.1589530032.1589530032.1; __utmc=4212273; __utmz=4212273.1589530032.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; token=5ebead2fd9a18; user=38358; auth=d26b3ba62bb3b4806945e9017bb38e1867fec678; _gat=1'
	}
	page = rq.get(link+url,headers=headers).text
	page = bs(page,'lxml')
	results = page.find_all(class_ = 'result') 
	if len(results)==0:
		return -1
	if results[0].get('id')=='result-hidden-notification':
		results = page.find_all(class_ = 'result hidden')
	package = []
	cnt = number
	for result in results:
		if cnt == 0:
			break
		similarity_str = result.find(class_='resultsimilarityinfo').text
		similarity = float(similarity_str[:-1])
		thumbnail = result.find(class_='resultimage').find('img').get('src')
		title = result.find(class_='resulttitle').text
		print(thumbnail)
		content = result.find(class_='resultcontentcolumn')
		site = 'None'
		if content.find('strong'):
			site = content.find('strong').text
		TV = 'None'
		ID = 'None'
		ID_link = 'None'
		author = 'None'
		author_link = 'None'
		if site=='None':
			pass
		elif site=='Title: ':
			site = 'None'
			TV = content.text
		else:
			site=site[:-5]
			info = content.find_all(class_='linkify')
			if len(info)!=0:
				try:
					ID = info[0].text
					ID_link = info[0].get('href')
				except:
					ID = ''
					ID_link = ''
				try:
					author = info[1].text
					author_link = info[1].get('href')
				except:
					author = ''
					author_link = ''
		pack={'similarity_str':similarity_str, 'similarity':similarity, 'thumbnail':thumbnail, 'title':title, 'site':site,'TV':TV, 'ID':ID, 'author':author, 'ID_link':ID_link, 'author_link':author_link}
		package.append(pack)
		cnt -= 1
	return package