import streamlit as st
import pyodbc
import pandas


st.title("BANK")

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

@st.cache_resource
def run_query2(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
Cust_query = "Select * from dbo.Customer where Cust_id = " + str(option_cust)
st.write(Cust_query)
cust_details = run_query2(Cust_query)
df_cust = pandas.DataFrame((tuple(t) for t in cust_details)) 
st.dataframe(df_cust)



@st.cache_resource
def run_query3(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
account_relation_query = "Select Account_id from dbo.Account_Customer_Relation where Cust_id = " + str(option_cust)
account_rows = run_query3(account_relation_query)
account_ids_df = pandas.DataFrame((tuple(t) for t in account_rows)) 
option_account = st.selectbox('Get Account Details for?', account_ids_df[0] )
st.write('Customer details for:', option_account)

@st.cache_resource
def run_query4(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
Account_query = "Select * from dbo.Account where Account_id = " + str(option_account)
st.write(Account_query)
cust_details = run_query4(Account_query)
df_account = pandas.DataFrame((tuple(t) for t in cust_details)) 
st.dataframe(df_account)

@st.cache_resource
def run_query5(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
all_accounts = "Select Account_id from dbo.Account"
all_account_rows = run_query5(all_accounts)
all_account_ids_df = pandas.DataFrame((tuple(t) for t in all_account_rows)) 


@st.cache_resource
def run_query6(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
max_transaction_id_query = "Select max(Transaction_Id) Account_id from dbo.Account_transaction"
max_transaction_id_row = run_query6(max_transaction_id_query)
max_transaction_id_df = pandas.DataFrame((tuple(t) for t in max_transaction_id_row)) 
max_transaction_id = max_transaction_id_df[0][0]


st.Write("Send money"):
debit_account = st.selectbox('Debit Account?', account_ids_df[0] )
credit_account = st.selectbox('Debit Account?', all_account_ids_df[0] )
amount = st.text_input('Amount to Send', 100 )
transaction_query = "Insert into dbo.Account_transaction values (" + str(max_transaction_id) + "," + str(debit_account) + "," + str(credit_account) + ",'Debit',SYSDATETIME(),SYSDATETIME())"


@st.cache_resource
def run_query7(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


if st.button("Send money"):   
    run_query7(transaction_query)
    
