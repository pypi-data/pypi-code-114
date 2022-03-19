import uuid

from property_price_register.models.sale import Sales
from property_price_register.utils import (
    download_zip,
    extract_zip
)


def main():

    fileuuid = uuid.uuid4()
    filename = f'/tmp/{fileuuid}.zip'

    download_zip(filename)
    extract_zip(filename)

    sales = Sales.load()

    all_data = Sales.from_file(f'/tmp/{fileuuid}/PPR-ALL.csv')

    for d in all_data:
        if not sales.contains(d):
            sales.append(d)

    sales.save('/tmp/ppr.csv')


if __name__ == '__main__':
    main()
