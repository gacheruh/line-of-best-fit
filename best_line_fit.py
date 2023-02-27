import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



file_location = "kenya-climate-data-1991-2016-temp-degress-celcius.csv"
repeated_years = np.loadtxt(file_location, dtype = float, usecols =0, skiprows =1, delimiter =",")
monthly_temp = np.loadtxt(file_location, dtype = float, usecols =2, skiprows =1, delimiter =",")

# Edit data to yearly records
n = 0
temp = 0
years = []
average_temps = []

for data in monthly_temp:
    # Counting years
    if n%12 == 0:
        years.append(int(repeated_years[n]))
        if n != 0:
            temp = temp / 12
            average_temps.append(temp)
            temp = 0
    # Counting moths
    temp += monthly_temp[n]
    n += 1
    if n == len(repeated_years):
        temp = temp / 12
        average_temps.append(temp)

# Plotting the graph
plot_one = plt.plot(years, average_temps, ".")

# Drawing the line of best fit
def line(m, x, c):
    return m*x + c

# Find optimal values for 'm' and 'c'
optimal, __ = curve_fit(line, years, average_temps)
m, c = optimal
print("Optimal line function is.... y = %.3f*x + %.3f" %( m, c))

# Redrawing the plot
x_values = np.arange(min(years), max(years), 1)
y_values = line(m, x_values, c)
# The final line
plot_two = plt.plot(years, average_temps, ".", color = "blue")
best_line = plt.plot(x_values, y_values, "--", color = "red")
plt.show()
