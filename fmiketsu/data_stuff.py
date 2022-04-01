from typing import List

from fmiopendata.multipoint import MultiPoint


def get_multipoint_header(multipoint: MultiPoint, station: str) -> List[str]:
    headers = ["time"]
    for time_key in multipoint.data:
        for measure_key in multipoint.data[time_key][station]:
            headers.append(f'{measure_key}')
        return headers
    return headers


def get_data_table_from_multipoint(multipoint: MultiPoint, station: str):
    rows = []
    for time_key in multipoint.data:
        row = [time_key]
        for measure_key in multipoint.data[time_key][station]:
            row.append(multipoint.data[time_key][station][measure_key]["value"])
        rows.append(row)
    return rows
