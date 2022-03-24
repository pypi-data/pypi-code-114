import os
import re
import pandas as pd
from datetime import datetime
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from sentence_transformers import SentenceTransformer
from autoads.models import get_similarity_api, get_similarity_matrix
from autoads.keywords import make_live_request,get_results
from autoads.gads import (add_negative_keywords, get_existing_keywords,
                        get_search_term_report,get_all_ads,create_ad,
                        create_keyword,_handle_googleads_exception,
                        create_adgroup, get_all_shared_sets,get_shared_set_keywords)


email = 'weilbacherindustries@gmail.com' # email in data for seo
api_key = '05f014a493983975' # api key for data for seo
save_path = 'data' #all the csvs will be stored on this folder
path = 'data/google-ads.yaml'
customer_id = '8306215642' #google ads customer id
start_date='2022-01-01'
end_date='2022-01-02'

cost_threshold = 0  # get cost >= cost_threshold
conversion_threshold = 1 #  get conversion >= conversion_threshold
first_threshold = 0.8 # similarity threshold for keyword similarity
second_threshold = 0.8 # similarity threshold for description similarity
third_threshold = 0.35 # similarity threshold for seed keyword and keywords3

negative_first_threshold = 0.8 # if keyword similarity <= negative_threshold and conversion == 0 keyword negative
negative_second_threshold = 0.8 # if keyword similarity <= negative_threshold and conversion == 0 keyword negative
negative_third_threshold = 0.35 # if keyword similarity <= negative_threshold and conversion == 0 keyword negative

similarity_model_path = 'Maunish/ecomm-sbert' # this model is already uploaded on huggingface so no need to download

os.makedirs(save_path,exist_ok=True)
os.makedirs(save_path+'/history',exist_ok=True)
googleads_client = GoogleAdsClient.load_from_storage(path=path, version="v9")

print("Getting existing keywords")
df_existing = get_existing_keywords(googleads_client,customer_id)
# df_existing = pd.read_csv('data/df_existing.csv')
keywords_to_remove = df_existing[df_existing['camp_status'].isin(['ENABLED'])]['keyword_name'].unique().tolist()

print("Getting search term report")
df_search_term_report = get_search_term_report(googleads_client,customer_id,start_date,end_date)
# df_search_term_report = pd.read_csv('data/search_term_df.csv')
df_search_term_report = df_search_term_report[~df_search_term_report['stv_status'].isin(['EXCLUDED','ADDED_EXCLUDED'])]
df_search_term_report = df_search_term_report.query("(campaign_status == 'ENABLED') & (adgroup_status == 'ENABLED')")
df_search_term_report['keyword_length'] = df_search_term_report['stv_search_term'].apply(lambda x:len(x))
df_search_term_report = df_search_term_report[df_search_term_report['keyword_length']<=80]
df_search_term_report = df_search_term_report.merge(df_existing.loc[:,['adgroup_id','keyword_name']],on='adgroup_id',how='left')
df_search_term_report['Keywords'] = df_search_term_report['stv_search_term']
df_search_term_report['Keywords2'] = df_search_term_report['keyword_name']

df_search_term_report['sum_conversion'] = df_search_term_report.groupby('date')['metrics_conversions'].transform(sum)
df_search_term_report_negative = df_search_term_report.loc[df_search_term_report['sum_conversion']==0]
# df_search_term_report_negative.to_csv(save_path+'/df_search_term_report_negative.csv',index=False)

df_exclude_from_negative = get_shared_set_keywords(googleads_client,customer_id)
exclude_keywords = df_exclude_from_negative['shared_criterion_keyword_text'].unique().tolist()
df_search_term_report_negative = df_search_term_report_negative.loc[~df_search_term_report_negative['stv_search_term'].isin(exclude_keywords)]
df_search_term_report_negative = df_search_term_report_negative.loc[df_search_term_report_negative['metrics_cost']>=cost_threshold * 1000000]
df_search_term_report_negative = df_search_term_report_negative.drop_duplicates("stv_search_term")
# df_search_term_report_negative.to_csv(save_path+'/df_search_term_report_negative.csv',index=False)

df_search_term_report = df_search_term_report.loc[df_search_term_report['metrics_conversions']>=conversion_threshold]
df_search_term_report = df_search_term_report[~df_search_term_report["Keywords"].isin(keywords_to_remove)]
df_search_term_report['camp_id'] = df_search_term_report['adgroup_camp'].apply(lambda x: x.split('/')[-1])
df_search_term_report =  df_search_term_report.drop_duplicates('Keywords')

print("Getting ads data")
df_ads_data = get_all_ads(googleads_client,customer_id)
# df_ads_data = pd.read_csv('data/df_ads_data.csv')
df_ads_data = df_ads_data.drop_duplicates(['adgroup_id']).reset_index(drop=True)

campaign_id_ads_data = df_ads_data['campaign_id'].unique().tolist()
ad_group_id_ads_data = df_ads_data['adgroup_id'].unique().tolist()

df_search_term_report = df_search_term_report[(df_search_term_report['camp_id'].isin(campaign_id_ads_data)) |
                                            (df_search_term_report['adgroup_id'].isin(ad_group_id_ads_data))].reset_index(drop=True)

model = SentenceTransformer(similarity_model_path)

def calculate_similarity(df,model,first_threshold,second_threshold,third_threshold,negative=False):
    print("Calculating First similarity keywords")
    df['Keywords'] = df['Keywords'].apply(lambda x:str(x))
    df['Keywords2'] = df['Keywords2'].apply(lambda x:str(x))

    keywords1 = df['Keywords'].tolist()
    keywords2 = df['Keywords2'].tolist()
    df['first_similarity'] = get_similarity_api(model,keywords1,keywords2)

    print("Calculating second similarity")
    tasks = [
        'organic',
        # 'people_also_ask',
    ]
    task_params = {
        'organic': ['description'],
        # 'people_also_ask': ['title'],
    }

    print("Getting Descriptions")
    seed_keywords = df["Keywords2"].unique().tolist()
    for keyword in seed_keywords:
        print(keyword)
        response = make_live_request(keyword,email,api_key,depth=5)
        if response['tasks'][0]['result']:
            results = get_results(response,tasks,task_params)
            organic_description = str([x.replace(",","") for x in results['organic_description']])
            organic_description = organic_description.replace("[","").replace("]","")
            df.loc[df["Keywords2"]== keyword,'seed_organic_description'] = str(organic_description)
        else:
            print("Failed to get organic description")
            df.loc[df["Keywords2"]== keyword,'seed_organic_description'] =  keyword

    all_keywords = df["Keywords"].unique().tolist()
    for keyword in all_keywords:
        print(keyword)
        response = make_live_request(keyword,email,api_key,depth=5)
        if response['tasks'][0]['result']:
            results = get_results(response,tasks,task_params)
            organic_description = str([x.replace(",","") for x in results['organic_description']])
            organic_description = organic_description.replace("[","").replace("]","")
            df.loc[df["Keywords"]== keyword,'organic_description'] = organic_description
        else:
            print("Failed to get organic description")
            df.loc[df["Keywords"]== keyword,'organic_description'] = [keyword]  

    print("Performing similarity using organic description")
    for i,row in df.iterrows():
        all_titles = row['seed_organic_description'].split(',')
        all_seed_titles = row['organic_description'].split(',')
        similarity_matrix = get_similarity_matrix(model,all_titles,all_seed_titles)
        df.loc[i,'second_similarity'] = similarity_matrix.max(axis=1).mean()

    def remove_word(row):
        keyword1 = re.split("\s|(?<!\d)[,-](?!\d)",row['Keywords'])
        keyword2 = re.split("\s|(?<!\d)[,-](?!\d)",row['Keywords2'])
        keyword = [x for x in keyword1 if x not in keyword2]
        return "" if len(keyword) == 0 else ' '.join(keyword)

    df['Keywords3'] = df.apply(remove_word,axis=1)
    df['Keywords3'] = df['Keywords3'].apply(lambda x:str(x))

    print("Performing third similarity")
    keywords1 = df['Keywords2'].tolist()
    keywords2 = df['Keywords3'].tolist()
    df['third_similarity'] = get_similarity_api(model,keywords1,keywords2)

    if not negative:
        df = df[df['first_similarity']  >= first_threshold]
        df = df[df['second_similarity'] >= second_threshold]
        df = df[df['third_similarity']  >= third_threshold]
    else:
        df = df[df['first_similarity']  <= first_threshold]
        df = df[df['second_similarity'] <= second_threshold]
        df = df[df['third_similarity']  <= third_threshold]

    return df

info_dict = {
        'campaign_id': list(),
        'adgroup_id': list(),
        'shared_set_id': list(),
        'keyword_id': list(),
        'keyword_id2': list(),
        'type':list(),
}

if len(df_search_term_report) != 0:
    df_search_term_report = calculate_similarity(df_search_term_report,
                                                model,
                                                first_threshold,
                                                second_threshold,
                                                third_threshold,
                                                negative=False)
    df_search_term_report.to_csv(save_path+'/df_search_term_report.csv',index=False)

    ads_to_copy_dict = {
        'headlines_to_copy': list(),
        'descriptions_to_copy': list(),
        'final_url_to_copy': list(),
        'path1_to_copy' : list(),
        'path2_to_copy' : list(),
        'adgroup_id_created' : list(),
        'campaign_to_copy_to': list()
    }

    print("Copying data for creating ads")
    for i,row in df_search_term_report.iterrows():
        ad_group_id = row['adgroup_id']
        campaign_id = row['camp_id']
        if ad_group_id in ad_group_id_ads_data:
            headlines_to_copy = df_ads_data.loc[df_ads_data['adgroup_id']==ad_group_id,'headline_keywords'].tolist()[0]

            existing_keywords = df_existing.loc[df_existing['adgroup_id']==ad_group_id,'keyword_name'].unique().tolist()
            keyword_in_search_term = row['stv_search_term']
            headlines_to_copy = list(set([keyword_in_search_term]+headlines_to_copy))

            descriptions_to_copy = df_ads_data.loc[df_ads_data['adgroup_id']==ad_group_id,'ad_description'].tolist()[0]

            final_url_to_copy = df_ads_data.loc[df_ads_data['adgroup_id']==ad_group_id,'final_url'].tolist()[0][0]

            path1_to_copy = df_ads_data.loc[df_ads_data['adgroup_id']==ad_group_id,'path1'].tolist()[0]
            path2_to_copy = df_ads_data.loc[df_ads_data['adgroup_id']==ad_group_id,'path2'].tolist()[0]

            ads_to_copy_dict['headlines_to_copy'].append(headlines_to_copy)
            ads_to_copy_dict['descriptions_to_copy'].append(descriptions_to_copy)
            ads_to_copy_dict['final_url_to_copy'].append(final_url_to_copy)
            ads_to_copy_dict['path1_to_copy'].append(path1_to_copy)
            ads_to_copy_dict['path2_to_copy'].append(path2_to_copy)
        
        elif campaign_id in campaign_id_ads_data:
            headlines_to_copy = df_ads_data.loc[df_ads_data['campaign_id']==campaign_id,'headline_keywords'].tolist()[0]

            existing_keywords = df_existing.loc[df_existing['campaign_id']==campaign_id,'keyword_name'].unique().tolist()
            keyword_in_search_term = row['stv_search_term']
            headlines_to_copy = list(set([keyword_in_search_term]+headlines_to_copy))

            descriptions_to_copy = df_ads_data.loc[df_ads_data['campaign_id']==campaign_id,'ad_description'].tolist()[0]

            final_url_to_copy = df_ads_data.loc[df_ads_data['campaign_id']==campaign_id,'final_url'].tolist()[0][0]

            path1_to_copy = df_ads_data.loc[df_ads_data['campaign_id']==campaign_id,'path1'].tolist()[0]
            path2_to_copy = df_ads_data.loc[df_ads_data['campaign_id']==campaign_id,'path2'].tolist()[0]

            ads_to_copy_dict['headlines_to_copy'].append(headlines_to_copy)
            ads_to_copy_dict['descriptions_to_copy'].append(descriptions_to_copy)
            ads_to_copy_dict['final_url_to_copy'].append(final_url_to_copy)
            ads_to_copy_dict['path1_to_copy'].append(path1_to_copy)
            ads_to_copy_dict['path2_to_copy'].append(path2_to_copy)


    if len(df_search_term_report) != 0:
        answer = input("Upload the keywords from the report and create ads for it ? (y/n)  ")
        #code for expanding existing campaign
        if answer == 'y' or answer == 'Y':
            print("Adding to existing campaign")
            try:
                for i, row in df_search_term_report.iterrows():
                    keyword = row['Keywords']
                    campaign_id = str(int(row['camp_id']))
                    ad_group = create_adgroup(googleads_client,customer_id,campaign_id, adgroupName=keyword)
                    if ad_group is None:
                        continue
                    ad_group_id = ad_group.split('/')[-1]
                    keyword_id1 = create_keyword(
                        googleads_client,customer_id,
                        ad_group_id, keyword, kw_type='PHRASE')
                    keyword_id1 = keyword_id1.split('~')[-1]
                    keyword_id2 = create_keyword(
                        googleads_client,customer_id,
                        ad_group_id, keyword, kw_type='EXACT')
                    keyword_id2 = keyword_id2.split('~')[-1]
                    info_dict['campaign_id'].append(campaign_id)
                    info_dict['adgroup_id'].append(ad_group_id)
                    info_dict['shared_set_id'].append("-")
                    info_dict['keyword_id'].append(keyword_id1)
                    info_dict['keyword_id2'].append(keyword_id2)
                    info_dict['type'].append('expanded')
                    ads_to_copy_dict['adgroup_id_created'].append(ad_group_id)
                    ads_to_copy_dict['campaign_to_copy_to'].append(campaign_id)

                print(f"{df_search_term_report.shape[0]} campaigns expanded")
            except GoogleAdsException as ex:
                _handle_googleads_exception(ex)
            
            print("Copying ads to created ad groups")
            df_ads_to_copy = pd.DataFrame(ads_to_copy_dict)
            df_ads_to_copy['path1_to_copy'].fillna("",inplace=True)
            df_ads_to_copy['path2_to_copy'].fillna("",inplace=True)
            df_ads_to_copy.to_csv(save_path+'/df_ads_to_copy.csv',index=False)

            for i,row in df_ads_to_copy.iterrows():
                adgroup_id_created = row['adgroup_id_created']
                headlines_to_copy = row['headlines_to_copy']
                descriptions_to_copy = row['descriptions_to_copy']
                final_url_to_copy = row['final_url_to_copy']
                path1_to_copy = row['path1_to_copy']
                path2_to_copy = row['path2_to_copy']

                headlines_to_copy = [x for x in headlines_to_copy if len(x) <= 30][:15]
                descriptions_to_copy = descriptions_to_copy[:3]

                if len(headlines_to_copy) != 0 and len(descriptions_to_copy) != 0:
                    create_ad(googleads_client,customer_id,adgroup_id_created,
                                final_url_to_copy,headlines_to_copy,descriptions_to_copy,
                                path1_to_copy,path2_to_copy)
                else:
                    print("Missing headlines or descriptions")
    else:
        print("No keywords to add into existing campaigns")
else:
    print("No keywords to add into existing campaigns") 



if len(df_search_term_report_negative) != 0:
    df_search_term_report_negative = calculate_similarity(df_search_term_report_negative,
                                                model,
                                                negative_first_threshold,
                                                negative_second_threshold,
                                                negative_third_threshold,
                                                negative=True)
    print(df_search_term_report_negative.shape)
    df_search_term_report_negative.to_csv(save_path+'/df_search_term_report_negative.csv',index=False)

    if len(df_search_term_report_negative) != 0:
        answer = input("Do you want to upload negative keywords? (y/n): ")
        if answer == 'y' or answer == 'Y':
            print("Get Shared Set List")
            df_shared_set = get_all_shared_sets(googleads_client,customer_id)
            for i,row in df_shared_set.iterrows():
                print("No - Id - Name")
                print(f"{i} - {row['shared_set_id']} - {row['shared_set_name']}")
            answer = int(input("Select the number from above list: "))
            shared_set_id = df_shared_set.loc[i].at['shared_set_id']
            negative_keywords = df_search_term_report_negative['stv_search_term'].unique().tolist()
            negative_keywords = [x for x in negative_keywords if x not in exclude_keywords]
            negative_keywords = [x for x in negative_keywords if len(x) <= 80]
            if len(negative_keywords) != 0:
                resourse_names_list1 = add_negative_keywords(googleads_client,customer_id,shared_set_id,negative_keywords,kw_type='PHRASE')
                resourse_names_list2 = add_negative_keywords(googleads_client,customer_id,shared_set_id,negative_keywords,kw_type='EXACT')

                keyword_ids1 = [x.resource_name.split('~')[-1] for x in resourse_names_list1]
                keyword_ids2 = [x.resource_name.split('~')[-1] for x in resourse_names_list2]

                info_dict['campaign_id'].extend(len(keyword_ids1)*["-"])
                info_dict['adgroup_id'].extend(len(keyword_ids1)*["-"])
                info_dict['shared_set_id'].extend(len(keyword_ids1)*[str(shared_set_id)])
                info_dict['keyword_id'].extend(keyword_ids1)
                info_dict['keyword_id2'].extend(keyword_ids2)
                info_dict['type'].extend(len(keyword_ids1)*["negative"])
            else:
                print("No keywords to add in negative list")
    else:
        print("No keywords to add in negative list")
else:
    print("No keywords to add in negative list")

info_df = pd.DataFrame.from_dict(info_dict)
info_df.to_csv(save_path+f'/history/{datetime.now().strftime("%m-%d-%Y %H-%M-%S")}.csv', index=False)
