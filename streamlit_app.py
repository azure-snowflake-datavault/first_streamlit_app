import streamlit as st
import sqlalchemy
import pyodbc
import pandas

st.title('Bank')
st.text('Account Name')
st.text('Account Balance')
st.text('Rrfresh Balance')
st.text('Send money')
st.text('Recipient')
st.text('Request money')
st.text('Requestee')



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



conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("Select cust_id from dbo.Customer")
cust_ids_df = pandas.DataFrame((tuple(t) for t in rows)) 

option = st.selectbox('Get Account Details for?', cust_ids_df[0] )
st.write('Customer details for:', option)


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
Cust_query = "Select * from dbo.Customer where Cust_id = " + str(option)
st.write(Cust_query)
rows = run_query(Cust_query)
df = pandas.DataFrame((tuple(t) for t in rows)) 
st.dataframe(df)


