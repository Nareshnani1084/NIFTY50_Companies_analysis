import pandas as pd
import yfinance as yf

# Load the list of Nifty 50 stock symbols
nifty_50_symbols = pd.read_csv("ind_nifty50list.csv")
nifty_50_symbols = nifty_50_symbols["Symbol"].to_list()
nifty_50_symbols = [i+".NS" for i in nifty_50_symbols]

# Initialize a dictionary to store P/E ratios
pe_ratios = {}

# Get P/E ratio for each stock
for symbol in nifty_50_symbols:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        pe_ratio = info.get('trailingPE', None)
        pe_ratios[symbol] = pe_ratio
    except Exception as e:
        print(f"Unable to get P/E ratio for {symbol}: {str(e)}")

# Create a DataFrame from the P/E ratio data
pe_ratio_df = pd.DataFrame(list(pe_ratios.items()), columns=['Symbol', 'PriceToEarnings'])

# Save the P/E ratio data to a CSV file
pe_ratio_df.to_csv("pe_ratio_data.csv", index=False)
