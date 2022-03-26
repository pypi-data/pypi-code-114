import logging
import sys
import typing as t

from click import confirm
from rich.table import Table

from kiraak import console
from kiraak.catalog import Catalog, Product
from kiraak.difflib import get_close_matches
from kiraak.order import OrderList

logger = logging.getLogger(__name__)


class Mapping:
    def __init__(self, orderlist: OrderList, catalog: Catalog) -> None:
        self.map: t.Dict[str, Product] = {}
        self.orders = orderlist
        self.catalog = catalog

    def match(self, prod, conf=True):
        """Gets the closest match to a product
        Note: Now redundant"""
        close_matches = get_close_matches(prod, self.catalog, len(self.catalog), 0)
        if not conf:
            return close_matches[0]
        if not close_matches:
            logger.error(f"Product {prod} not found in catalog!")
            sys.exit(1)
        for res in close_matches:
            logger.info(
                f"Matching [bold]{prod}[/] -> [bold]{res}[/]",
                extra={"markup": True},
            )
            if (
                inp := input("Continue? ([Y]es/[n]o/[q]uit/[s]kip/[name]) ").lower()
            ) == "n":
                continue
            if inp in ["y", ""]:
                return res
            if inp == "s":
                return None
            if inp == "name":
                return self.match(input("Enter name of product: "))
            logger.error("Skipping...")

    def initialize_mapping(self) -> None:
        for oproduct in self.orders.all_products:
            if not oproduct.mapping:
                oproduct.mapping = self.catalog.find_by_id(oproduct.sku)
        if not all([x.mapping for x in self.orders.all_products]):
            logger.error(
                f"Products {','.join([x.name for x in self.orders.all_products if not x.mapping])} not found in catalog, skipping products!"
            )
        if not all(
            [x.mapping.price == x.price for x in self.orders.all_products if x.mapping]
        ):
            logger.error(
                f"Products {','.join([x.name for x in self.orders.all_products if x.mapping.price != x.price])} do not have matching prices!"
            )
            sys.exit(1)

    def confirm(self) -> None:
        while True:
            tbl = Table(
                "Number",
                "Order Product",
                "Catalog Product",
                "Catalog Description",
                "Catalog Size",
            )
            for i, order_prod in enumerate(self.orders.unique_products):
                if not order_prod.mapping:
                    logger.error(
                        f"Product {order_prod.name} not found in catalog, skipping in all orders!"
                    )
                    continue
                tbl.add_row(
                    str(i),
                    order_prod.name,
                    order_prod.mapping.name,
                    order_prod.mapping.desc,
                    order_prod.mapping.quantity,
                )

            console.print(tbl)
            if confirm("Edit mapping?", default=True):
                while True:
                    num = int(input("Enter number of product to edit: "))
                    product = list(self.map.keys())[num]
                    self.map[product] = self.match(product)
                    if not confirm("Continue editing?", default=True):
                        break
            else:
                break

    def __getitem__(self, key) -> Product:
        return self.map[key]
