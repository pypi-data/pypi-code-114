import re
from typing import Generator

from hypersquirrel.scraperfactory import get_scraper
from hypersquirrel.watchlist import Watchlist, PagedWatchlist
from hypersquirrel.watchlist.decorator import maxitems

PAGED_PATTERN = re.compile("<\d+-\d+>")


def _create_watchlist(url: str):
    match = PAGED_PATTERN.findall(url)
    if len(match) == 1:
        pages = match[0].replace("<", "").replace(">", "").split("-")
        return PagedWatchlist({
            "url": url.replace(match[0], "${page}"),
            "page_min": int(pages[0]),
            "page_max": int(pages[1])
        })
    return Watchlist({
        "url": url
    })


def scrape(url: str) -> Generator[dict, None, None]:
    w = _create_watchlist(url)
    w.decorate(maxitems.decorator)
    return scrape_watchlist(w)


def scrape_watchlist(w: Watchlist) -> Generator[dict, None, None]:
    scraper = get_scraper(w)
    return w.scrape(scraper)
