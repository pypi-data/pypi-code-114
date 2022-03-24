import os
import uuid
import pandas as pd
from datetime import datetime
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from autoads.keywords import get_keywords_metrics
from autoads.gads import create_adgroup, create_campaign, create_keyword, _handle_googleads_exception

df_path = 'data/keywords_to_upload.csv' # specify keywords to uplod csv here
save_path = 'data'
path = 'data/google-ads.yaml'
customer_id = '8306215642' #google ads customer id

email = 'weilbacherindustries@gmail.com'  # email in data for seo
api_key = '05f014a493983975'  # api key for data for seo

match_extract = ['exact', 'phrase']
budget = 100  # pass in USD

os.makedirs(save_path,exist_ok=True)
os.makedirs(save_path+'/history',exist_ok=True)
googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v9")

df = pd.read_csv(df_path)
df = df.drop_duplicates("Keywords")
df_expand = df[~df['camp_id'].isna()].reset_index(drop=True)
df_create = df[df['camp_id'].isna()].reset_index(drop=True)

info_dict = {
        'campaign_id': list(),
        'adgroup_id': list(),
        'keyword_id': list(),
        'keyword_id2': list(),
        'type':list(),
}

df_beta = get_keywords_metrics(email, api_key, df_create, match_extract)

values = ['volume', 'cpc_exact', 'cpc_phrase']
df_beta.loc[:,values] = df_beta.loc[:,values] / 30
df_beta['total_cost'] = 0.33 * df_beta['volume'] * (( df_beta['cpc_exact'] + df_beta['cpc_phrase']) / 2) 
df_beta['total_cost'] = df_beta['total_cost'].cumsum()
df_beta = df_beta.sort_values(by=['total_cost'], na_position='last')
df_beta = df_beta[df_beta['total_cost'] <= budget].reset_index(drop=True)

# spendings = df_beta['total_cost'].iloc[-1]

if len(df_expand) != 0:
    #code for expanding existing campaign
    print("Adding to existing campaign")
    try:
        for i, row in df_expand.iterrows():
            keyword = row['Keywords']
            campaign_id = str(int(row['camp_id']))
            ad_group = create_adgroup(googleads_client,customer_id,campaign_id, adgroupName=keyword)
            if ad_group is None:
                continue
            ad_group_id = ad_group.split('/')[-1]
            keyword_id1 = create_keyword(
                googleads_client,customer_id,
                ad_group_id, keyword, kw_type='PHRASE')
            keyword_id1 = keyword_id1.split('/')[-1]
            keyword_id2 = create_keyword(
                googleads_client,customer_id,
                ad_group_id, keyword, kw_type='EXACT')
            keyword_id2 = keyword_id2.split('/')[-1]
            info_dict['campaign_id'].append(campaign_id)
            info_dict['adgroup_id'].append(ad_group_id)
            info_dict['keyword_id'].append(keyword_id1)
            info_dict['keyword_id2'].append(keyword_id2)
            info_dict['type'].append('expanded')
        print(f"{df_expand.shape[0]} campaigns expanded")
    except GoogleAdsException as ex:
        _handle_googleads_exception(ex)
else:
    print("No keywords to add into existing campaigns")

# code for ceating new campaign
if len(df_create) != 0:
    try:
#         if spendings < budget:
#             print('Creatinng Beta Campaigns')
#             seed_keywords = df.groupby(['Keywords2']).groups
#             for k, d in seed_keywords.items():
#                 campaign = create_campaign(googleads_client, customer_id, campaignName=f'beta_{k}',
#                                         budgetName=k+'_budget_'+f"{uuid.uuid4()}", budgetDollars=budget)
#                 campaign_id = campaign.split('/')[-1]
#                 data = df.iloc[d]['Keywords'].tolist()
#                 for keyword in data:
#                     ad_group = create_adgroup(
#                         googleads_client, customer_id, campaign_id, adgroupName=keyword)
#                     if ad_group is None:
#                         continue
#                     ad_group_id = ad_group.split('/')[-1]
#                     keyword_id1 = create_keyword(
#                         googleads_client, customer_id,
#                         ad_group_id, keyword, kw_type='BROAD')
#                     keyword_id1 = keyword_id1.split('/')[-1]
#                     info_dict['campaign_id'].append(campaign_id)
#                     info_dict['adgroup_id'].append(ad_group_id)
#                     info_dict['keyword_id'].append(keyword_id1)
#                     info_dict['keyword_id2'].append(' ')
#                     info_dict['type'].append('created_beta')
#             info_df = pd.DataFrame.from_dict(info_dict)
#             df = pd.concat([df, info_df], axis=1)
#             df.to_csv(save_path+'/beta_info.csv', index=False)
#             print(f"{len(seed_keywords)} new campaigns created")
        
#         else:
            print("Creating new Campaigns")
            seed_keywords = df_beta.groupby(['Keywords2']).groups  
            for k, d in seed_keywords.items():
                campaign = create_campaign(googleads_client,customer_id,campaignName=k,
                                           budgetName=k+'_budget_'+f"{uuid.uuid4()}", budgetDollars=budget)
                campaign_id = campaign.split('/')[-1]
                data = df_beta.iloc[d]['Keywords'].tolist()
                for keyword in data:
                    ad_group = create_adgroup(googleads_client,customer_id,campaign_id, adgroupName=keyword)
                    if ad_group is None:
                        continue
                    ad_group_id = ad_group.split('/')[-1]
                    keyword_id1 = create_keyword(
                        googleads_client,customer_id,
                        ad_group_id, keyword, kw_type='PHRASE')
                    keyword_id1 = keyword_id1.split('/')[-1]
                    keyword_id2 = create_keyword(
                        googleads_client,customer_id,
                        ad_group_id, keyword, kw_type='EXACT')
                    keyword_id2 = keyword_id2.split('/')[-1]
                    info_dict['campaign_id'].append(campaign_id)
                    info_dict['adgroup_id'].append(ad_group_id)
                    info_dict['keyword_id'].append(keyword_id1)
                    info_dict['keyword_id2'].append(keyword_id2)
                    info_dict['type'].append('created')
            print(f"{len(seed_keywords)} new campaigns created")
    except GoogleAdsException as ex:
        _handle_googleads_exception(ex)
else:
    print("No new campaigns to create")

info_df = pd.DataFrame.from_dict(info_dict)
df = pd.concat([df, info_df], axis=1)
df.to_csv(save_path+f'/history/{datetime.now().strftime("%m-%d-%Y %H-%M-%S")}.csv', index=False)
