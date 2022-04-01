import datetime as dt
from typing import Tuple


def datetime_to_fmi(time: dt.datetime) -> str:
    """
    Format datetime for fmi api request
    :param time: datetime
    :return: time string
    """
    return time.isoformat(timespec="seconds") + "Z"


def from_to_fmi_times(to_time: dt.datetime, hours_back: int) -> Tuple[str, str]:
    """
    Get two string dates from given datetime and given hours back
    :param to_time: start point
    :param hours_back: timestamp in past from given to_time
    :return: tuple of str timestamps
    """
    from_time = to_time - dt.timedelta(hours=hours_back)
    return datetime_to_fmi(from_time), datetime_to_fmi(to_time)
