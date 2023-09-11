import streamlit as st
import sqlalchemy
import pyodbc

st.title('Bank')
st.text('Account Name')
st.text('Account Balance')
st.text('Rrfresh Balance')
st.text('Send money')
st.text('Recipient')
st.text('Request money')
st.text('Requestee')

st.text('Test 6')


# conn = st.experimental_connection('streamlit_bank', type='sql')
# Customer = conn.query('select * from dbo.Customer')
# st.dataframe(Customer)


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

# server = "streamlitbank.database.windows.net,1433"
# server_tcp = "tcp:streamlitbank.database.windows.net"
# server_1433 = "streamlitbank.database.windows.net,1433"
# server_tcp_1433 = "tcp:streamlitbank.database.windows.net,1433"

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


