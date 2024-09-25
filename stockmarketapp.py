import streamlit as st

import yfinance as yf
import datetime

ticker_symbol = st.text_input("Enter the stock name", "Life of Brian")

start_date = st.date_input('start_date', value=datetime.date(2020, 11, 5))
end_date = st.date_input('end_date', value=datetime.date(2023, 12, 5))
data = yf.download(ticker_symbol, start=start_date, end=end_date)
st.write(data)
st.line_chart(data['Close'])