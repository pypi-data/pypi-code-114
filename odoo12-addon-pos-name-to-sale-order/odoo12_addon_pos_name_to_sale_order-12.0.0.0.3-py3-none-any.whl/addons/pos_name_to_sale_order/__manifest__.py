# Copyright 2021-Coopdevs Treball SCCL (<https://coopdevs.org>)
# - konykon - <kon.tsagari@coopdevs.org>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "PoS name to sale order",
    "version": "12.0.0.0.3",
    "depends": [
        "pos_order_to_sale_order",
        "pos_sale",
        "sale"
    ],
    "author": "Coopdevs Treball SCCL",
    "category": "Project Management",
    "website": "https://coopdevs.org",
    "license": "AGPL-3",
    "summary": """
        Group sale orders by Point of sale.
    """,
    "data": [
        "views/sale_order.xml",
        "views/sale_report.xml"
    ],
    "installable": True,
}
