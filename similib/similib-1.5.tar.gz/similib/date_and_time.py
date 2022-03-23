import time
import datetime
import pytz


def get_cur_date():
    return datetime.datetime.now(pytz.timezone('PRC')).strftime("%Y-%m-%d")


def get_cur_datetime():
    return datetime.datetime.now(pytz.timezone('PRC')).strftime("%Y-%m-%d %H:%M:%S")


def ns_timestamp_to_datetime(timestamp):
    try:
        return str(datetime.datetime.fromtimestamp(int(timestamp / 1000)))
    except Exception:
        return ""


def timestamp_to_datetime(timestamp):
    try:
        return str(datetime.datetime.fromtimestamp(int(timestamp)))
    except Exception:
        return ""


def datetime_to_timestamp(dt):
    if not dt:
        return
    try:
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = int(time.mktime(timeArray))
        return timestamp
    except Exception:
        pass

def datetime_to_format(time_string,entry_format,output_format):
    try:
        timeArray = time.strptime(time_string,entry_format)
        t  = time.strftime(output_format,timeArray)
        return t
    except Exception:
        return time_string



def datetime_to_datetimezone(dt,zone="00:00"):
    if not dt:
        return
    try:
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # 转换时区格式
        zone_time = time.strftime("%Y-%m-%dT%H:%M:%S+{}".format(zone),timeArray)
        return zone_time
    except Exception:
        pass

if __name__ == '__main__':
    pass