import argparse
import sys

from .lang import process_article
from .scraper import get_theguardian_articles, parse_theguardian_article, NoContentException, historical_news_api

DEFAULT_COUNTRY = "us"
DEFAULT_YEAR = 1950


def select_article(articles):
    while True:
        for i, article in enumerate(articles, start=1):
            print(i, article.title)
        try:
            input_ = input("Chose an article number: ")
            if input_[0].lower() == "q":
                print("Bye")
                break
            article_number = int(input_) - 1
        except ValueError:
            print("Please select a number")
            continue

        try:
            article = articles[article_number]
        except IndexError:
            print("Please select a valid article")
            continue

        return article.url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', required=True)
    parser.add_argument('-c', '--country', required=False, default=DEFAULT_COUNTRY)
    parser.add_argument("-e", "--endyear", type=int, default=DEFAULT_YEAR,
                        help='Check the history up until this year')
    args = parser.parse_args()
    articles = get_theguardian_articles(args.search)
    url = select_article(articles)
    print(url)
    try:
        article_text = parse_theguardian_article(url)
    except NoContentException as exc:
        print(exc)
        sys.exit(1)
    print(article_text)
    related_articles = [
        art.lead_paragraph for art in
        historical_news_api(args.search)
    ]

    print("Original article:")
    print(article_text)
    print(f"- {len(related_articles)} related articles found")

    sims = process_article(article_text, related_articles)

    print("Similar articles:")
    for i, similarity in sims:
        print(f"{similarity} -> {related_articles[i]}\n")
    print("---\n")


if __name__ == "__main__":
    main()
