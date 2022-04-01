import unittest
import datetime as dt
from fmiketsu.retrievers import get_station_data, get_yearly_station_data


class TestCopy(unittest.TestCase):

    def test_get_station_data(self):
        df = get_station_data(
            from_time=dt.datetime.utcnow(),
            hours_forward=10,
            location="Rovaniemi",
            station="Rovaniemi rautatieasema")

        print(df)

    def test_get_yearly_station_data(self):
        df = get_yearly_station_data(years=[1999, 2020],
                                     month=2,
                                     day=1,
                                     hour=12,
                                     hours_forward=2,
                                     location="Rovaniemi",
                                     station="Rovaniemi rautatieasema")
        print(df)
