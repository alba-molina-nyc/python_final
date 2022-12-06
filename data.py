import holidays
import matplotlib.pyplot as plt
import numpy as np
from datetime import date


countries = holidays.utils.list_supported_countries()
for country in countries:
    if country == 'US':
        print('country: ', country )
        print(type(country))
        print(type(countries))
        print(type(holidays.US()))
# print('here: ', all_countries)


# US Holidays - 2021
for day in sorted(holidays.US(years=2023).items()):
    print(day)

