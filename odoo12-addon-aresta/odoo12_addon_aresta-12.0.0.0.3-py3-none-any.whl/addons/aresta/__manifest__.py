{
    "name": "Odoo customizations for Aresta",
    "version": "12.0.0.0.3",
    "depends": [
        "delivery",
        "pos_order_to_sale_order",
        "pos_sale",
        "sale"
    ],
    "author": "Coopdevs Treball SCCL",
    "category": "Project Management",
    "website": "https://coopdevs.org",
    "license": "AGPL-3",
    "summary": """
        Odoo customizations for Aresta.
    """,
    "data": [
        "views/sale_order.xml",
        "views/sale_report.xml",
        "report/stock_report_deliveryslip.xml",
    ],
    "installable": True,
}
