from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from datetime import date
import json
import tkinter as tk
from tkinter import ttk


#Use Alpha Vantage API Key to access updated stock market data and metadata
ts = TimeSeries(key='5ZRUIOQ3NN7GYT1Z')

def display_table(tickers, table):
    stock_list = []
    #tickers = ['MSFT', 'AAPL', 'TSLA', 'PRPL', 'WM']
    for ticker in tickers:
        ticker_json_obj = json.loads(json.dumps(ts.get_daily(symbol=ticker)))
        ticker_latest_date = ticker_json_obj[1]["3. Last Refreshed"]

        ticker_info = []
        ticker_info.append(ticker)
        ticker_info.append(round(float(ticker_json_obj[0][ticker_latest_date]['1. open']), 2))
        ticker_info.append(round(float(ticker_json_obj[0][ticker_latest_date]['4. close']), 2))
        ticker_info.append(round(((float(ticker_json_obj[0][ticker_latest_date]['4. close']) - float(ticker_json_obj[0][ticker_latest_date]['1. open'])) / float(ticker_json_obj[0][ticker_latest_date]['1. open'])) * 100.0, 2))
        ticker_info.append(ticker_latest_date)
        stock_list.append(ticker_info)
    stock_list.sort(key=lambda e: e[1], reverse=True)

    for stock in stock_list:
        table.insert("", "end", values=stock)

def show_stocks(tickers):
    stocks = tk.Tk()

    label = tk.Label(stocks, text="Stock Watchlist", font=("Arial", 24)).grid(row=0, columnspan=5)

    cols = ('Ticker', 'Open', 'Close', 'Up/Down', 'Date')
    table = ttk.Treeview(stocks, columns=cols, show="headings")

    for col in cols:
        table.heading(col, text=col)

    table.grid(row=1, column=0, columnspan=2)

    loadStocks = tk.Button(stocks, text="Load Stocks", width=15, command= lambda: display_table(tickers, table)).grid(row=4, column=0)
    closeButton = tk.Button(stocks, text="Exit", width=15, command=exit).grid(row=4, column=1)

    stocks.mainloop()

def input_tickers():

    def generate_window(input_window, fields):
        for i in range(5):
            fields.append("Ticker {}: ".format(i+1))

        for field in fields:
            row = tk.Frame(input_window)
            label = tk.Label(row, width=15, text=field, anchor='w')
            ticker = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            label.pack(side=tk.LEFT)
            ticker.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            values.append((field, ticker))
        return values

    def fetch(values):
        for value in values:
            field = value[0]
            tickers.append(value[1].get())

    input_window = tk.Tk()
    fields = []
    values = []
    tickers = []

    values = generate_window(input_window, fields)
    input_window.bind('<Return>', (lambda event, e=values: fetch(e)))
    submit_button = tk.Button(input_window, text='Submit', command=(lambda e=values: fetch(e)))
    submit_button.pack(side=tk.LEFT, padx=5, pady=5)
    exit_button = tk.Button(input_window, text='Exit', command=input_window.quit)
    exit_button.pack(side=tk.LEFT, padx=5, pady=5)
    input_window.mainloop()

    return tickers

def main():
    #tickers = input_tickers()

    #placeholder input, trying to get input_tickers() to work
    tickers = ['MSFT', 'AAPL', 'WM', 'DIS', 'TSLA']
    show_stocks(tickers)


if __name__ == "__main__":
    main()
