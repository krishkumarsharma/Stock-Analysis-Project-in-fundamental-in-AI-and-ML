# stock analysis project using Twelve Data API
# final version with colored trend graph (red/green)

import requests
import matplotlib.pyplot as plt
import pandas as pd

# ---------------- API SETUP ----------------
API_KEY = "01b91260996f48268f6d14098e51d5b1"

stock = input("Enter stock symbol (AAPL or INFY.NS): ").upper().strip()

if stock == "":
    print("❌ Enter valid stock")
    exit()

# API call
url = "https://api.twelvedata.com/time_series"
params = {
    "symbol": stock,
    "interval": "1day",
    "outputsize": 180,
    "apikey": API_KEY
}

print("\nFetching data...")
res = requests.get(url, params=params)
data = res.json()

if "values" not in data:
    print("❌ API Error:")
    print(data)

else:
    print("\n--- STOCK ANALYSIS ---")

    prices = []
    dates = []

    for entry in data["values"]:
        prices.append(float(entry["close"]))
        dates.append(entry["datetime"])

    prices.reverse()
    dates.reverse()

    # BASIC INFO
    latest = prices[-1]
    first = prices[0]

    print("Latest:", round(latest,2))
    print("Start:", round(first,2))
    print("High:", round(max(prices),2))
    print("Low:", round(min(prices),2))

    # TREND
    print("\nTrend:")
    if latest > first:
        print("UPTREND 📈")
    else:
        print("DOWNTREND 📉")

    # MOVING AVG
    sma = sum(prices[-10:]) / 10
    print("10-Day Avg:", round(sma,2))

    # SUGGESTION
    print("\nSuggestion:")
    if latest > sma:
        print("BUY 🟢")
    else:
        print("SELL 🔴")

    # DATAFRAME
    df = pd.DataFrame({"Date": dates, "Price": prices})
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    monthly = df.groupby("Month")["Price"].mean()

    months = monthly.index.astype(str)
    values = monthly.values

    # ---------------- GRAPH ----------------
    print("\nShowing advanced trend graph...")

    plt.figure(figsize=(11,6))

    # colored trend line
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            plt.plot(months[i-1:i+1], values[i-1:i+1], color='green')
        else:
            plt.plot(months[i-1:i+1], values[i-1:i+1], color='red')

    # markers
    plt.scatter(months, values)

    # BUY/SELL labels
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            plt.text(i, values[i], "BUY ↑", fontsize=8, color='green')
        else:
            plt.text(i, values[i], "SELL ↓", fontsize=8, color='red')

    # fill area (light effect)
    plt.fill_between(months, values, alpha=0.1)

    # titles
    plt.title("Stock Trend Analysis (6 Months) - " + stock, fontsize=14)
    plt.xlabel("Month")
    plt.ylabel("Average Price")

    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()