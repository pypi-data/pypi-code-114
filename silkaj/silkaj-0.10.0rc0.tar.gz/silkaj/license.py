# Copyright  2016-2022 Maël Azimi <m.a@moul.re>
#
# Silkaj is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Silkaj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Silkaj. If not, see <https://www.gnu.org/licenses/>.

import webbrowser
from pathlib import Path
from typing import List

import click
import g1_monetary_license as gml

languages = ["es", "en", "eo", "fr", "pt"]

licenses_urls = {
    "en": "https://duniter.org/en/wiki/g1-license/",
    "fr": "https://duniter.fr/wiki/g1/licence-txt/",
}


def license_approval(currency: str) -> None:
    if currency != "g1":
        return
    if click.confirm(
        "You will be asked to approve Ğ1 license. Would you like to display it?"
    ):
        display_license()
    click.confirm("Do you approve Ğ1 license?", abort=True)


@click.command("license", help="Display Ğ1 monetary license")
def license_command() -> None:
    display_license()


@click.pass_context
def display_license(ctx) -> None:
    """
    Display in web browser if flag set and not headless system
    Otherwise, display in the terminal
    """
    if ctx.obj["G1_LICENSE_WEB"] and has_web_browser():
        languages_choices = list(licenses_urls.keys())
        language = language_prompt(languages_choices)
        webbrowser.open(licenses_urls[language])
    else:
        language = language_prompt(languages)
        path = license_path(language)
        with open(path) as license:
            click.echo_via_pager(license.read())


def has_web_browser() -> bool:
    try:
        webbrowser.get()
        return True
    except webbrowser.Error:
        return False


def language_prompt(languages_choices: List) -> str:
    return click.prompt(
        f"In which language would you like to display the Ğ1 monetary license?",
        type=click.Choice(languages_choices),
        show_choices=True,
        show_default=True,
        default="en",
    )


def license_path(lang: str) -> Path:
    path = gml.__path__.__dict__["_path"][0]  # type: ignore # mypy issue #1422
    return Path(path, f"g1_monetary_license_{lang}.rst")
