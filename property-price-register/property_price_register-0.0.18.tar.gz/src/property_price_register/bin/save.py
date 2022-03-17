from property_price_register.models.sale import Sales


def main():

    sales = Sales.load()

    # Remove long lines, can always get them back when we merge with latest if we want. This can come from bad encodings
    sales._data = [s for s in sales._data if len(str(s.serialize())) < 2000]

    sales.save('/tmp/ppr.csv')

    import pdb; pdb.set_trace()

    pass


if __name__ == '__main__':
    main()
