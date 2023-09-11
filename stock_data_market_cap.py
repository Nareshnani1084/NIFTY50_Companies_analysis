import pandas as pd
import yfinance as yf

# Load the list of stock symbols
stock_list = pd.read_csv("ind_nifty50list.csv")
stock_list = stock_list["Symbol"].to_list()
stock_list = [i+".NS" for i in stock_list]

data = yf.download(stock_list)
data.columns = pd.MultiIndex.from_tuples([i[::-1] for i in data.columns])

save_location = "stock_market"
combined_data = pd.DataFrame()

# Get Market Cap
market_caps = {}
for symbol in stock_list:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        market_cap = info.get('marketCap', None)
        market_caps[symbol] = market_cap
    except Exception as e:
        print(f"Unable to get market cap for {symbol}: {str(e)}")

    # Rest of your code to save data...
    try:
        TEMP = data[symbol].copy(deep=True)
        TEMP = TEMP.dropna()
        TEMP.to_csv(save_location+"/"+symbol+".csv")

        # Combine data into a single DataFrame with symbol
        TEMP['Symbol'] = symbol
        combined_data = pd.concat([combined_data, TEMP])
    except Exception as e:
        print(f"Unable to load data for {symbol}: {str(e)}")

# Save the combined data to a CSV file
combined_data.to_csv(save_location+"/combined_stock_data_market.csv", index=False)

# Print market caps
for symbol, market_cap in market_caps.items():
    print(f"{symbol}: {market_cap}")
