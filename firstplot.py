# import matplotlib.pyplot as plt
import numpy as np
import requests
response = requests.get("https://holidays.abstractapi.com/v1/?api_key=3e9f7a9fdbfe4adda2318bdf3f611928&country=US&year=2020&month=12&day=25")

# response = requests.get("https://holidays.abstractapi.com/v1/?api_key=3e9f7a9fdbfe4adda2318bdf3f611928&country=US&year=2020&month=12&day=25")
print(response.status_code)
print(response.content)

# https://holidays.abstractapi.com/v1/?api_key=3e9f7a9fdbfe4adda2318bdf3f611928&country=US&year=2020&month=12&day=25 api url
# print(api_key)
# https://app.abstractapi.com/api/holidays/documentation the api i am using
# https://docs.python.org/3/library/configparser.html config parser
# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()