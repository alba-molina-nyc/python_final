import matplotlib.pyplot as plt
import numpy as np
import configparser, os

config = configparser.ConfigParser()
config.read_file(open('.gitignore'))
api = config.api_key

url = 'https://api.adoptapet.com/search/pets_at_shelter?key=A34F48&v=1&output=xml&shelter_id=2342'




# https://app.abstractapi.com/api/holidays/documentation

# print(api)



# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()