import streamlit as st
import pyodbc
import pandas


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
# st.cache_data(ttl=600)
@st.cache_resource
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

cust_rows = run_query("Select cust_id from dbo.Customer")
cust_ids_df = pandas.DataFrame((tuple(t) for t in cust_rows)) 
option_cust = st.selectbox('Get Customer Details for?', cust_ids_df[0] )
st.write('Customer details for:', option_cust)

Cust_query = "Select * from dbo.Customer where Cust_id = " + str(option_cust)
st.write(Cust_query)
cust_details = run_query(Cust_query)
df_cust = pandas.DataFrame((tuple(t) for t in cust_details)) 
st.dataframe(df_cust)



@st.cache_resource
def run_query2(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
account_relation_query = "Select Account_id from dbo.Account_Customer_Relation where Cust_id = " + str(option_cust)
account_rows = run_query2("account_relation_query")
account_ids_df = pandas.DataFrame((tuple(t) for t in account_rows)) 
option_account = st.selectbox('Get Account Details for?', account_ids_df[0] )
st.write('Customer details for:', option_account)

@st.cache_resource
def run_query3(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
Account_query = "Select * from dbo.Account where Account_id = " + str(option_account)
st.write(Account_query)
cust_details = run_query3(Account_query)
df_account = pandas.DataFrame((tuple(t) for t in cust_details)) 
st.dataframe(df_account)

