#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/03/18 16:24:06.894459
#+ Editado:	2022/03/18 17:56:31.382793
# ------------------------------------------------------------------------------
from typing import Union, List, Optional
import json
import requests

from .excepcions import ErroTipado
from .cmc_uteis import lazy_check_types

from conexions import Proxy
# ------------------------------------------------------------------------------
class CoinMarketCap:
    __MAX_CANT_MOEDAS: int = 1000000

    __lig_cmc: str = 'https://coinmarketcap.com'
    __lig_top: str = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start={}&limit={}&sortBy=market_cap&sortType=desc&convert={}&cryptoType=all&tagType=all&audited=false'
    __verbose: bool
    __proxied: bool
    __timeout: int
    __reintentos: int

    # constructor --------------------------------------------------------------
    def __init__(self, verbose: bool = False, proxied: bool = False, timeout: int = 10, reintentos: int = 5) -> None:
        self.__verbose = verbose
        self.__proxied = proxied
        self.__timeout = timeout
        self.__reintentos = reintentos

        if proxied:
            self.__r = Proxy(verbose= verbose)
            self.__r.set_timeout(timeout)
            self.__r.set_reintentos(reintentos)
        else:
            self.__r = requests
    # --------------------------------------------------------------------------

    # getters ------------------------------------------------------------------
    # MAX_CANT_MOEDAS
    def get_max_cant_moedas(self) -> int:
        return self.__MAX_CANT_MOEDAS

    # __lig_cmc
    def get_lig_cmc(self) -> str:
        return self.__lig_cmc

    # __lig_top
    def get_lig_top(self, inicio: int, topx: int, moedas: Union[str, List[str]]) -> str:
        return self.__lig_top.format(inicio, topx, moedas)

    # verbose
    def get_verbose(self) -> bool:
        return self.__verbose

    # proxied
    def get_proxied(self) -> bool:
        return self.__proxied

    # timeout
    def get_timeout(self) -> int:
        return self.__timeout

    # reintentos
    def get_reintentos(self) -> int:
        return self.__reintentos
    # --------------------------------------------------------------------------

    # setters ------------------------------------------------------------------
    # MAX_CANT_MOEDAS
    def set_max_cant_moedas(self, novo_max_cant_moedas) -> None:
        self.MAX_CANT_MOEDAS = novo_max_cant_moedas

    # verbose
    def set_verbose(self, novo_verbose: bool) -> None:
        self.__verbose = novo_verbose
        if self.get_proxied(): self.r.set_verbose(novo_verbose)

    # proxied
    def set_proxied(self, novo_proxied: bool) -> None:
        self.__proxied= novo_proxied

    # timeout
    def set_timeout(self, novo_timeout: int) -> None:
        self.__timeout= novo_timeout
        if self.get_proxied(): self.r.set_timeout(novo_timeout)

    # reintentos
    def set_reintentos(self, novo_reintentos: int) -> None:
        self.__reintentos= novo_reintentos
        if self.get_reintentos(): self.r.set_timeout(novo_reintentos)
    # --------------------------------------------------------------------------

    # funcions -----------------------------------------------------------------
    def crudo(self, moedas: Union[str, List[str]] = 'usd') -> List[dict]:
        """
        """

        # se mete mal o tipo dos valores saca erro
        if not lazy_check_types(moedas, str):
            raise ErroTipado('Os tipos das variables non entran dentro do esperado')

        return json.loads(self.__r.get(self.get_lig_top(1, self.get_max_cant_moedas(), moedas)).text)

    def top(self, moedas: Union[str, List[str]] = 'usd', inicio: Optional[int] = 1, topx: Optional[int] = 10) -> List[dict]:
        """
        Fai uso do endpoint:
        https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1000&sortBy=market_cap&sortType=desc&convert=USD,EUR,BTC,ETH,XMR&cryptoType=all&tagType=all&audited=false
        """

        # se mete mal o tipo dos valores saca erro
        if not lazy_check_types([inicio, topx, moedas], [int, int, str]):
            raise ErroTipado('Os tipos das variables non entran dentro do esperado')

        if inicio <= 0:
            inicio = 1

        if topx < 0:
            topx = 10
        elif topx == 0:
            topx = self.get_max_cant_moedas()

        moedas = moedas.replace(' ','')
        if type(moedas) == list:
            moedas = ','.join(moedas)

        while True:
            json_devolto = json.loads(self.__r.get(self.get_lig_top(inicio, topx, moedas)).text)

            if json_devolto['status']['error_code'] == '0':
                break

        lista_top = []
        for monero in json_devolto['data']['cryptoCurrencyList']:
            lista_top.append({
                'posicion': monero['cmcRank'],
                'simbolo': monero['symbol'],
                'nome': monero['name'],
                'prezo': [f"{ele['price']} {ele['name']}" for ele in monero['quotes']],
                'ligazon': self.get_lig_cmc()+f'/currencies/{monero["slug"]}/'
                })

        return lista_top
    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------
