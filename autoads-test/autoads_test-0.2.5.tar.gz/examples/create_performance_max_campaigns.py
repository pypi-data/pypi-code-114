import uuid
from autoads.gads import (PerformanceMaxCampaign, Audience,
                          get_all_ads, get_all_audience,
                          get_existing_keywords, get_search_term_report)
from google.ads.googleads.client import GoogleAdsClient

path = '/home/maunish/Upwork Projects/Google-Ads-Project/examples/google-ads.yaml'
customer_id = '6554081276'  # google ads customer id

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

df_existing['audience_keywords'] = df_existing['stv_search_term'] + \
    df_existing['keyword_name']

# path = '/home/maunish/Upwork Projects/Google-Ads-Project/examples/google-ads.yaml'
# customer_id = '9606147127'  # google ads customer id
# googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v10")

print("Get Audience Data")
df_audience = get_all_audience(googleads_client, customer_id)
audience_names = df_audience['audience_name'].tolist()
print(audience_names)
for i, row in df_existing.iterrows():
    if row['camp_name'] in audience_names:
        df_existing.loc[i, 'camp_name'] = row['camp_name'] + \
            "_" + str(uuid.uuid4())

print(df_existing['camp_name'])
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

    audience_resource = audience.create(googleads_client, customer_id)

    budget_name = row['camp_name'] + f"_{uuid.uuid4()}"
    budget_dollars = 10
    campaign_name = row['camp_name'] + f"_max"
    target_roas = 2.5
    asset_group_name = row['camp_name'] + f"_asset"
    headlines = flatten_list(row['headline_keywords'])[:5]
    long_headlines = flatten_list(row['headline_keywords'])[:5]
    descriptions = flatten_list(row['ad_description'])[:5]
    bussiness_name = keywords[0]

    campaign = PerformanceMaxCampaign(
        # budget paramaters
        budget_name=budget_name,
        budget_dollars=10,
        # campaign parameters
        campaign_name=campaign_name,
        target_roas=2.5,
        campaign_enabled=False,
        # asset parameters
        audience_resource=audience_resource,
        asset_group_name=asset_group_name,
        headlines=headlines,
        descriptions=descriptions,
        long_headlines=long_headlines,
        business_name=bussiness_name,
        marketing_logos=["https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-google-logos-vector-eps-cdr-svg-download-10.png",
                         "https://www.designbust.com/download/1039/png/google_logo_transparent256.png"],
        marketing_images=["https://gaagl.page.link/Eit5"],
        square_marketing_images=["https://gaagl.page.link/bjYi"],
        youtube_videos=["https://www.youtube.com/watch?v=x1dJa6XC2tA"],
        final_urls=["http://www.example.com"],
        final_mobile_urls=["http://www.example.com"],
        asset_group_enabled=False
    )

    camapaign_resource = campaign.create(googleads_client, customer_id)
