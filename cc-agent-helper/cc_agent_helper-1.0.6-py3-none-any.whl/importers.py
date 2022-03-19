import logging

from itertools import chain, islice

from pymongo import MongoClient
import pymongo.errors

from . import settings

LOG = logging.getLogger(__name__)


def import_win_lose(data):
    if settings.WIN_LOSE_MONGODB_URL:
        with MongoClient(settings.WIN_LOSE_MONGODB_URL) as connection:
            db = connection.bookmaker
            db.win_lose.replace_one({'uuid': data.get('uuid')}, data, upsert=True)
    else:
        LOG.info(data)
    return data.get('username')


def chunks(iterable, size=10):
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))


def ticket_filter(x):
    # check sport type
    if x.get('sport') not in ['football', 'soccer']:
        return False
    #
    # # reject virtual sport
    # home_team = x.get('home_team', '')
    #
    # # sbobet virtual
    # if home_team.startswith('e-'):
    #     return False
    #
    # # ibet pingoal
    # if '(pg)' in home_team:
    #     return False
    #
    # # ibet virtual
    # if '(v)' in home_team:
    #     return False

    return True


def import_ticket(ticket_iterator, username, from_date, to_date):
    total_tickets = 0
    ticket_filtered = filter(ticket_filter, ticket_iterator)
    with MongoClient(settings.TICKET_MONGODB_URL) as connection:
        for tickets in chunks(ticket_filtered, 100):
            collector = [dict(ticket, _id=ticket.get('uuid')) for ticket in tickets]
            total_tickets += len(collector)
            if settings.TICKET_MONGODB_URL:
                try:
                    connection.bookmaker.tickets.insert_many(collector, ordered=False)
                except pymongo.errors.BulkWriteError:
                    pass
            LOG.info('{} Processed {} tickets'.format(username, total_tickets))
        uuid = '__'.join([username, from_date, to_date])
        summary = {
            '_id': uuid,
            'count': total_tickets,
            'username': username,
            'from_date': from_date,
            'to_date': to_date
        }

        connection.bookmaker.account_ticket_count.replace_one({'_id': uuid}, summary, upsert=True)

        return summary
