import requests
from bs4 import BeautifulSoup as bs

def esearch(query, db='pubmed'):
    '''
    Function to search for UIDs of studies of interest
    Output: list of UIDs
    
    Args:
        query: string search term.
    '''
    
    # Creating eSearch URL
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=" + db + "&term=" + query + \
        "&usehistory=y&api_key=7aa5da5090966cca7cac857543588887b908"
            
    # Requesting URL
    r = requests.get(url)
    
    # Parsing Request Contents
    soup = bs(r.content, 'html.parser')
    
    # Getting WebENV and QueryKey
    web = soup.find('webenv').get_text()
    key = soup.find('querykey').get_text()
    
    # Returning WebENV and QueryKey to find UID List
    return web, key
