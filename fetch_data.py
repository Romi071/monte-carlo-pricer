import requests
import csv

response = requests.get("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=180")
data = response.json()
btcprices = []
for sublist in data:
    btcprices.append(float(sublist[4]))

with open("btc_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for price in btcprices:
        writer.writerow([price])