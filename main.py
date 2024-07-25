import streamlit as st, pandas as pd, pymysql

st.title("Amazon Sales (India)")

st.map(latitude=20.5937, longitude=78.9629, color='green')


# with pymysql.connect(user='root', passwd='ningunaok12OK@', database='AmazonSales') as connection:
#     fact = pd.read_sql("SELECT * FROM Fact;", connection)

# st.dataframe(fact)