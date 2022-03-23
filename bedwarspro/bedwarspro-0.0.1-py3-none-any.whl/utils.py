from datetime import timezone, datetime


def get_rank(raw):
    """Return the rank of the player."""
    display_rank = None

    prefix = raw.get('prefix')
    rank = raw.get('rank')
    playerRank = raw.get('playerRank')

    if prefix:
        return prefix
    elif rank:
        return rank.replace('_', ' ')
    else:
        return playerRank.replace('_', ' ')


UTC = timezone.utc


def _add_tzinfo(dt, tzinfo=UTC) -> datetime:
    return dt.replace(tzinfo=tzinfo)


def convert_to_datetime(decimal, add_tzinfo=True) -> datetime:
    seconds = decimal / 1e3
    dt = datetime.fromtimestamp(seconds)
    if add_tzinfo:
        return _add_tzinfo(dt)
    return dt
