import uuid
import datetime
import pandas as pd
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from autoads.gads import (create_adgroup, create_campaign, create_keyword, 
                          _handle_googleads_exception, update_campaign, get_existing,
                        add_negative_keywords, get_all_shared_sets, get_search_term_report)

# specify keywords to uplod csv here
beta_df_path = 'M:/GAds/Google-Ads-Project/data/beta_info.csv'
beta_df = pd.read_csv(beta_df_path)

save_path = 'M:/GAds/Google-Ads-Project/data'
# path = 'M:/GAds/hubspot_andrew/google-ads.yaml'
# customer_id = '8306215642'
path = 'M:/GAds/google-ads_something.yaml'
customer_id = '7213150354'

start_date = '2022-01-01'
end_date = '2022-03-15'

shared_set_id = 8989534941
conversion_threshold = 1

start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v9")
    
def get_campaign_name(googleads_client, customer_id, campaign_id):
    ga_service = googleads_client.get_service("GoogleAdsService")
    query = f"""
            SELECT 
                campaign.id, 
                campaign.name 
                FROM campaign 
            WHERE 
                campaign.id = {campaign_id} 
            """
    search_request = googleads_client.get_type("SearchGoogleAdsStreamRequest")
    search_request.customer_id = customer_id
    search_request.query = query
    stream = ga_service.search_stream(search_request)
    for batch in stream:
        for row in batch.results:
            return str(row.campaign.name)
    
def get_search_term_alpha():
    print(get_all_shared_sets(googleads_client, customer_id))
    info_dict = {
    'campaign_id': list(),
    'adgroup_id': list(),
    'keyword_id': list(),
}
    df_search_term = pd.read_csv('M:/GAds/mock_search_term.csv')#get_search_term_report(
        # googleads_client, customer_id, start_date, end_date, full=True)
    df_search_term = df_search_term[  
        # df_search_term['stv_status'].isin(['ENABLED']) &
        df_search_term['adgroup_status'].isin(['ENABLED']) &
        df_search_term['campaign_status'].isin(['ENABLED'])
    ]

    existing_df = get_existing(googleads_client, customer_id) #pd.read_csv('M:/GAds/existing_and.csv')
    existing_df = existing_df[~existing_df['camp_id'].isin(beta_df['campaign_id'])].reset_index(drop=True)
    filtered_search_term = df_search_term[df_search_term['campaign_id'].isin(beta_df['campaign_id'])].reset_index(drop=True)
    search_term_negatives = filtered_search_term[filtered_search_term['metrics_conversions'] < conversion_threshold].reset_index(drop=True)
    filtered_search_term = filtered_search_term[filtered_search_term['metrics_conversions'] >= conversion_threshold].reset_index(drop=True)
    existing_keywords = existing_df['keyword_name'].tolist()
    
    campaigns = filtered_search_term.groupby(['campaign_id']).groups
    for k, d in campaigns.items():
        try:
            data_kw = filtered_search_term.iloc[d]['stv_search_term'].tolist()
            valid = any([True for kw in data_kw if kw not in existing_keywords])
            if valid:
                campaign = create_campaign(googleads_client, customer_id, campaignName=f'alpha_{get_campaign_name(googleads_client, customer_id, str(k))[5:]}',
                                           budgetName=f'{get_campaign_name(googleads_client, customer_id, str(k))[5:]}' +
                                           'alpha_budget_'+f"{uuid.uuid4()}",
                                            budgetDollars=100)
                campaign_id = campaign.split('/')[-1]
                for keyword in data_kw:
                    if keyword not in existing_keywords:
                            existing_keywords.append(keyword)
                            ad_group = create_adgroup(
                                googleads_client, customer_id, campaign_id, adgroupName=keyword)
                            if ad_group is None:
                                continue
                            ad_group_id = ad_group.split('/')[-1]
                            keyword_id1 = create_keyword(
                                googleads_client, customer_id,
                                ad_group_id, keyword, kw_type='EXACT')
                            keyword_id1 = keyword_id1.split('/')[-1]
                            info_dict['campaign_id'].append(campaign_id)
                            info_dict['adgroup_id'].append(ad_group_id)
                            info_dict['keyword_id'].append(keyword_id1)
        except GoogleAdsException as ex:
                _handle_googleads_exception(ex)
    
    negative_keywords = search_term_negatives['stv_search_term'].apply(lambda x : ' '.join(str(x)[:80].split(' ')[:10])).values
    negative_keywords = list(set(negative_keywords))
    print(
        f'adding {negative_keywords.__len__()} negative keywords to {shared_set_id}')
    add_negative_keywords(
        googleads_client, customer_id, shared_set_id, negative_keywords, kw_type='EXACT')
    print('pausing all the beta campaigns')
    for beta_camp_id in beta_df['campaign_id'].tolist():
        update_campaign(googleads_client, customer_id,
                        int(beta_camp_id), status = 'PAUSED')
    info_df = pd.DataFrame.from_dict(info_dict)
    info_df.to_csv(save_path+'/alpha_info.csv', index=False)
    

if __name__ == '__main__':
    get_search_term_alpha()
                
