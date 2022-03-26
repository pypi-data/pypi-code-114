"""Handles adding orders to kiraak"""
import logging

from click import confirm
from rich.table import Table

from kiraak import console
from kiraak.api import add_order, get_current_order
from kiraak.catalog import Catalog
from kiraak.mapping import Mapping
from kiraak.order import OrderList

logger = logging.getLogger(__name__)


def add_orders(orders: OrderList, catalog: Catalog):
    """Adds the provided orders"""
    mapping = Mapping(orders, catalog)
    mapping.initialize_mapping()
    mapping.confirm()

    for order in orders:
        logger.info(f"Adding order of {order.name} @ {order.flat}:")
        tbl = Table(
            "Product", "Quantity", "Catalog Name", "Catalog Desc", "Catalog Size"
        )
        for prod in order.prods:
            if not prod.mapping:
                logger.error(
                    f"Product {prod.name} x {str(prod.qty)} not found in catalog, skipping!"
                )
                tbl.add_row(
                    prod.name,
                    str(prod.qty),
                    "N/A",
                    "N/A",
                    "N/A",
                    style="default on red",
                )
                continue
            tbl.add_row(
                prod.name,
                str(prod.qty),
                prod.mapping.name,
                prod.mapping.desc,
                prod.mapping.quantity,
            )
        console.print(tbl)
        if confirm(f"Confirm order of {order.name} @ {order.flat}?"):
            final_order = {
                "name": order.name,
                "flat": order.flat,
                "total": sum([p.price * p.qty for p in order if p.mapping]),
                "products": [
                    {
                        "cat": p.mapping,
                        "amt": p.qty,
                        "price": p.price,
                        "total": p.qty * p.price,
                    }
                    for p in order
                    if p.mapping
                ],
            }
            if not all([x["cat"].price == x["price"] for x in final_order["products"]]):
                logger.error("Mismatch of prices! Please check the order and prices!")
                logger.error("Skipping...")
                continue
            add_order(final_order, catalog.id, order)
        else:
            logger.error("Order not added! Reason: Cancelled")

    return orders
