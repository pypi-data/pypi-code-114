# Creator : Sunkyeong Lee
# Inquiry : sunkyeong.lee@concentrix.com / sunkyong9768@gmail.com

import urllib.request
import json
from sqlalchemy import create_engine
import pandas as pd
import time

api_key = ''

def itemConverter(item):
    item_list = {'conversion' : 'segments', 'traffic' : 'visits', 'bounce' : 'bounce_rate', 'mobile_visitor' : 'unique_visitors', 'desktop_visitor' : 'unique_visitors'}
    return item_list[item]

def getResponse(url, item, domain):
    response = urllib.request.urlopen(url)
    response_message = response.read().decode('utf8')

    if item == 'mobile_channel' or item == 'desktop_channel':
        return pd.DataFrame(json.loads(response_message)['visits'][domain])  

    else: 
        return pd.DataFrame(json.loads(response_message)[itemConverter(item)])

def getSimilarwebData(company, domain, start_date, end_date, site_code, channel, item):
    conversion_url = 'https://api.similarweb.com/v1/segment/{company}/conversion-analysis/query?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&metrics=visits,converted-visits&channel={channel}&main_domain_only=false&format=json&show_verified=false'.format(company = company, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code, channel = channel)
    traffic_url = 'https://api.similarweb.com/v1/website/{domain}/total-traffic-and-engagement/visits?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&main_domain_only=false&format=json&show_verified=false&mtd=false'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    bounce_url = 'https://api.similarweb.com/v1/website/{domain}/total-traffic-and-engagement/bounce-rate?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&main_domain_only=false&format=json&show_verified=false&mtd=false'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    mobile_channel_url = 'https://api.similarweb.com/v1/website/{domain}/traffic-sources/mobile-overview-share?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&main_domain_only=false&format=json'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    desktop_channel_url = 'https://api.similarweb.com/v1/website/{domain}/traffic-sources/overview-share?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&main_domain_only=false&format=json'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    desktop_visitor = 'https://api.similarweb.com/v1/website/{domain}/unique-visitors/desktop_unique_visitors?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&state=&main_domain_only=false&format=json&show_verified=false&mtd=false'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    mobile_visitor = 'https://api.similarweb.com/v1/website/{domain}/unique-visitors/mobileweb_unique_visitors?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&main_domain_only=false&granularity=monthly&format=json&show_verified=false&mtd=false'.format(domain = domain, api_key = api_key, start_date = start_date, end_date = end_date, site_code = site_code)
    
    if item == 'conversion':        
        return getResponse(conversion_url, item, 'null')

    elif item == 'traffic':
        return getResponse(traffic_url, item, 'null')
    
    elif item == 'bounce':
        return getResponse(bounce_url, item, 'null')
    
    elif item == 'mobile_visitor':
        return getResponse(mobile_visitor, item, 'null')
    
    elif item == 'desktop_visitor':
        return getResponse(desktop_visitor, item, 'null')

    elif item == 'mobile_channel' or item == 'desktop_channel':
        if item == 'mobile_channel':
            channel_resp = getResponse(mobile_channel_url, item, domain)
        else :
            channel_resp = getResponse(desktop_channel_url, item, domain)

        channel_df_final = []
        for j in range(len(channel_resp['visits'])):
            channel_df = pd.DataFrame(channel_resp['visits'].loc[j])
            channel_df.insert(0, 'source', channel_resp['source_type'].loc[j], True)
            channel_dict = channel_df.to_dict('records')
            for i in range(len(channel_dict)):
                channel_df_final.append(channel_dict[i])

        return pd.DataFrame(channel_df_final)

# Traffic 전용
def getSimilarwebData_all(company_id, start_date, end_date, site_code, device_type, metric):
    metricStr = metricToStr(metric)
    traffic_url = 'https://api.similarweb.com/v1/company/{company_id}/{device_type}-traffic-and-engagement/query?api_key={api_key}&country={site_code}&start_date={start_date}&end_date={end_date}&main_domain_only=false&granularity=Monthly&metrics={metric}'.format(company_id = company_id, device_type = device_type, api_key = api_key, site_code = site_code, start_date = start_date, end_date = end_date, metric = metricStr)
    
    response = urllib.request.urlopen(traffic_url)
    response_message = response.read().decode('utf8')

    return pd.DataFrame(json.loads(response_message)['companies'])


## Segment Analysis 전용
def getSimilarwebData_SA(segment_id, start_date, end_date, site_code, metric):
    metricStr = metricToStr(metric)
    segment_analysis_url = 'https://api.similarweb.com/v1/segment/{segment_id}/traffic-and-engagement/query?api_key={api_key}&start_date={start_date}&end_date={end_date}&country={site_code}&granularity=monthly&main_domain_only=false&format=json&show_verified=false&metrics={metric}&mtd=false'.format(segment_id = segment_id, api_key = api_key, site_code = site_code, start_date = start_date, end_date = end_date, metric = metricStr)
    
    response = urllib.request.urlopen(segment_analysis_url)
    response_message = response.read().decode('utf8')

    return pd.DataFrame(json.loads(response_message)['segments'])


def stackTodb(dataFrame, dbTableName):
    print(dataFrame)
    db_connection_str = 'mysql+pymysql://root:12345@127.0.0.1:3307/similarweb'
    db_connection = create_engine(db_connection_str, encoding='utf-8')
    conn = db_connection.connect()

    dataFrame.to_sql(name=dbTableName, con=db_connection, if_exists='append', index=False)
    print("finished")


def inputConverter(item, input):
    if item == 'website':
        website_list = {'samsung' : 'samsung.com%23', 'apple' : 'apple.com%23', 'lg' : 'lg.com%23', 'currys' : 'currys.co.uk%23', 'amazon.uk mobile phone' : 'amazon.co.uk%23Mobile%20Phones%20and%20Communication', 'amazon.uk home appliances' : 'amazon.co.uk%23Kitchen%20and%20Home%20Appliances', 'hp' : 'hp.com%23', 'amazon.uk home cinema' : 'amazon.co.uk%23Home%20Cinema,%20TV%20and%20Video', 'dell' : 'dell.com%23', 'amazon cell phone' : 'amazon.com%23Cell%20Phones%20and%20Accessories', 'amazon electronics' : 'amazon.com%23Electronics', 'walmart' : 'walmart.com%23Electronics', 'amazon appliances' : 'amazon.com%23Appliances', 'bestbuy' : 'bestbuy.com%23'}
        return website_list[input]
    
    elif item == 'company':
        company_list = {'samsung' : 'samsung', 'apple' : 'apple', 'lg' : 'lg', 'currys' : 'currys', 'amazon.uk mobile phone' : 'amazon', 'amazon.uk home appliances' : 'amazon', 'hp' : 'hp', 'amazon.uk home cinema' : 'amazon', 'dell' : 'dell', 'amazon cell phone' : 'amazon', 'amazon electronics' : 'amazon', 'walmart' : 'walmart', 'amazon appliances' : 'amazon', 'bestbuy' : 'bestbuy'}
        return company_list[input]

    elif item == 'site_code':
        sitecode_list = {'world' : 'world', 'au' : 'au', 'br' : 'br', 'ca' : 'ca', 'fr' : 'fr', 'de' : 'de', 'in' : 'in', 'id' : 'id', 'it' : 'it', 'nl' : 'nl', 'ru' : 'ru', 'sa' : 'sa', 'es' : 'es', 'se' : 'se', 'tr' : 'tr', 'uk' : 'gb', 'ae' : 'ae', 'us' : 'us', 'eg' : 'eg'}
        return sitecode_list[input]
    
    elif item == 'domain':
        domain_list = {'samsung' : 'samsung.com', 'apple' : 'apple.com', 'nike' : 'nike.com'}
        return domain_list[input]
    
    elif item == 'company_id':
        company_id_list = {'samsung' : 'a56cd730-f350-4651-851c-6ad31610fc98', 'apple' : '4b1b29f6-6d43-44d7-a3e8-bc08bcf42cf8', 'lg' : 'ec6daea4-2fa3-42b6-9179-aaf6f76e4e70', 'nike' : '2149c731-363b-4208-bc57-e93577a7fc4c'}
        return company_id_list[input]

# 22-01-26 channel 추가
def channelConverter(channel):
    channel_list = {'total' : 'total', 'direct' : 'direct', 'paid-search' : 'paid-search', 'organic-search' : 'organic-search', 'display-ads' : 'display-ads', 'referrals' : 'referrals', 'mail' : 'mail', 'social' : 'social'}
    return channel_list[channel]

def defaultColumn(dataFrame, site_code):
    dataFrame.insert(0, "site_code", site_code, True)
    dataFrame.insert(1, "data_saved", time.strftime('%Y-%m-%d', time.localtime()), True)


def refineSWFrame(item, company, domain, start_date, end_date, site_code, channel, device_type, metric):
    if item == 'conversion':
        dataFrame = getSimilarwebData(inputConverter('website', company), 'null', start_date, end_date, inputConverter('site_code', site_code), channel, 'conversion')
        defaultColumn(dataFrame, site_code)
        dataFrame.insert(2, "device_type", 'desktop', True)
        dataFrame.insert(3, "company_name", inputConverter('company', company), True)
        dataFrame.insert(4, "sub_company_name", company, True)
        dataFrame.insert(5, "channel", channel, True)
        
        return dataFrame

    elif item == 'traffic' or item == 'bounce' or item == 'mobile_channel' or item == 'desktop_channel' or item == 'mobile_visitor' or item == 'desktop_visitor':
        dataFrame = getSimilarwebData('null', inputConverter('domain', domain), start_date, end_date, inputConverter('site_code', site_code), 'null', item)
        defaultColumn(dataFrame, site_code)

        if item == 'mobile_channel' or item == 'mobile_visitor':
            dataFrame.insert(2, "device_type", 'mobile', True)

        elif item == 'desktop_channel' or item == 'desktop_visitor':
            dataFrame.insert(2, "device_type", 'desktop', True)

        else :
            dataFrame.insert(2, "device_type", 'total', True)

        dataFrame.insert(3, "domain", inputConverter('domain', domain), True)
        
        return dataFrame
    
    elif item == 'all':
        dataFrame = getSimilarwebData_all(inputConverter('company_id', company), start_date, end_date, inputConverter('site_code', site_code), device_type, metric)
        defaultColumn(dataFrame, site_code)
        dataFrame.insert(2, "device_type", device_type, True)
        dataFrame.insert(3, "company", company, True)

        return dataFrame

def refineSWFrame_SA(segment_id, start_date, end_date, site_code, metric, description, domain):
    dataFrame = getSimilarwebData_SA(segment_id, start_date, end_date, inputConverter('site_code', site_code), metric)
    defaultColumn(dataFrame, site_code)
    dataFrame.insert(2, "domain", domain, True)
    dataFrame.insert(3, "description", description, True)       
     
    return dataFrame

def SW_getData(company, channel, start_date, end_date, site_code, dbTableName, item):
    if item == 'conversion':
        for i in range(len(company)):
            for j in range(len(site_code)):
                for p in range(len(channel)):
                    while True:
                        try:
                            stackTodb(refineSWFrame(item, company[i], 'null', start_date, end_date, site_code[j], channel[p], 'null', 'null'), dbTableName)
                    
                        except urllib.error.HTTPError:
                            print('No Matching Data : {company} X {site_code} X {channel}'.format(company = company[i], site_code = site_code[j], channel = channel[p]))

                        break

    elif item == 'traffic' or item == 'bounce' or item == 'mobile_channel' or item == 'desktop_channel' or item == 'mobile_visitor' or item == 'desktop_visitor':
        for i in range(len(company)):
            for j in range(len(site_code)):
                while True:
                    try:
                        stackTodb(refineSWFrame(item, 'null', company[i], start_date, end_date, site_code[j], 'null', 'null', 'null'), dbTableName)
                
                    except urllib.error.HTTPError:
                        print('No Matching Data : {company} X {site_code}'.format(domain = company[i], site_code = site_code[j]))

                    break
    else:
        print('conversion, traffic, bounce, mobile_channel, desktop_channel 중 하나만 입력하세요')



def SW_getAllTraffic(company, start_date, end_date, site_code, dbTableName, metric, device_type):
    for i in range(len(company)):
        for j in range(len(site_code)):
            for p in range(len(device_type)):
                while True:
                    try:
                        stackTodb(refineSWFrame('all', company[i], 'null', start_date, end_date, site_code[j], 'null', device_type[p], metric), dbTableName)
                
                    except urllib.error.HTTPError:
                        print('No Matching Data : {company} X {site_code} X {device_type}'.format(company = company[i], site_code = site_code[j], device_type = device_type[p]))

                    break
# New
def SW_segmentAnalysis(start_date, end_date, site_code, dbTableName, metric, segment_id, description, domain):
    for i in range(len(segment_id)):
        for j in range(len(site_code)):
            while True:
                try:
                    stackTodb(refineSWFrame_SA(segment_id[i], start_date, end_date, site_code[j], metric, description[i], domain[i]), dbTableName)
            
                except urllib.error.HTTPError:
                    print('No Matching Data : {site_code} X {domain} X {description}'.format(site_code = site_code[j], domain = domain[i], description = description[i]))

                break


def metricToStr(metric):
    return ','.join(metric)


# if __name__ == "__main__":

# visit
    # company = ['apple', 'samsung']
    # start_date = '2021-05'
    # end_date = '2021-06'
    # site_code = ['uk', 'us']
    # dbTableName = 'tb_conversion_mobile_channel_1'
    # channel = ['total', 'direct']
    # # conversion 만 channel 입력 가능
    # item = 'mobile_channel'
    # # item에는 conversion, traffic, bounce, mobile_channel, desktop_channel만 입력 가능


    # SW_getData(company, channel, start_date, end_date, site_code, dbTableName, item)


    # company = ['apple', 'samsung']
    # start_date = '2020-01'
    # end_date = '2022-01'
    # site_code = ['world', 'uk', 'us']
    # dbTableName = 'tb_conversion_traffic_all'
    # metric = ['visits', 'pages-per-visit', 'page-views', 'bounce-rate', 'visit-duration']
    # device_type = ['total', 'desktop', "mobile"]

    # SW_getAllTraffic(company, start_date, end_date, site_code, dbTableName, metric, device_type)

    # segment_id = ["7081ea4c-c5ac-42c4-9e56-ae17d37c4fe7", "1c2dd1c6-fdd6-4319-ac86-409661c518b5", "d73b1c7c-bcef-44f0-8127-9adf7809a32f"]
    # description = ["Cart", "Checkout", "Order"]
    # domain = ["Nike", "Nike", "Nike"]
    # start_date = '2022-01'
    # end_date = '2022-02' 
    # site_code = ['world', 'au', 'uk', 'us']
    # dbTableName = 'tb_segment_analysis_test'
    # metric = ['visits', 'share', 'pages-per-visit', 'page-views', 'bounce-rate', 'visit-duration', 'unique-visitors']

    # SW_segmentAnalysis(start_date, end_date, site_code, dbTableName, metric, segment_id, description, domain)