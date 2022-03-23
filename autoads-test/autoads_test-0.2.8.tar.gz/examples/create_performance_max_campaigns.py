import uuid
import numpy as np
from sentence_transformers import SentenceTransformer
from autoads.models import get_similarity_matrix
from autoads.keywords import make_live_request,get_results
from autoads.gads import (PerformanceMaxCampaign, Audience,
                          get_all_ads, get_all_audience,
                          get_existing_keywords, get_search_term_report)
from google.ads.googleads.client import GoogleAdsClient
# comment
path = 'data/google-ads.yaml'
customer_id = '8306215642' 
email = 'weilbacherindustries@gmail.com' # email in data for seo
api_key = '05f014a493983975' # api key for data for seo

first_threshold = 0.8 # similarity threshold
second_threshold = 0.8

similarity_model_path = 'Maunish/ecomm-sbert' # this model is already uploaded on huggingface so no need to download

googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v10")

print("Getting Existing Keywords")
df_existing = get_existing_keywords(googleads_client, customer_id)
existing_campaign_names = df_existing['camp_name'].unique().tolist()
df_existing = df_existing.query(
    "(camp_status == 'ENABLED') & (adgroup_status == 'ENABLED')")
df_existing = df_existing.groupby(['camp_id', 'camp_name']).agg(
    {"keyword_name": list}).reset_index()

print("Get search term report")
df_search_term_report = get_search_term_report(googleads_client, customer_id)
df_search_term_report = df_search_term_report.groupby("campaign_id").agg({"stv_search_term": set,
                                                                         "metrics_conversions": "sum"}).reset_index()
df_search_term_report['stv_search_term'] = df_search_term_report["stv_search_term"].apply(list)

print("Get ads data")
df_ads_data = get_all_ads(googleads_client, customer_id)
df_ads_data = df_ads_data.groupby('campaign_id').agg({
    "headline_keywords": list,
    "ad_description": list,
    "final_url": list,
    "path1": list,
    "path2": list}).reset_index()

df_existing = df_existing.merge(
    df_search_term_report, how='left', left_on='camp_id', right_on='campaign_id')
df_existing = df_existing.merge(df_ads_data, how='left', on='campaign_id')
df_existing = df_existing[df_existing['metrics_conversions'] > 0]

df_existing = df_existing.dropna()

print("Calculating similarity")
model = SentenceTransformer(similarity_model_path)
for i,row in df_existing.iterrows():
    stv_search_term = row['stv_search_term']
    keyword_name = row['keyword_name']

    print("Calculating first similarity")
    similarity_matrix = get_similarity_matrix(model,stv_search_term,keyword_name)
    max_similarity = similarity_matrix.max(axis=0)
    similarity_indexes = np.where(max_similarity>=first_threshold)[0].tolist()
    stv_search_term = [stv_search_term[x] for x in similarity_indexes]

    if len(stv_search_term) !=0:
        tasks = [
            'organic',
            # 'people_also_ask',
        ]
        task_params = {
            'organic': ['description'],
            # 'people_also_ask': ['title'],
        }

        print("Getting Descriptions")
        search_term_organic_descriptions = list()
        for keyword in stv_search_term:
            print(keyword)
            response = make_live_request(keyword,email,api_key,depth=5)
            if response['tasks'][0]['result']:
                results = get_results(response,tasks,task_params)
                organic_description = results['organic_description']
                organic_description = str([x.replace(",","") for x in results['organic_description']])
                organic_description = organic_description.replace("[","").replace("]","")
                search_term_organic_descriptions.append(organic_description)
            else:
                print("Failed to get organic description")
                search_term_organic_descriptions.append(keyword)


        print("Getting Descriptions")
        keywords_organic_descriptions = list()
        for keyword in keyword_name:
            print(keyword)
            response = make_live_request(keyword,email,api_key,depth=5)
            if response['tasks'][0]['result']:
                results = get_results(response,tasks,task_params)
                organic_description = results['organic_description']
                organic_description = str([x.replace(",","") for x in results['organic_description']])
                organic_description = organic_description.replace("[","").replace("]","")
                keywords_organic_descriptions.append(organic_description)
            else:
                print("Failed to get organic description")
                keywords_organic_descriptions.append(keyword)

        print("Calulating second similarity")
        similarity_matrix = get_similarity_matrix(model,search_term_organic_descriptions,keywords_organic_descriptions)
        max_similarity = similarity_matrix.max(axis=0)
        similarity_indexes = np.where(max_similarity>=second_threshold)[0].tolist()
        stv_search_term = [stv_search_term[x] for x in similarity_indexes]

    df_existing.at[i,'stv_search_term'] = stv_search_term

df_existing['audience_keywords'] = df_existing['stv_search_term'] + df_existing['keyword_name']

# path = '/home/maunish/Upwork Projects/Google-Ads-Project/examples/google-ads.yaml'
# customer_id = '9606147127'  # google ads customer id
# googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v10")

print("Get Audience Data")
df_audience = get_all_audience(googleads_client, customer_id)
audience_names = df_audience['audience_name'].tolist()
for i, row in df_existing.iterrows():
    if (row['camp_name'] in audience_names) or (row['camp_name'] + "_max" in existing_campaign_names):
        df_existing.loc[i, 'camp_name'] = row['camp_name'] + \
            "_" + str(uuid.uuid4())

df_existing.to_csv('data/df_ext.csv', index=False)


def flatten_list(row):
    flat_list = list(set([item for sublist in row for item in sublist]))
    return flat_list

print("Creating performance campaigns")
for i, row in df_existing.iterrows():
    audience_name = row['camp_name']
    audience_description = row['camp_name']
    keywords = list(set(row['audience_keywords']))
    urls = flatten_list(row['final_url'])

    audience = Audience(
        audience_name=audience_name,
        audience_description=audience_description,
        keywords=keywords,
        urls=urls,
    )

    budget_name = row['camp_name'] + f"_{uuid.uuid4()}"
    campaign_name = row['camp_name'] + f"_max"
    asset_group_name = row['camp_name'] + f"_asset"
    headlines = flatten_list(row['headline_keywords'])
    headlines = [x for x in headlines if len(x) <=30][:5]

    min_headlines = np.argmin([len(x) for x in headlines])
    if len(headlines[min_headlines]) > 15:
        headlines[min_headlines] = headlines[min_headlines][:15]

    descriptions = flatten_list(row['ad_description'])
    descriptions = [x for x in descriptions if len(x) <= 90][:5]

    min_description = np.argmin([len(x) for x in descriptions])
    if len(descriptions[min_description]) > 60:
        descriptions[min_description] = descriptions[min_description][:60]
    
    print("Audience Keywords: ",keywords)
    
    long_headlines = input("Long headline: (min 1 max 5 headlines,  90 character max/headline ,user comma to separate): ")
    long_headlines = long_headlines.split(',')
    long_headlines = [x for x in long_headlines if len(x) <= 90][:5]

    business_name = input("Business Name: 25 character max:")
    bussiness_name = business_name[:25]
    budget_dollars = int(input("Budget in integer dollars: "))

    youtube_videos = input("Youtube video full links with id (example https://www.youtube.com/watch?v=x1dJa6XC2tA must be greater than 10 sec)")
    youtube_videos = youtube_videos.split(',')

    marketing_logos = ["https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-google-logos-vector-eps-cdr-svg-download-10.png",
                         "https://www.designbust.com/download/1039/png/google_logo_transparent256.png"]
    marketing_images = ["https://gaagl.page.link/Eit5"]
    square_marketing_images = ["https://gaagl.page.link/bjYi"]
    final_urls = urls
    final_mobile_urls = urls

    audience_resource = audience.create(googleads_client, customer_id)

    campaign = PerformanceMaxCampaign(
        # budget paramaters
        budget_name=budget_name,
        budget_dollars=budget_dollars,
        # campaign parameters
        campaign_name=campaign_name,
        campaign_enabled=False,
        # asset parameters
        audience_resource=audience_resource,
        asset_group_name=asset_group_name,
        headlines=headlines,
        descriptions=descriptions,
        long_headlines=long_headlines,
        business_name=bussiness_name,
        marketing_logos=marketing_logos,
        marketing_images=marketing_images,
        square_marketing_images=square_marketing_images,
        youtube_videos=youtube_videos,
        final_urls=final_urls,
        final_mobile_urls=final_mobile_urls,
        asset_group_enabled=False
    )

    camapaign_resource = campaign.create(googleads_client, customer_id)
