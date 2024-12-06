import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit as st

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: pink;
    }
    [data-testid="stAppViewContainer"] {
        background-color: lightblue;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Stock Data Viewer")

ticker = st.sidebar.text_input("Select Ticker Symbol", "AARVI.NS")
period = st.sidebar.selectbox("Select Period", ["1d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"])
Parameter = st.sidebar.selectbox("Select Parameter", ["Open","Close","High","Low","Volume"])


dataf = yf.download(ticker, period=period)

mydict = {'1d':'Todays','1mo':'1 Month','3mo':'3 Months','6mo':'6 Months','1y':'1 Year','2y':'2 Years','5y':'5 Years'}
getperiod = mydict.get(period)

st.write(f"## Analysis for {ticker} - for Period: {getperiod}")
st.write(dataf)

chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

if not dataf.empty:
    dataf.reset_index(inplace=True)

    if chart_type == "Line Chart":
        st.write("### Line Chart")
        st.line_chart(dataf[[Parameter]])

    elif chart_type == "Bar Chart":
        st.write("### Bar Chart")
        st.bar_chart(dataf[[Parameter]])

    elif chart_type == "Area Chart":
        st.write("### Area Chart")
        st.area_chart(dataf[[Parameter]])
else:
    st.write("No data available for the selected ticker and period.")
