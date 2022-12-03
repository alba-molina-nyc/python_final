import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import data


x = [country for country in data.north_america]
print(x)
y = [] #number of holidays
 
# This will plot a simple bar chart
plt.bar(x, y)
  
# Title to the plot
plt.title("Bar Chart")
  
# Adding the legends
plt.legend(["bar"])
plt.show()