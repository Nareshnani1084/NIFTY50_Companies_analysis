import pandas as pd
import yfinance as yf

# Load the list of Nifty 50 stock symbols
nifty_50_symbols = pd.read_csv("ind_nifty50list.csv")
nifty_50_symbols = nifty_50_symbols["Symbol"].to_list()
nifty_50_symbols = [i+".NS" for i in nifty_50_symbols]

# Initialize dictionaries to store ratios
pb_ratios = {}
debt_ratios = {}

# Get P/B ratio and Debt Ratio for each stock
for symbol in nifty_50_symbols:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        pb_ratio = info.get('priceToBook', None)
        debt_ratio = info.get('debtToEquity', None)
        pb_ratios[symbol] = pb_ratio
        debt_ratios[symbol] = debt_ratio
    except Exception as e:
        print(f"Unable to get ratios for {symbol}: {str(e)}")

# Create DataFrames for P/B ratio and Debt Ratio
pb_ratio_df = pd.DataFrame(list(pb_ratios.items()), columns=['Symbol', 'PriceToBook'])
debt_ratio_df = pd.DataFrame(list(debt_ratios.items()), columns=['Symbol', 'DebtToEquity'])

# Save the P/B ratio and Debt Ratio data to separate CSV files
pb_ratio_df.to_csv("pb_ratio_data.csv", index=False)
debt_ratio_df.to_csv("debt_ratio_data.csv", index=False)
