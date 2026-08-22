import csv
import numpy as np
import matplotlib.pyplot as plt

prices = []

with open("btc_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        prices.append(float(row[0]))

prices_arr = np.array(prices)
#Turn it into log(S_n / S_n-1)
log_prices = np.log(prices_arr[1:] / prices_arr[:-1])
#Get the statisticals
mean = 365*np.mean(log_prices)
std = (365**0.5)*np.std(log_prices)

print(mean)

#Initial cond
s0 = prices_arr[-1]
iterations = 10000
t_intervals = 30
dt = 1/365

#Z matrix for our random normal distribution
Z_mat = np.random.normal(0, 1, (t_intervals, iterations))

#Simulated prices
sim = np.zeros((31, 10000))
sim[0, :] = s0

#GBM equation looped over 30 days
for i in range(1, t_intervals + 1):
    sim[i, :] = sim[i-1, :]*np.exp((mean - 0.5*std**2)*dt + std*dt**0.5*Z_mat[i-1, :])

#Probability the asset ends higher than it started:
sim_bool = sim[-1, :] > s0 
wins = sim_bool.sum()
avgwin_amount = sim[-1, :].mean() - s0
win_prob = 100 * wins / iterations
print(f"There is a {win_prob}% chance that the asset ends higher than it started after 30 days")
print(f"There average net balance after 30 days is {avgwin_amount:.2f}$")

#Sim complete, now plot it:
plot_data = sim[:, 0:100]
histogram_data = sim[-1, :]

plt.plot(plot_data)
plt.figure()
plt.hist(histogram_data)

plt.show()