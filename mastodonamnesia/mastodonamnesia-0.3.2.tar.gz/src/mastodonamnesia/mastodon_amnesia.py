"""
    MastodonAmnesia - deletes old Mastodon toots
    Copyright (C) 2021  Mark S Burgunder

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import argparse
import time
from math import ceil
from typing import Any
from typing import cast
from typing import Dict

import arrow
from mastodon import MastodonRatelimitError
from rich import traceback

from mastodonamnesia import __version__
from mastodonamnesia.control import Configuration

traceback.install(show_locals=True)


def main() -> None:
    """Main logic to run MastodonAmnesia."""

    parser = argparse.ArgumentParser(description="Delete old toots.")
    parser.add_argument(
        "-c", "--config-file", action="store", default="config.json", dest="config_file"
    )
    args = parser.parse_args()

    config = Configuration(config_file_name=args.config_file)

    logger = config.bot.logger
    mastodon = config.mastodon_config.mastodon

    now = arrow.now()
    oldest_to_keep = now.shift(seconds=-config.bot.delete_after)

    logger.info("Welcome to MastodonAmnesia (%s)", __version__)
    logger.info(
        "We are removing toots older than %s from %s@%s",
        oldest_to_keep,
        config.mastodon_config.base_url,
        config.mastodon_config.user_info.user_name,
    )

    max_toot_id, toots = skip_recent_toots(config, oldest_to_keep)

    # Delete toots
    toots_deleted = 0
    while True:
        if len(toots) == 0:
            break

        for toot in toots:
            if should_keep(toot, config):
                logger.info(
                    "Not deleting toot. Bookmarked: %s - Faved: %s - Pinned %s",
                    toot.get("bookmarked"),
                    toot.get("favourited"),
                    toot.get("pinned"),
                )
                continue

            try:
                toot_created_at = arrow.get(cast(int, toot.get("created_at")))
                logger.debug(
                    "Oldest to keep vs toot created at %s > %s (%s)",
                    oldest_to_keep,
                    toot_created_at,
                    bool(oldest_to_keep > toot_created_at),
                )

                if toot_created_at < oldest_to_keep:
                    mastodon.status_delete(toot.get("id"))
                    logger.info(
                        "Deleted toot %s from %s", toot.get("url"), toot_created_at
                    )
                    toots_deleted += 1

            except MastodonRatelimitError:
                need_to_wait = ceil(
                    mastodon.ratelimit_reset - mastodon.ratelimit_lastcall
                )
                logger.info("Deleted a total of %s toots", toots_deleted)
                logger.info(
                    'Need to wait %s seconds (until %s) to let server "cool down"',
                    need_to_wait,
                    arrow.get(mastodon.ratelimit_reset),
                )
                time.sleep(need_to_wait)

        # Get More toots
        toots = mastodon.account_statuses(
            id=config.mastodon_config.user_info.account_id,
            limit=10,
            max_id=max_toot_id,
        )

    logger.info("All old toots deleted! Total of %s toots deleted", toots_deleted)


def skip_recent_toots(
    config: Configuration, oldest_to_keep: arrow.Arrow
) -> tuple[int, list[dict[str, Any]]]:
    """Method to skip over toots that should not yet be deleted.

    :param config: Configuration object for MastodonAmnesia
    :param oldest_to_keep: arrow object of date of oldest toot we want to keep
    :return: tuple consisting of that toot id of the oldest toot to keep and
    List of toots
    """
    logger = config.bot.logger
    mastodon = config.mastodon_config.mastodon
    toots = mastodon.account_statuses(
        id=config.mastodon_config.user_info.account_id, limit=10
    )
    max_toot_id = toots[-1].get("id") if len(toots) > 0 else None
    # Find first toot that needs to be deleted
    logger.info("Finding first toot old enough to delete.")
    while True:
        if len(toots) == 0:
            break

        last_toot_created_at = arrow.get(toots[-1].get("created_at"))
        logger.debug("Oldest toot in this batch is from %s", last_toot_created_at)
        if last_toot_created_at < oldest_to_keep:
            break

        try:
            toots = mastodon.account_statuses(
                id=config.mastodon_config.user_info.account_id,
                limit=10,
                max_id=max_toot_id,
            )
            max_toot_id = toots[-1].get("id") if len(toots) > 0 else None

        except MastodonRatelimitError:
            need_to_wait = ceil(mastodon.ratelimit_reset - mastodon.ratelimit_lastcall)
            logger.info(
                'Need to wait %s seconds (until %s) to let server "cool down"',
                need_to_wait,
                arrow.get(mastodon.ratelimit_reset),
            )
            time.sleep(need_to_wait)
    return max_toot_id, toots


def should_keep(toot: Dict[str, Any], config: Configuration) -> bool:
    """Function to determine if toot should be kept even though it might be a
    candidate for deletion."""
    keeping = False
    if config.bot.skip_deleting_bookmarked:
        keeping = bool(toot.get("bookmarked"))
    if config.bot.skip_deleting_faved:
        keeping = bool(toot.get("favourited"))
    if config.bot.skip_deleting_pinned:
        keeping = bool(toot.get("pinned"))
    return keeping


# run main programs
if __name__ == "__main__":
    main()
