# import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import date
import holidays

north_america = holidays.CA() + holidays.US() + holidays.MX()
print('north_america: ', north_america)


# holidays.HolidayBase(years=[], expand=True, observed=True, prov=None, state=None)