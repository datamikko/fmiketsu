from typing import List, Any

from fmiopendata.multipoint import MultiPoint


def get_multipoint_headers(multipoint: MultiPoint, station: str) -> List[str]:
    """
    Get column names from response data
    :param multipoint: fmi data
    :param station: station name
    :return: column names
    """
    headers = ["time"]
    for time_key in multipoint.data:
        for measure_key in multipoint.data[time_key][station]:
            headers.append(f'{measure_key}')
        return headers
    return headers


def get_data_table_from_multipoint(multipoint: MultiPoint, station: str) -> List[List[Any]]:
    """
    Get list of rows from fmi dictionary.
    Row list is values from each measurement
    :param multipoint: fmi data
    :param station: station name
    :return: list of rows
    """
    rows = []
    for time_key in multipoint.data:
        row = [time_key]
        for measure_key in multipoint.data[time_key][station]:
            row.append(multipoint.data[time_key][station][measure_key]["value"])
        rows.append(row)
    return rows
