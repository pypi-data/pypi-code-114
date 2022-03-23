from rich.table import Table
from rich.console import Console

class TablePrinter:

    def __init__(self):
        self._console = Console()

    def print_accounts(self, accounts):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column('Number')
        table.add_column('Name')
        table.add_column('Currency')
        table.add_column('Branch')
        table.add_column('Balance')
        for acc in accounts:
            table.add_row(
               str(acc.number), acc.name, acc.currency, acc.branch, str(acc.balance)
            )

        self._console.print(table)

    def print_movements(self, movements):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column('Date')
        table.add_column('Detail')
        table.add_column('Debit')
        table.add_column('Credit')
        table.add_column('Reference')
        for move in movements:
            table.add_row(
                str(move.date), move.detail, str(move.debit), str(move.credit), move.reference
            )

        self._console.print(table)


    def print_cards(self, cards):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column('Id')
        table.add_column('Balance USD')
        table.add_column('Balance Local')
        table.add_column('Due date')
        table.add_column('Name')
        table.add_column('Number')
        for card in cards:
            table.add_row(
                str(card.id), str(card.balance_dollar), str(card.balance_local),
                str(card.due_date), card.name, str(card.number)
            )

        self._console.print(table)


    def print_providers(self, providers):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column('Code')
        table.add_column('Country')
        table.add_column('Name')
        for provider in providers:
            table.add_row(
                provider.code, provider.country, provider.name
            )

        self._console.print(table)


