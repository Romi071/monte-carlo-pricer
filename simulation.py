import csv
import numpy as np

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

#Initial cond
s0 = prices_arr[-1]
iterations = 10000
t_intervals = 30
dt = 1/365

#Z matrix for our random normal distribution
Z_mat = np.random.normal(0, 1)
