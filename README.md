# Monte Carlo BTC Asset Pricer

A Monte Carlo asset pricer in Python. Fetches historical Binance market data to calculate annualized drift and volatility, and simulates thousands of future Bitcoin price paths using Geometric Brownian Motion (GBM).

## Key Features & Mathematics

*   **Live Data Pipeline:** Directly queries the Binance public API for the last 180 days of daily Bitcoin closing prices, bypassing the need for manual CSV downloads.
*   **Statistical Extraction:** Dynamically calculates daily log returns, computing the annualized drift (μ) and annualized historical volatility (σ) based on a 365-day trading year.
*   **Stochastic Modeling:** Uses Geometric Brownian Motion to simulate 10,000 potential future price paths over a 30-day horizon. The simulation relies on the discrete-time GBM solution: S_t = S_{t-1} * exp((μ - σ²/2)dt + σ√dt Z)
*   **Probability Analysis:** Aggregates all 10,000 simulated outcomes to calculate the exact statistical probability of the asset finishing higher than its starting price, alongside the expected monetary net change.
*   **Data Visualization:** Leverages Matplotlib to plot 100 sample random walk paths and generates a histogram of the final day-30 price distribution.

---

## Installation & Setup

1. **Clone or Download the Repository:**
   Save the two Python scripts to your local project directory.

2. **Install Required Dependencies:**
   Run the following command in your terminal to install the necessary mathematical, charting, and network libraries:
   
   pip install requests numpy matplotlib

## Usage & Outputs

Because the project is split into data collection and simulation, you must run the scripts sequentially.

**Step 1: Fetch the Data**
Run the data extraction script to ping Binance and create your historical dataset.

python data_fetcher.py

*This will generate a btc_data.csv file in your directory containing the last 180 daily closing prices.*

**Step 2: Run the Simulation**
Execute the Monte Carlo script to analyze the CSV and simulate the price paths.

python monte_carlo.py

**Expected Outputs:**
*   **Terminal:** Prints the annualized drift, the probability of the asset yielding a positive return over the next 30 days, and the average expected net balance.
*   **Visuals:** Opens a line chart showing a sample of 100 simulated price paths, followed by a histogram showing the normal distribution of the 10,000 final simulated prices.
