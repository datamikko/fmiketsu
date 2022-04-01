
# FMIKETSU

Python library to offer functions that use fmiopendata -python library.

Two main functions in retriever:

 * **get_station_data** to get table of data from given time and some hours back
 * **get_yearly_station_data** to get station data on specific day from given list of years 
Both return pandas dataframe of measurements.

## Install

Use pip to install or upgrade to newest version:

```bash
pip install git+https://github.com/datamikko/fmiketsu.git@main --upgrade
```

## Example

```python
from fmiketsu.retrievers import get_yearly_station_data
df = get_yearly_station_data(years=[1999, 2015, 2020],
                             month=2,
                             day=1,
                             hour=12,
                             hours_back=24,
                             location="Rovaniemi",
                             station="Rovaniemi rautatieasema")
print(df.info())
```