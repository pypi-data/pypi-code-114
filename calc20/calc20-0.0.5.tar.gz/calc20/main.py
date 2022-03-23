#!/usr/bin/env python
# encoding: utf-8

import random
from openpyxl import Workbook


def generate_expression():
    """Generate minuend and subtrahend."""
    minuend = random.randrange(10, 20)
    subtrahend = random.randrange(minuend % 10, minuend)

    return (minuend, subtrahend)


def save_into_file(expressions):
    """Save expressions into XLS file."""
    workbook = Workbook()
    dest_filename = '运算题.xlsx'

    workbook.properties.title = "20以内数字减法"
    workbook.properties.creator = "Yarving Liu"
    workbook.properties.category = "Math"
    workbook.properties.description = "60道20以内数字减法运算题"
    workbook.properties.identifier = "substration_expression"
    workbook.properties.subject = "20以内数字减法"
    workbook.properties.subject = "20以内数字减法"


    sheet = workbook.active
    sheet.title = "运算题"

    for row in range(1, 21):
        for col in range(1, 4):
            index = 3 * (row - 1) + col - 1
            minuend, subtrahend = expressions[index]
            sheet.cell(row=row, column=col, value=f"{minuend} - {subtrahend} = ")

    workbook.save(filename = dest_filename)



def main():
    """Get 60 different subsctraction expression."""
    expressions = []
    for _ in range(60):
        expression = generate_expression()
        if expression in expressions:
            expression = generate_expression()

        expressions.append(expression)

    save_into_file(expressions)



if __name__ == "__main__":
    main()
