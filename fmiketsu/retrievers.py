from typing import List

from fmiopendata.wfs import download_stored_query
import pandas as pd
import datetime as dt

from fmiketsu.data_stuff import get_multipoint_header, get_data_table_from_multipoint
from fmiketsu.time_stuff import from_to_fmi_times


def get_station_data(from_time: dt.datetime, hours_forward: int, location: str, station: str) -> pd.DataFrame:
    from_time, to_time = from_to_fmi_times(from_time=from_time, hours_forward=hours_forward)
    multipoint = download_stored_query("fmi::observations::weather::multipointcoverage",
                                       args=[f"place={location}",
                                             f"starttime={to_time}",
                                             f"endtime={from_time}"])
    print(type(multipoint))
    headers = get_multipoint_header(multipoint=multipoint, station=station)
    print(headers)
    rows = get_data_table_from_multipoint(multipoint=multipoint, station=station)
    print(rows[0])
    return pd.DataFrame(rows, columns=headers)


def get_yearly_station_data(years: List[int], month: int, day: int, hour: int, hours_forward: int, location: str, station: str) -> pd.DataFrame:
    frames = []
    for year in years:
        from_time = dt.datetime(year, month, day, hour, 0)
        df = get_station_data(from_time=from_time, hours_forward=hours_forward, location=location, station=station)
        frames.append(df)

    return pd.concat(frames)
