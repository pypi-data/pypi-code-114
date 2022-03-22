import tldextract


def get_domain_and_tld(url):
	"""
	return the domain and tld: forums.news.cnn.com/index.html --> cnn.com, http://bbc.co.uk --> bbc.co.uk
	:type url: str
	:rtype: str
	"""
	if url is None:
		return None

	ext = tldextract.extract(url)
	return f'{ext.domain}.{ext.suffix}'
