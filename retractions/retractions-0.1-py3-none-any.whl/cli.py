import asyncio
import logging
import sys
import typing as tp
from argparse import ArgumentParser
from pathlib import Path
from urllib.request import Request

import httpx

from .backends import UpdateType, registry
from .doi import DOI

logger = logging.getLogger(__name__)


def path_or_pipe(s: str) -> tp.Optional[Path]:
    if s == "-":
        return None
    return Path(s).resolve()


def read_dois(p: tp.Optional[Path]) -> tp.Iterator[DOI]:
    if p is None:
        for line in sys.stdin:
            yield DOI.parse(line)
    else:
        with open(p) as f:
            for line in f:
                yield DOI.parse(line)


async def fetch(reqs: tp.List[Request]) -> tp.List[tp.Optional[bytes]]:
    contents = dict()
    async with httpx.AsyncClient() as client:

        async def get(idx, req: Request):
            got = await client.request(
                req.get_method(),
                req.full_url,
                headers=dict(req.headers),
                # todo: handle POST request data
            )
            return idx, got

        for coro in asyncio.as_completed(get(idx, url) for idx, url in enumerate(reqs)):
            idx, r = await coro
            if r.status_code == 404:
                contents[idx] = None
                continue
            r.raise_for_status()
            contents[idx] = r.content

    return [contents[k] for k in sorted(contents)]


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument(
        "doi",
        nargs="*",
        help="DOI to check for retractions or updates. Handled after --infile lists.",
    )
    parser.add_argument(
        "-r",
        "--retractions-only",
        action="store_true",
        help="Only list retracted DOIs, not updated",
    )
    backends = sorted(registry)
    parser.add_argument("-b", "--backend", choices=backends, default="openretractions")
    parser.add_argument(
        "-i",
        "--infile",
        type=path_or_pipe,
        action="append",
        help="Get DOIs from file (newline-separated); accepts multiple",
    )
    parser.add_argument(
        "-o", "--outfile", type=path_or_pipe, help="Write to file instead of stdout"
    )
    parser.add_argument("-u", "--url", action="store_true", help="Show DOIs as URLs")

    parsed = parser.parse_args(args)
    backend = registry[parsed.backend]

    def fmt_doi(doi: DOI):
        if parsed.url:
            return doi.to_url()
        else:
            doi.to_str()

    requests = []
    if parsed.infile:
        for infile in parsed.infile:
            requests.extend(backend.make_request(d) for d in read_dois(infile))
    requests.extend(backend.make_request(d) for d in parsed.doi)

    response_contents = asyncio.run(fetch(requests))
    rows = []
    for content in response_contents:
        if content is None:
            continue
        update = backend.parse_content(content)
        if update is None:
            continue
        row = [update.type.value]
        row.append(fmt_doi(update.original_doi))

        if not update.type == UpdateType.RETRACTION:
            if parsed.retractions_only:
                continue

            row.append(fmt_doi(update.update_doi) if update.update_doi else "")
            row.append(update.timestamp.isoformat() if update.timestamp else "")

        rows.append("\t".join(row))

    if parsed.outfile:
        with open(parsed.outfile, "w") as f:
            for row in rows:
                f.write(row + "\n")
    else:
        for row in rows:
            print(row)
