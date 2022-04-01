import datetime as dt
from typing import Tuple


def datetime_to_fmi(time: dt.datetime) -> str:
    return time.isoformat(timespec="seconds") + "Z"


def from_to_fmi_times(from_time: dt.datetime, hours_forward: int) -> Tuple[str, str]:
    to_time = from_time - dt.timedelta(hours=hours_forward)
    return datetime_to_fmi(from_time), datetime_to_fmi(to_time)
