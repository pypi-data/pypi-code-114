import logging
import time

import click
from rich.table import Table
from woocommerce import API

from kiraak import console
from kiraak.api import get_catalog, login
from kiraak.catalog import Catalog
from kiraak.config import Auth

wcapi = API(
    url="https://rgbsocial.redgreenbluemix.com/",
    consumer_key=Auth.WOOCOMMERCE_CONSUMER_KEY,
    consumer_secret=Auth.WOOCOMMERCE_CONSUMER_SECRET,
    wp_api=True,
    version="wc/v3",
)


logger = logging.getLogger(__name__)

logger.info(f"Logging in as {Auth.MOBILE}")
partner_info = login(Auth.MOBILE, Auth.PASSWORD)
logger.info(
    f"Logged in as {partner_info['partnerName']} @ {partner_info['partnerBrand']}"
)


class WC_Product:
    pass


class WC_Products:
    def __init__(raw_json: dict) -> None:
        pass


def compare():
    # Get and print catalog
    logger.info("Fetching catalog...")
    catalog = Catalog(get_catalog())
    logger.info(f"Recieved catalog (id {catalog.id})")

    prods = []
    i = 1
    while new_prods := wcapi.get("products", json={"page": i, "per_page": 20}).json():
        i += 1
        prods.extend(new_prods)
    print(prods)
    print(len(prods))


@click.command()
@click.option("--loop", is_flag=True)
@click.argument("time-gap", default=300, type=int)
def main(loop, time_gap):
    compare()
    while loop:
        time.sleep(time_gap)
        compare()


if __name__ == "__main__":
    main()
