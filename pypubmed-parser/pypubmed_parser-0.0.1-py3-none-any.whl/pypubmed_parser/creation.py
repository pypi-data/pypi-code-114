import pandas as pd
import numpy as np
from pubmed.esummarize import esummarize

def create_dataframe(query):
        
    # Getting eSummarize Data
    soup = esummarize(query)
    
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

    return df
