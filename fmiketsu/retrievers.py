from typing import List

from fmiopendata.wfs import download_stored_query
import pandas as pd
import datetime as dt

from fmiketsu.data_stuff import get_multipoint_headers, get_data_table_from_multipoint
from fmiketsu.time_stuff import from_to_fmi_times


def get_station_data(to_time: dt.datetime, hours_back: int, location: str, station: str) -> pd.DataFrame:
    """
    Retrieve dataframe of measurements from fmi api.
    :param to_time: end time
    :param hours_back: how many hours of data
    :param location: fmi api place
    :param station: fmi api station name in place
    :return: dataframe of measurements
    """
    from_time, to_time = from_to_fmi_times(to_time=to_time, hours_back=hours_back)
    multipoint = download_stored_query("fmi::observations::weather::multipointcoverage",
                                       args=[f"place={location}",
                                             f"starttime={from_time}",
                                             f"endtime={to_time}"])

    headers = get_multipoint_headers(multipoint=multipoint, station=station)
    rows = get_data_table_from_multipoint(multipoint=multipoint, station=station)
    return pd.DataFrame(rows, columns=headers)


def get_yearly_station_data(
        years: List[int],
        month: int,
        day: int,
        hour: int,
        hours_back: int,
        location: str,
        station: str) -> pd.DataFrame:
    """
    Retireve measurements form given date yearly.
    :param years: List of years
    :param month: data month
    :param day: data day
    :param hour: data hour
    :param hours_back: how many hours of data
    :param location: fmi api place
    :param station: fmi api station name in place
    :return: dataframe of measurements
    """
    frames = []
    for year in years:
        print(f'{year} ', end="")
        to_time = dt.datetime(year, month, day, hour, 0)
        df = get_station_data(to_time=to_time, hours_back=hours_back, location=location, station=station)
        frames.append(df)
    print("All done")
    return pd.concat(frames)
