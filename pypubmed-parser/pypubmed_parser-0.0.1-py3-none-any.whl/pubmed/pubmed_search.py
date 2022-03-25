# Importing Dependencies
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import warnings
warnings.filterwarnings('ignore')

class pubmed_search:
    def __init__(self, database='pubmed'):
        self.url_base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
        self.api = '7aa5da5090966cca7cac857543588887b908'
        self.db = database
        
    def esearch(self, query):
        '''
        Function to search for UIDs of studies of interest
        Input: query is the string quote term of interest
        Output: list of UIDs
        '''
        # Creating eSearch URL
        url = self.url_base + "esearch.fcgi?db=" + self.db + "&term=" + query + "&usehistory=y&api_key=" \
                + self.api
                
        # Requesting URL
        r = requests.get(url)
        
        # Parsing Request Contents
        soup = bs(r.content, 'html.parser')
        
        # Getting WebENV and QueryKey
        web = soup.find('webenv').get_text()
        key = soup.find('querykey').get_text()
        
        # Returning WebENV and QueryKey to find UID List
        return web, key
    
    def esummarize(self, query):
        # Performing eSearch
        web, key = self.esearch(query)
        
        # Creating eSummary URL
        url = self.url_base + "esummary.fcgi?db=" + self.db + "&query_key=" + key + "&WebEnv=" + web + "&api_key=" + self.api
        
        # Requesting URL
        r = requests.get(url)
        
        # Parsing Request Contents
        soup = bs(r.content, 'html.parser')
        
        # Returning Raw Data
        return soup
    
    def create_dataframe(self, query, clean='yes'):
        
        # Getting eSummarize Data
        soup = self.esummarize(query)
        
        # Creating Empty Lists
        title = []
        pmid = []
        doi = []
        journal = []
        pubtype = []
        pubdate = []
        language = []
        author = []
        first_author = []

        # Finding All Important Article Details
        for i in soup.find_all('docsum'):
            title.append(i.find(attrs={'name': 'Title'}).get_text())
            pmid.append(i.find('id').get_text())
            try:
                doi.append(i.find(attrs={'name': 'DOI'}).get_text())
            except:
                doi.append('NA')
                pass
            pubdate.append(i.find(attrs={'name': 'PubDate'}).get_text())
            journal.append(i.find(attrs={'name': 'Source'}).get_text())
            language.append(i.find(attrs={'name': 'Lang'}).get_text())
            try:
                pubtype.append(i.find(attrs={'name': 'PubType'}).get_text())
            except:
                pubtype.append('NA')
                pass
    
            # Author List
            author_raw = []
            for j in i.find(attrs={'name': 'AuthorList'}).find_all(attrs={'name': 'Author'}):
                author_raw.append(j.get_text())
            author.append(author_raw)
        
        # Finding First Author
        for i in author:
            try:
                first_author.append(i[0])
            except:
                first_author.append('NA')
                pass
    
        # Creating DataFrame 
        df = pd.DataFrame(columns=['pmid', 'title', 'pubdate', 'first_author', 'authors', 'journal', 'pubtype', 'doi', 'language'])
        df['pmid'] = pmid
        df['title'] = title
        df['pubdate'] = pubdate
        df['first_author'] = first_author
        df['authors'] = author
        df['journal'] = journal
        df['pubtype'] = pubtype
        df['doi'] = doi
        df['language'] = language
        
        # Updating Publication Date to Publication Year
        df['pubdate'] = pd.to_datetime(df['pubdate']).dt.year
        
        if clean == 'yes':
            df = df[df['language']=='English'].drop(['language'], axis=1)
            return df
            
        if clean == 'no':
            df_raw = df
            df_clean = df[df['language']=='English'].drop(['language'], axis=1)
            return df_raw, df_clean