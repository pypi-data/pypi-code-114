import itertools
from types import SimpleNamespace


class Watchlist(SimpleNamespace):
    def __init__(self, config: dict):
        super(Watchlist, self).__init__(**config)

    def decorate(self, decorator):
        decorator(self)

    def validate(self, validator):
        validator(self)

    def scrape(self, scraper, url=None):
        gen = scraper(url or self.url)
        yield from itertools.islice(gen, self.max_items)


class PagedWatchlist(Watchlist):
    def get_paged_scrape_generator(self, scraper):
        for page in range(self.page_min, self.page_max + 1):
            url = self.url.replace("${page}", str(page))
            yield from super().scrape(scraper, url)

    def scrape(self, scraper):
        gen = self.get_paged_scrape_generator(scraper)
        yield from itertools.islice(gen, self.max_items)
