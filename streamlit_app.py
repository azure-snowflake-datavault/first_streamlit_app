import streamlit as st


st.title('Bank')


st.text('Account Name')
st.text('Account Balance')
st.text('Rrfresh Balance')



st.text('Send money')
st.text('Recipient')

st.text('Request money')
st.text('Requestee')


conn = st.experimental_connection('streamlit_bank', type='sql')

Customer = conn.query('select * from dbo.Customer')
st.dataframe(Customer)


