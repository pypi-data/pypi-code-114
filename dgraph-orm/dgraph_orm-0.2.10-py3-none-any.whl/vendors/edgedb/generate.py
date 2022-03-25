import typing as T
import asyncio
from pathlib import Path

from dgraph_orm.vendors.edgedb.generator import generate


async def main():
    await generate(
        config_path=Path("graphorm_config.json"),
        output_path=Path(__file__).parent / "gen",
    )


if __name__ == "__main__":
    asyncio.run(main())
