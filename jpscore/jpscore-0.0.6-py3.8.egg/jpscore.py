import requests,re
import pandas as pd
import subprocess as sp

def main():
 sp.call("wget https://github.com/ytakefuji/covid_score_japan/raw/main/jppop.xlsx --no-check-certificate",shell=True)
 df = pd.read_excel('jppop.xlsx',engine='openpyxl')
 df=df[1:48]
 df=df.rename({ 'Unnamed: 1':'jPref'},axis=1)
 df.to_csv('pop.csv')
 print('pop.csv was created')

 print('downloading nhk_news_covid19_prefectures_daily_data.csv file')
 sp.call("wget https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv",shell=True)
 p=pd.read_csv('nhk_news_covid19_prefectures_daily_data.csv')
 date=p['日付'][len(p)-1]

# print('jprefectures file was read...')
# d=open('jprefectures').read().strip()
# d=open('prefectures').read().strip()
# d=d.split(',')
# print('scoring the following ',len(d),' countries...')
# print(d)

 pp=pd.read_csv('pop.csv')
 print('calculating scores of prefectures\n')
 print('score is created in result.csv')
 print('date is ',date)

 d=p.都道府県名.unique()
 print('scoring the following ',len(d),' countries...')

 dd=pd.DataFrame(
  { 
   "prefecture": d,
   "deaths": range(len(d)),
   "population": range(len(d)),
   "score": range(len(d)),
  })
 
 
 for i in d:
 # print(int(p.loc[(p.都道府県名==i) & (p.日付==date),'各地の死者数_累計']))
  dd.loc[dd.prefecture==i,'deaths']=int(p.loc[(p.都道府県名==i) & (p.日付==date),'各地の死者数_累計'])
  dd.loc[dd.prefecture==i,'population']=round(int(pp.loc[(pp.jPref==i[0:2]) | (pp.jPref==i[0:3]),'Population 2019'])/1000,3)
 # print("deaths", int(dd.loc[dd.prefecture==i,'deaths']))
 # print("pop",dd.loc[dd.prefecture==i,'population'])
  dd.loc[dd.prefecture==i,'score']=round(dd.loc[dd.prefecture==i,'deaths']/dd.loc[dd.prefecture==i,'population'],1)
 dd=dd.sort_values(by=['score'])
 dd.to_csv('result.csv',index=False)
 dd=pd.read_csv('result.csv',index_col=0)
 print(dd)
 dd.to_csv('result.csv',encoding='utf_8_sig',index=True)
 sp.call("rm n*.csv p*.csv *.xlsx",shell=True)

if __name__ == "__main__":
 main()
