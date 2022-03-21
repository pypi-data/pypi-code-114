from setuptools import setup


setup(
    name = 'BridgeCo',
    version = '0.0.1',
    author = 'Guilherme Silva dos Santos',
    author_email = 'guilherme.santos@bridgeconsulting.com.br',
    packages = ['BridgeCo'],
    description = 'Permite criar work itens no projeto Bridge Technology.',
    long_description = 'Desenvolvido para automatizar a criação de work itens em planejamentos de sprints.',
    license = 'MIT',
    keywords = 'Bridge BridgeCO Azure AzureDevops WorkItens',
    install_requires= [
        'anyio>=3.5.0',
        'certifi>=2021.10.8',
        'charset-normalizer>=2.0.12',
        'h11>=0.12.0',
        'httpcore>=0.14.7',
        'httpx>=0.22.0',
        'idna>=3.3',
        'python-dateutil>=2.8.2',
        'rfc3986>=1.5.0',
        'six>=1.16.0',
        'sniffio>=1.2.0']
)