import os
from autoads.gads import get_all_ads,get_existing_keywords,create_ad,remove_ad

from google.ads.googleads.client import GoogleAdsClient
path = 'data/google-ads.yaml'
customer_id = '8306215642' #google ads customer id
save_path = 'data'

os.makedirs(save_path,exist_ok=True)
client = GoogleAdsClient.load_from_storage(path=path, version="v9")

ALLOWED_ENABLED_ADS = 3
df_ads_data = get_all_ads(client,customer_id)
df_exising = get_existing_keywords(client,customer_id)
df_ads_data = df_ads_data.query("(campaign_status == 'ENABLED') & \
                                (adgroup_status == 'ENABLED') & \
                                (adgroup_ad_status == 'ENABLED')")
df_ads_data['ads_in_adgroup'] = df_ads_data.groupby('adgroup_id')['adgroup_id'].transform('count')
df_ads_data['ad_is_poor'] = ((df_ads_data['adgroup_ad_strength'] == 'POOR') & (df_ads_data['metrics_impressions'] == 0)).astype(int)
df_ads_data['poor_ads_in_adgroup'] = df_ads_data.groupby('adgroup_id')['ad_is_poor'].transform(sum)
df_ads_data['ads_space_left'] = (ALLOWED_ENABLED_ADS - df_ads_data['ads_in_adgroup'] + df_ads_data['poor_ads_in_adgroup'])
df_ads_data = df_ads_data.query('ads_space_left > 0')
df_exising = df_exising.query("(camp_status == 'ENABLED') & (adgroup_status == 'ENABLED')")
df_exising['keyword_name'] = df_exising['keyword_name'].apply(str.title)
df_exising = df_exising.groupby('adgroup_id')['keyword_name'].apply(list).reset_index()
df_ads_data = df_ads_data.merge(df_exising[['adgroup_id','keyword_name']],on='adgroup_id',how='left')
df_ads_data = df_ads_data.dropna(subset=['keyword_name'])
df_ads_data['prev_no_of_headlines'] = df_ads_data['headline_keywords'].apply(len)
df_ads_data = df_ads_data[df_ads_data['prev_no_of_headlines']<15]
df_ads_data['headline_keywords'] = df_ads_data['headline_keywords'] + df_ads_data['keyword_name']
df_ads_data['headline_keywords'] = df_ads_data['headline_keywords'].apply(set)
df_ads_data['headline_keywords'] = df_ads_data['headline_keywords'].apply(lambda x: [a for a in x if len(a) <= 30])
df_ads_data['new_no_of_headlines'] = df_ads_data['headline_keywords'].apply(len)
df_ads_data = df_ads_data.query("new_no_of_headlines > 0")
df_ads_data = df_ads_data.query("prev_no_of_headlines != new_no_of_headlines").reset_index(drop=True)
df_ads_data['ads_to_add_per_adgroup'] = df_ads_data.groupby('adgroup_id')['adgroup_id'].transform('count')
df_ads_data_remove = df_ads_data[df_ads_data['ad_is_poor']==1]
df_ads_data = df_ads_data.sort_values(by='metrics_conversions')
df_ads_data.to_csv(save_path+'/df_ads.csv',index=False)

# path = '/home/maunish/Upwork Projects/Google-Ads-Project/examples/google-ads.yaml'
# customer_id = '6554081276' # google ads customer id
# client = GoogleAdsClient.load_from_storage(path=path, version="v9")

if len(df_ads_data_remove) != 0:
    for i, row in df_ads_data_remove.iterrows():
        ad_group_id = row['adgroup_id']
        ad_group_ad_id = row['adgroup_ad_id']
        remove_ad(client,customer_id,ad_group_id,ad_group_ad_id)
    print(f'{df_ads_data_remove.shape[0]} ads removed')
else:
    print("No ads to remove")

df_ads_data['path1'].fillna("",inplace=True)
df_ads_data['path2'].fillna("",inplace=True)

if len(df_ads_data) != 0:
    answer = input("Do you want to add the ads in the file df_ads.csv (y/n) ?")
    if answer in ['y','Y']:
        df_ads_grouped = df_ads_data.groupby('adgroup_id')
        for name,group in df_ads_grouped:
            number_of_ads_to_add = group['ads_space_left'].iloc[0]
            df_group = group.iloc[:number_of_ads_to_add]
            for i,row in df_group.iterrows():
                adgroup_id = row['adgroup_id']
                headlines = row['headline_keywords']
                descriptions = row['ad_description']
                final_url = row['final_url'][0]
                path1 = row['path1']
                path2 = row['path2']
                
                headlines = headlines[:15]
                descriptions = descriptions[:3]

                if len(headlines) != 0 and len(descriptions) != 0:
                    create_ad(client,customer_id,adgroup_id,final_url,headlines,descriptions,path1,path2,enable=True)
                else:
                    print("Missing headlines or descriptions")
else:
    print("No ads to add")
