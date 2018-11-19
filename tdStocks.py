import csv
import matplotlib.pyplot as plt

prices = []
dates = []
i = 0.0

with open('td.csv') as file:
	reader = csv.DictReader(file)
	for row in reader:
		prices.append(row['Close'])
		dates.append(i)
		i += 1.0

plt.plot(dates, prices)
plt.title("TD Stocks over 1 month")
plt.xlabel("Days")
plt.grid()
plt.ylabel("Prices")
plt.show()

