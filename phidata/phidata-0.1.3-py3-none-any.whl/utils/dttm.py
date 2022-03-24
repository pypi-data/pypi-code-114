import datetime


def get_today_utc_date_str() -> str:
    today = datetime.datetime.now(datetime.timezone.utc).date()
    return today.strftime("%Y_%m_%d")
