import asyncio
from .pururin import get_pur
from .nhentai import get_nh
from .simplyh import get_sim
from .hentaifox import get_hfox
from .hentai2read import get_h2r
from .utils.misc import choose


class Tomoe():
    def __init__(self,
                 Pururin: str = choose().pururin,
                 Nhentai: str = choose().nhentai,
                 Simplyhentai: str = choose().simply,
                 Haentaifox: str = choose().hentaifox,
                 Hentai2read: str = choose().hentai2read):

        self.pururin = Pururin
        self.nhentai = Nhentai
        self.simply = Simplyhentai
        self.hentaifox = Haentaifox
        self.hentai2read = Hentai2read


Api = Tomoe()


def main():
    async def main_pururin():
        await asyncio.gather(get_pur(Api.pururin))

    async def main_nhentai():
        await asyncio.gather(get_nh(Api.nhentai))

    async def main_simply():
        await asyncio.gather(get_sim(Api.simply))

    async def main_hentaifox():
        await asyncio.gather(get_hfox(Api.hentaifox))

    async def main_hentai2read():
        await asyncio.gather(get_h2r(Api.hentai2read))

    if Api.pururin is not None:
        asyncio.run(main_pururin())

    elif Api.nhentai is not None:
        asyncio.run(main_nhentai())

    elif Api.simply is not None:
        asyncio.run(main_simply())

    elif Api.hentaifox is not None:
        asyncio.run(main_hentaifox())

    elif Api.hentai2read is not None:
        asyncio.run(main_hentai2read())

    else:
        print("No arguments was given")


if __name__ == '__main__':
    main()
