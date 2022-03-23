import typer

from helpers import Crypto, Profiler

class ConfigurationController():

    def __init__(self):
        pass


    def add_new_credential(self):
        provider = typer.prompt('Plese enter the provider id for the new configuration')
        username = typer.prompt('Please enter the username')
        password = typer.prompt('Please enter the password', hide_input=True, confirmation_prompt=True)

        typer.echo('\nDO NOT FORGET YOUR PASSPHRASE, IT WILL BE REQUIRED AT THE LOGIN STEP TO VALIDATE YOU IDENTITY')
        typer.echo('EACH CONFIGURATION MAY HAVE DIFFERENT PASSPHRASES\n')

        passphrase = typer.prompt('Please enter your passphrase', hide_input=True, confirmation_prompt=True)
        crypto = Crypto()
        encrypted_pass = crypto.encrypt(password, passphrase)

        profiler = Profiler()
        profiler.add_new_credential(provider, username, encrypted_pass.decode())


    def add_new_environment(self):
        environment = typer.prompt('Please enter the environment')
        api_key = typer.prompt('Please enter the api_key')
        profiler = Profiler()
        profiler.add_new_environment(environment, api_key)
