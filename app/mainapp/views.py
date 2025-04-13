import time
from django.shortcuts import render
import yfinance as yf


def stockPicker(request):
    nifty_50_tickers = [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS",
        "HINDUNILVR.NS",
        "SBIN.NS",
        "BAJFINANCE.NS",
        "ITC.NS",
        "CIPLA.NS",
    ]
    return render(
        request, "mainapp/stockpicker.html", {"stockpicker": nifty_50_tickers}
    )


def stockTracker(request):
    if request.method == "POST":
        ticker_symbols = request.POST.getlist("ticker_symbols")
    details = []
    start_time = time.time()
    for ticker_symbol in ticker_symbols:
        try:
            stock = yf.Ticker(ticker_symbol)
            info = stock.info

            # Historical data for calculating change
            hist = stock.history(period="2d")
            if len(hist) >= 2:
                prev_close = hist["Close"].iloc[-2]
                latest_close = hist["Close"].iloc[-1]
                change = latest_close - prev_close
                percent_change = (change / prev_close) * 100
            else:
                change = percent_change = None

            details.append(
                {
                    "Name": info.get("longName"),
                    "Current_Price": info.get("currentPrice"),
                    "Market_Cap": info.get("marketCap"),
                    "PE_Ratio": info.get("trailingPE"),
                    "Sector": info.get("sector"),
                    "Change": round(change, 2) if change else None,
                    "Percent_Change": f"{round(percent_change, 2)}%"
                    if percent_change
                    else None,
                }
            )

        except Exception as e:
            details.append(
                {
                    "Name": ticker_symbol,
                    "Error": str(e),
                }
            )
    end_time = time.time()  # End timer
    duration = round(end_time - start_time, 2)
    return render(
        request, "mainapp/stocktracker.html", {"details": details, "duration": duration}
    )
