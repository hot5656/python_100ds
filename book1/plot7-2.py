import matplotlib.pyplot as plt
import numpy as np

# Generating some random data (e.g., normal distribution)
data = np.random.normal(loc=0, scale=1, size=1000)

# Creating a histogram with density=True
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue', edgecolor='black')

# Adding labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Random Data')

# Displaying the plot
plt.show()