import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv("Seattle2014.csv")
print(data.head())
rainfall = data["PRCP"].values
inches = rainfall/254
print(inches.shape)
seaborn.set()
plt.hist(inches, 40)
plt.show()

print("Number of days without rain: ", np.sum(inches == 0))
print("Number of days with rain: ", np.sum(inches != 0))
print("Number of days with rain more than 0.5 inches: ", np.sum(inches>0.5))
print("Number of days with rain < 0.2 inches: ", np.sum((inches > 0)& (inches < 0.2)))