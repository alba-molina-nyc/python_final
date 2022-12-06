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


# US Holidays - 2021 - CA
for day, name in sorted(holidays.US(years=2023, state='CA').items()):
    print(day, name)


# check if public holiday or not
us_holidays = holidays.UnitedStates()
uk_holidays = holidays.UnitedKingdom()
fr_holidays = holidays.France()
print('01-01-2022' in us_holidays)
print('01-01-2022' in uk_holidays)
print('01-01-2022' in fr_holidays)

for country in countries:
    countries.country
    # print(type(country), 'country-type')