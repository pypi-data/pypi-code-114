import csv

import yaml

with open("config.yaml") as file:
    all_codes = yaml.safe_load(file)

with open("codes.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    for key, value in all_codes.items():
        writer.writerow([key, value])
