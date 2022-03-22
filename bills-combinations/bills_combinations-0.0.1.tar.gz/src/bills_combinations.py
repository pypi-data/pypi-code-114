import itertools


def bills_combinations(bills_in_wallet, money_desired=100):
    bills_combination = []
    bills_options_count = 0
    for bills_quantity in range(1, len(bills_in_wallet) + 1):
        combinations = [list(combination) for combination in
                        itertools.combinations(bills_in_wallet, bills_quantity) if
                        sum(combination) == money_desired]
        for combination in combinations:
            if combination not in bills_combination:
                bills_combination.append(combination)
                bills_options_count += 1
    return f"there are {bills_options_count} combinations possible and they are {bills_combination}"


def main():
    bills_in_wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    print(bills_combinations(bills_in_wallet, 100))


if __name__ == "__main__":
    main()
