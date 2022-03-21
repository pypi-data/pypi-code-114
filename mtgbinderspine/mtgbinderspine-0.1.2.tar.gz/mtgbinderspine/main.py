import io
import logging
import pathlib
import time
from typing import List

import click
import requests
from cairosvg import svg2png
from diskcache import FanoutCache
from PIL import Image, ImageDraw, ImageFont
from requests.exceptions import HTTPError
from rich.logging import RichHandler
from rich.progress import Progress
from svglib.svglib import svg2rlg

logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")

cache = FanoutCache()


@cache.memoize()
def _get_scryfall(path: str):
    response = requests.get(f"https://api.scryfall.com/{path}")
    response.raise_for_status()

    time.sleep(0.1)
    return response


def get_set_image(set_three_letter_code: str):
    """
    Downloads the set svg from scryfall

    The scryfall api docs request that we don't make more than 10 requests per second.
    """
    try:
        set_info = _get_scryfall(f"sets/{set_three_letter_code}").json()
    except HTTPError as e:
        if e.response.status_code == 404:
            return None

    icon_uri = set_info["icon_svg_uri"]

    icon_resp = requests.get(icon_uri)
    icon_resp.raise_for_status()

    return icon_resp.content


def get_set_name(set_three_letter_code: str):
    set_info = _get_scryfall(f"sets/{set_three_letter_code}").json()

    return set_info["name"]


def render_spine(
    set_three_letter_code: str,
    length_in=10.5,
    width_in=1,
    dpi: int = 600,
    font_size=350,
):
    """
    Renders the card spine as a Pillow Image
    """

    width = int(length_in * dpi)

    height = int(width_in * dpi)

    # Draw Set Icon
    set_icon_margin = 0.1

    set_image = get_set_image(set_three_letter_code)

    if not set_image:
        raise ValueError(f"Set {set_three_letter_code} not found")

    svg_bytesio = io.BytesIO(set_image)

    raw_image = io.BytesIO()

    rlg = svg2rlg(svg_bytesio)

    svg2png_scale = ((width_in - set_icon_margin * 2) / rlg.height) * dpi

    svg2png(
        file_obj=svg_bytesio,
        write_to=raw_image,
        background_color="transparent",
        scale=svg2png_scale,
    )

    pil_icon = Image.open(raw_image).convert("RGBA")

    # Create the spine image
    im = Image.new(size=(width, height), mode="RGBA")

    icon_area_width = max(int(dpi * 2.5), pil_icon.width)

    # Paste the set icon in on the left side
    im.alpha_composite(
        pil_icon, ((icon_area_width - pil_icon.width) // 2, int(set_icon_margin * dpi))
    )

    # Draw the set name
    draw = ImageDraw.Draw(im)

    default_font_path = (
        pathlib.Path(__file__).parent.parent / "fonts" / "Beleren2016-Bold.ttf"
    )

    font = ImageFont.truetype(str(default_font_path), size=font_size)

    set_name = get_set_name(set_three_letter_code)

    text_size = draw.textsize(set_name, font)

    x_offset = icon_area_width

    draw.text(
        (x_offset + (width - x_offset - text_size[0]) / 2, (height - text_size[1]) / 2),
        set_name,
        fill=(0, 0, 0, 255),
        font=font,
    )

    return im


@click.command()
@click.argument("set_code", type=str, nargs=-1)
@click.option("--dpi", type=int, default=600, help="The dpi of the output image")
@click.option(
    "-o",
    "--output",
    type=click.Path(exists=False, file_okay=True, dir_okay=False),
    help="The output file (if not provided, will make a directory called renders in current directory)",
)
@click.option(
    "-l",
    "--length",
    type=float,
    default=10.5,
    help="The length of each spine, in inches (the width of the output image)",
)
@click.option(
    "-w",
    "--width",
    type=float,
    default=1,
    help="The width of each spine, in inches (the height of the output image)",
)
@click.option(
    "--border-thickness",
    "_border_thickness",
    type=int,
    default=3,
    help="The thickness of the border between each spine, in pixels",
)
@click.option(
    "--border-color",
    "_border_color",
    type=int,
    default=160,
    help="The color of the border between each spine, in grayscale (int 0-255)",
)
@click.option(
    "--font-size",
    "_font_size",
    type=int,
    default=350,
    help="The size of the font used to render the set name, in points",
)
def render_spine_command(
    set_code: List[str],
    output: str,
    dpi: int,
    length: float,
    width: float,
    _border_thickness: int,
    _border_color: int,
    _font_size: int,
):
    log.info("Starting render")

    ims = []

    with Progress() as progress:
        for code in progress.track(set_code):
            ims.append(
                render_spine(
                    code,
                    length_in=length,
                    width_in=width,
                    dpi=dpi,
                    font_size=_font_size,
                )
            )

    log.info("Rendering full image...")
    # Stack images
    im = Image.new(size=(ims[0].width, 1 + (ims[0].height + 1) * len(ims)), mode="RGBA")
    for i, sub_im in enumerate(ims):
        im.paste(sub_im, (0, 1 + i * (ims[0].height + 1)))

    # Draw separating lines
    draw = ImageDraw.Draw(im)

    for i in range(0, len(ims) + 1):
        y = i * (ims[0].height + 1)
        # Draw the line
        line_greyness = _border_color
        draw.line(
            (0, y, ims[0].width, y),
            fill=(line_greyness, line_greyness, line_greyness, 255),
            width=_border_thickness,
        )

    if output is None:
        filename = "_".join(set_code) + ".png"

        parent_folder = pathlib.Path("renders/")
        parent_folder.mkdir(parents=True, exist_ok=True)

        output = str(parent_folder / filename)

    log.info("Saving...")
    im.save(output, dpi=(dpi, dpi))

    log.info("Complete!")


if __name__ == "__main__":
    render_spine_command()
