import requests
from bs4 import BeautifulSoup as bs
from pubmed.esearch import esearch

def esummarize(query, db='pubmed'):
    '''
    Function to retrieve articles from UID list and parse data
    Output: DataFrame of article information
    
    Args:
        query: string search term.
    '''
    
    # Performing eSearch
    web, key = esearch(query, db)
    
    # Creating eSummary URL
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=" + db + "&query_key=" + key + "&WebEnv=" + web + \
        "&api_key=7aa5da5090966cca7cac857543588887b908"
    
    # Requesting URL
    r = requests.get(url)
    
    # Parsing Request Contents
    soup = bs(r.content, 'html.parser')
    
    # Returning Raw Data
    return soup