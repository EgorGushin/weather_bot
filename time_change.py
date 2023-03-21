import time


def utc_to_local_time(utc_time):
    hour = time.gmtime(utc_time + 10800).tm_hour
    if hour < 10:
        hour = f'0{hour}'
    minut = time.gmtime(utc_time + 10800).tm_min
    if minut < 10:
        minut = f'0{minut}'
    sec = time.gmtime(utc_time + 10800).tm_sec
    if sec < 10:
        sec = f'0{sec}'
    return f'{hour}ч. {minut}мин. {sec}сек.'
