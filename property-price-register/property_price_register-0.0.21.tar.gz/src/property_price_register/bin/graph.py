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
    parser.add_argument(
        '--include-all',
        help='To include the total set of data as one label along with whatever other filters were used',
        dest='include_all',
        action='store_true'
    )
    parser.add_argument(
        '--remove-outliers',
        help='Remove sales with a price under 75k and a price of over 10m',
        dest='remove_outliers',
        action='store_true'
    )
    args = parser.parse_args()

    sales = Sales.load()

    if args.remove_outliers:
        tmp = Sales()
        tmp.extend([s for s in sales if s.price > 75_000 and s.price < 10_000_000])
        sales = tmp

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
        if args.include_all:
            x = []
            y = []
            for year, year_sales in year_prices.items():
                x.append(year)
                y.append(year_sales.average_price)
            plt.plot(x, y, label='all')

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

        if args.include_all:
            x = []
            y = []
            for year, year_sales in year_prices.items():
                x.append(year)
                y.append(year_sales.average_price)
            plt.plot(x, y, label='all')

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
