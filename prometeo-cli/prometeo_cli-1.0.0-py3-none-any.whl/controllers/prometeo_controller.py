import os
import typer
import prometeo

from getpass import getpass
from datetime import datetime

from client.prometeo_client import PrometeoClient
from helpers import SessionHandler, Profiler
from exceptions import ProviderNotFound

session = SessionHandler()

class PrometeoActionsController():

    def __init__(self):
        self._profiler = Profiler()
        self._environment = os.environ.get('PROMETEO_ENVIRONMENT')

        if self._environment is None:
            raise typer.Exit('Please set PROMETEO_ENVIRONMENT')

        api_key = self._profiler.get_configuration(self._environment)

        self._client = PrometeoClient(api_key, self._environment)

    def login(self, provider: str, interactive = False) -> None:
        passphrase = typer.prompt('Please enter your passphrase', hide_input=True, confirmation_prompt=True)

        try:
            if session.exists_session():
                confirm = typer.confirm('You have a session stored, want to login in a new one?')

                if confirm == False:
                    raise typer.Exit('Session already started')

                session.end_session()

            if interactive:
                provider = typer.prompt('Provider')
                username = typer.prompt('Username')
                password = getpass()
            else:
                username, password = self._profiler.get_credentials(provider, passphrase)

            session_key = self._client.login(provider, username, password)
            session.create_session(session_key)

        except (prometeo.exceptions.WrongCredentialsError, KeyError) as e:
            raise typer.Exit('Wrong credentials')

        except prometeo.exceptions.UnauthorizedError as e:
            print(e)
            raise typer.Exit('Unknown provider')
        except ProviderNotFound as e:
            raise typer.Exit('Configuration for the given provider not found')



    def logout(self) -> None:
        try:
            banking_session = self._client.banking.get_session(
                    session.retrieve_session()
            )
            banking_session.logout()
            session.end_session()

        except FileNotFoundError as e:
            raise typer.Exit('Session already terminated')


    def get_accounts(self) -> list:
        try:
            banking_session = self._client.banking.get_session(
                    session.retrieve_session()
            )
            return banking_session.get_accounts()

        except prometeo.exceptions.InvalidSessionKeyError as e:
            session.end_session()
            raise typer.Exit('Invalid session please login again')

        except FileNotFoundError as e:
            raise typer.Exit('Session already terminated')


    def get_account_movements(self, account, start_date, end_date):
        accounts = self.get_accounts()
        try:
            account = next(acc for acc in accounts if acc.number == account)
        except StopIteration:
            raise typer.Exit('Account not found')
        return account.get_movements(start_date, end_date)


    def get_cards(self):
        banking_session = self._client.banking.get_session(
                session.retrieve_session()
        )
        return banking_session.get_credit_cards()


    def get_card_movements(self, card_id, start_date, end_date, currency):
        try:

            cards = self.get_cards()
            card = next(ca for ca in cards if ca.id == card_id)
        except StopIteration:
            raise typer.Exit('Card not found')
        return card.get_movements(currency, start_date, end_date)


    def get_providers(self):
        banking = self._client.banking
        return banking.get_providers()
