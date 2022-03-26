import re
from typing import Generator

from kiraak.catalog import Product
from kiraak.config import FLAT_RE


class ParseFlatError(Exception):
    pass


class OrderProduct:
    def __init__(self, raw) -> None:
        self.sku = raw["sku"]
        self.line_id = raw["line_id"]
        self.name = raw["name"]
        self.qty = float(raw["qty"])
        self.price = float(raw["item_price"])
        self.mapping: Product | None = None

    def __str__(self) -> str:
        return self.name


class Order:
    def __init__(self, raw) -> None:
        self.order_num = raw["order_number"]
        self.status = raw["order_status"]
        self.date = raw["order_date"]
        self.note = raw["customer_note"]
        self.name = f'{raw["billing_first_name"]} {raw["billing_last_name"]}'
        self.flat = raw["billing_address"]
        res = re.match(FLAT_RE, raw["billing_address"])
        if not res:
            raise ParseFlatError(
                f"Could not parse flat from address {raw['billing_address']}"
            )
        self.flat = f'{res.group("block")}-{res.group("flat")}'
        self.phone = raw["billing_phone"]
        self.total = raw["order_subtotal"]
        self.prods: list[OrderProduct] = [OrderProduct(x) for x in raw["products"]]
        self.added = False

    def __str__(self) -> str:
        return self.name

    def __iter__(self) -> Generator[OrderProduct, None, None]:
        yield from self.prods


class OrderList:
    def __init__(self, raw) -> None:
        self.orders = [Order(x) for x in raw]
        self.all_products = [x for y in self.orders for x in y.prods]
        seen = set()
        self.unique_products = [
            seen.add(x.name) or x
            for y in self.orders
            for x in y.prods
            if x.name not in seen
        ]

    def __iter__(self) -> Generator[Order, None, None]:
        yield from self.orders

    def __len__(self) -> int:
        return len(self.orders)
