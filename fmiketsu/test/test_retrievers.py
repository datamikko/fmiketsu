import unittest
import datetime as dt
from fmiketsu.retrievers import get_station_data, get_yearly_station_data
from fmiketsu.time_stuff import from_to_fmi_times


class TestCopy(unittest.TestCase):

    def test_get_station_data(self):
        df = get_station_data(
            to_time=dt.datetime.utcnow(),
            hours_back=10,
            location="Rovaniemi",
            station="Rovaniemi rautatieasema")

        print(df.info())
        self.assertEqual(df.shape[0] > 0, True)

    def test_get_yearly_station_data(self):
        df = get_yearly_station_data(years=[1999, 2015, 2020],
                                     month=2,
                                     day=1,
                                     hour=12,
                                     hours_back=24,
                                     location="Rovaniemi",
                                     station="Rovaniemi rautatieasema")
        print(df.info())
        self.assertEqual(df.shape[0] > 0, True)

    def test_get_yearly_station_data_another(self):
        df = get_yearly_station_data(years=[1960, 1986, 2020],
                                     month=2,
                                     day=1,
                                     hour=12,
                                     hours_back=1,
                                     location="apukka",
                                     station="Rovaniemi Apukka")
        print(df.info())
        self.assertEqual(df.shape[0] > 0, True)

    def test_from_to_fmi_times(self):
        from_time, to_time = from_to_fmi_times(to_time=dt.datetime(2000, 1, 2, 0, 0), hours_back=24)
        print(from_time, to_time)

        self.assertEqual(from_time, "2000-01-01T00:00:00Z")
