import argparse
from collections import defaultdict

import matplotlib.pyplot as plt

from property_price_register.models.sale import Sales


def isnan(thing):
    return thing != thing


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--split-by',
        help='What to split by. Can be one of (blank (default), county, dublin_postal_code)',
        dest='split_by',
        default=None
    )
    parser.add_argument(
        '--filter',
        help='When splitting by county or postal code or whateber, filter the selected fields by comma separated values like --filter="Dublin,Carlow,Mayo"',
        dest='filter',
        default=None
    )
    args = parser.parse_args()

    sales = Sales.load()

    year_prices = defaultdict(Sales)
    for sale in sales:
        year_prices[sale.year].append(sale)

    if args.split_by is None:
        x = []
        y = []
        for year, year_sales in year_prices.items():
            x.append(year)
            y.append(year_sales.average_price)
        plt.plot(x, y, label='all')

        plt.legend(loc=2)
        plt.show()

    elif args.split_by == 'county':
        counties = set([s.county for s in sales])
        for county in counties:
            if args.filter is not None:
                if county not in args.filter.split(','):
                    continue
            x = []
            y = []
            for year, year_sales in year_prices.items():
                alt_sales = Sales()
                alt_sales.extend([s for s in year_sales if s.county == county])

                x.append(year)
                y.append(alt_sales.average_price)
            plt.plot(x, y, label=county)

        plt.legend(loc=2)
        plt.show()

    elif args.split_by == 'dublin_postal_codes':
        postal_codes = set([s.postal_code for s in sales if not isnan(s.postal_code)])
        for postal_code in postal_codes:
            if args.filter is not None:
                if postal_code not in args.filter.split(','):
                    continue
            x = []
            y = []
            for year, year_sales in year_prices.items():
                alt_sales = Sales()
                alt_sales.extend([s for s in year_sales if s.postal_code == postal_code])

                x.append(year)
                y.append(alt_sales.average_price)
            plt.plot(x, y, label=postal_code)

        plt.legend(loc=2)
        plt.show()
    else:
        print('nothing to do')


if __name__ == '__main__':
    main()
