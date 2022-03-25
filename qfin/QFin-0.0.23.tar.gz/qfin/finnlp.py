import threading
import heapq
import urllib.request
import re
import bs4 as bs
import googlesearch
import nltk


# Outpreform garch implied volatility estimates weekly/daily using webscraped data
# Google lookback search, does the algo get affected over the time before the on or before date
# Look for correlations in bloomberg commodity data and sentiment/word count analysis

class LinkScraper:

    """
    LinkScraper class is used to gather the highest ranking websites
    for the arg:search based on googlesearch (google's search algorithm)
    """

    def __init__(self, search, n):
        # List of returned urls
        self.urls = []
        # for each url returned append to list of urls
        for url in googlesearch.search(search, stop=n):
            self.urls.append(url)


class WebScraper:

    """
    WebScraper class is used to parse the HTML of a url to extract data from
    certain tags
    """

    # TODO: Extract text from a pdf
    def __init__(self, url):
        # Adds a User-Agent Header to the url Request
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/'
                '537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        # Opens a url request for initialized urllib.request.Request (req)
        scraped_data = urllib.request.urlopen(req)
        # Raw Scraped Text
        article = scraped_data.read()
        # Parses with bs4 and xml
        parsed_article = bs.BeautifulSoup(article, 'lxml')
        # Find all paragraphs
        paragraphs = parsed_article.find_all('p')
        # Article text string to append parsed HTML
        self.article_text = ""
        # Append all paragraphs to article_text variable
        for p in paragraphs:
            # article_text+='\n' # For readability of raw data
            self.article_text += p.text
        # print(article_text, '\n\n') # For readability of raw data


class Summarizer:

    """
    Summarizer class is used to summarize tags parsed by the WebScraper based
    on frequency and relevance to search
    """

    def __init__(self, article_text, search, n):
        # Preprocessing
        # Removing Square Brackets and Extra Spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)
        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        sentence_list = nltk.sent_tokenize(article_text)
        stopwords = nltk.corpus.stopwords.words('english')
        # Find Weighted Frequency of Occurrence
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                # TODO: Analyze frequency against relevance scores
                # TODO: If its quantitative (number) rank it higher, if its relevant to the
                # keyword arguemnt (add it) make it more relevant
                if word in search.split():  # if relevant rank higher
                    word_frequencies[word] += 5
                else:
                    word_frequencies[word] += 1
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (
                word_frequencies[word] / maximum_frequency
                )
        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        summary_sentences = heapq.nlargest(
            n, sentence_scores, key=sentence_scores.get
        )
        # New line for summaries
        self.summary = '\n'.join(summary_sentences)
        # TODO: Get Excel plugin for training_data extraction
        # Custom Delimiter for extracting training_data
        self.summary += '***'
        print(self.summary)


class CitationGenerator:
    # Use python-autocite
    pass


class SentimentAnalysis:
    """
    SentimentAnalysis class is used to rank different dimensions of a summary
    by [-1, 1] by a vector of Nx1 where N are the dimensions of evaluation
    """

    # TODO: Build CNN
    # Initialize and train the convolutional neural network
    def __init__(self):
        pass


class Analyst:
    """
    Analyst class is used to pipeline the LinkScraper, WebScraper, Summarizer,
    and SentimentAnalysis classes to better understand the subject of the query
    The comprehension comes from the desired Nx1 output vector for each summary
    """

    # TODO: Give the analyst proper hierarchical purpose
    # Currently the analyst is fetching summaries to be used to train CNN
    # Current issue is merging of rows in excel for labeling
    def __init__(self, search, n, sl, fall_through, write_file):
        # Get most recent news Links
        # WebScrape each Link
        # Summarize each WebScrape
        # Analyze each Summary

        # Item(s) to reserach
        self.search = search
        # Number of sources
        self.n = n
        # Summary length (sentances)
        self.sl = sl
        # Return to main thread before all existing threads terminate
        self.fall_through = fall_through
        # Write the researched summaries to a file
        self.write_file = write_file
        # List of sources
        self.urls = []
        # List of summaries
        self.summaries = []
        # List of threads
        self.threads = []
        # Gather Links to WebScrape
        for url in LinkScraper(search, n).urls:
            # Create and append a thread for each link and url Request
            # self.scrape_and_summarize(url, search) # Multi-threaded process
            # If n > x, multi-threading will be faster
            self.threads.append(
                threading.Thread(
                    target=self.scrape_and_summarize, args=(
                        url, search
                        )
                )
            )
        # Start all threads in list
        for thread in self.threads:
            thread.start()

        # fall_through refers to waiting for open threads before returning
        if not fall_through:
            # waiting for all threads to complete
            for thread in self.threads:
                thread.join()

        # if the user wishes to write the analysis to a text file
        if write_file:
            # Deny fall through to ensure all data is saved
            for thread in self.threads:
                thread.join()
                # Write the file out
                # Avoid UnicodeEncodeError with WebScraped html using utf-8
                file1 = open(
                    "training_data.txt", "w", encoding='utf-8'
                    )
                # TODO: Also write the relevant source (paired with summary)
                file1.write(''.join(self.summaries))

    # Primary target of thread
    def scrape_and_summarize(self, url, search):
        try:
            print('Analyzing: ', url)
            # Append the generated summary to list
            self.summaries.append(
                Summarizer(
                    WebScraper(url).article_text, search, self.sl
                ).summary
            )
            # Append the respective link to list
            self.urls.append(url)
            # summaries and urls essentially have 'paired keys'
        except ValueError:
            print('Value Error')
        except TimeoutError:
            print('Timeout Error')
        except urllib.error.URLError:
            print('URL Error')
        except UnicodeError:
            print('Unicode Encode Error')
        except Exception:
            print('Exception not Anticipated')


class PinBucket:
    def __init__(self, title, author, link, summary):
        self.title = title
        self.author = author
        self.link = link
        self.summary = summary


class SearchQuery:
    pass


class NeuralSearch:
    pass

Analyst('TSLA', 10, 3, False, False)
