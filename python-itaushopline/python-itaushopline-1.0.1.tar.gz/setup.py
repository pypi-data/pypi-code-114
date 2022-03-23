from setuptools import setup

setup(
    name = 'python-itaushopline',
    version = '1.0.1',
    author = 'MrPowerUp',
    author_email = 'gustavohenrique8282@hotmail.com',
    packages = ['itaushopline'],
    description = 'Lib para consultas e pagamentos via Itaú Shopline.',
    long_description = 'Lib (Classe) para gerar a DC com objetivo de realizar consultas e pagamentos via Itaú Shopline.',
    url = 'https://github.com/MrPowerUp82/python_itaushopline',
    project_urls = {
        'Código fonte': 'https://github.com/MrPowerUp82/python_itaushopline',
    },
    license = 'MIT',
    keywords = 'API ItaúShopline Itaú',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=['lxml==4.8.0','requests==2.27.1']
)