"""Module that assembles all the scraping functions into a functional scraper."""

import asyncpraw, asyncio, json, pathlib
from typing import Union
from rich.console import Console
from prisma import errors
from .s_database import Database
from .s_parsers import Exceptions
from .s_scraper import Scraper
from .s_periodic import Periodic
from .s_models import PostModel


__all__ = ["scrape", "scrape_multiple_subreddits"]
here = pathlib.Path(__file__).parent
console = Console()
stats = {"scraped": 0, "successful": 0, "failed": 0, "duplicate": 0}
database = Database()
with open(here.parent / "config.json", "r", encoding="utf-8") as f:
    config = json.load(f)


def printStatistics():
    """Prints statistics."""
    print("\n")
    console.rule("Statistics")
    console.log(
        f"Scraped: {stats['scraped']}\nSuccessful: {stats['successful']}\nFailed: {stats['failed']}\nDuplicate: {stats['duplicate']}"
    )
    console.rule()
    print("\n")


async def scrape(subreddit: str, search_type: str):
    """Scrapes a subreddit."""
    reddit = asyncpraw.Reddit(
        client_id=config["client_id"],
        client_secret=config["client_secret"],
        user_agent="Subreddit Scraper 0.1.0 - TheOnlyWayUp",
    )
    scraper = Scraper()
    subreddit = await reddit.subreddit(subreddit)
    await subreddit.load()
    console.log("[green][L][/green] - Connected to database.")
    console.rule(
        f"Scraping Started: {subreddit.display_name} - {search_type.capitalize()}"
    )
    async for postTuple in scraper.scrape(
        subreddit, search_type, database, char_limit=config["minimum_character_limit"]
    ):
        stats["scraped"] += 1

        first: Union[PostModel, Exceptions.PostException] = postTuple[0]
        post_id: str = postTuple[1]
        post_url: str = postTuple[2]

        if isinstance(first, Exceptions.PostException):
            if isinstance(first, Exceptions.Duplicate):
                stats["duplicate"] += 1
                console.log(
                    f"[yellow][Dd][/yellow] {subreddit.display_name} - {post_id} - {post_url}"
                )
                continue
            stats["failed"] += 1
            console.log(
                f"[yellow][F][/yellow] {subreddit.display_name} - {first} - {post_url}"
            )
            continue

        try:
            await database.add(first)
            stats["successful"] += 1
        except errors.UniqueViolationError:
            stats["duplicate"] += 1
            console.log(
                f"[yellow][Du][/yellow] {subreddit.display_name} - {post_id} - {post_url}"
            )
            continue

        console.log(
            f"[green][+][/green] {subreddit.display_name} {post_id} - {post_url} - {first.post['replies']}"
        )
    console.rule("Scraping Complete")
    return


async def scrape_multiple_subreddits(subreddits: list, search_types: list):
    """Scrapes multiple subreddits.
    Warning: Possibly high CPU usage. Average 20% increase, unsure how to optimize.
    """
    toGather = []
    p = Periodic(printStatistics, 10)
    await p.start()
    await database.connect()
    for subreddit in subreddits:
        for searchType in search_types:
            toGather.append(scrape(subreddit, searchType))
    await asyncio.gather(*toGather)
    await database.disconnect()
    await p.stop()

subreddits = config["subreddits"]
config = config["search_types"]

async def run_scraper():
    """Runs the scraper."""
    try:
        asyncio.run(
            scrape_multiple_subreddits(
                subreddits=config["subreddits"],
                search_types=config["search_types"],
            )
        )
    except BaseException as e:
        printStatistics()
        asyncio.run(database.disconnect())
        raise e
