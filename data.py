import holidays
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

# create holiday list

holiday_list = [] #initialize empty list
for yrs in range(2009,2023):
    for item in holidays.UnitedStates(years=yrs).items():
        holiday_list.append(item)
    for item in holidays.UnitedKingdom(years=yrs).items():
        holiday_list.append(item)
    for item in holidays.France(years=yrs).items():
        holiday_list.append(item)


# create a data frame from holiday list
df = pd.DataFrame(holiday_list)

# save dataframe to csv file
df.to_csv('/Users/albamolina/files/python_final/ex1_holidays.csv')
