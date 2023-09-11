import streamlit


streamlit.title('Bank')


streamlit.text('Account Name')
streamlit.text('Account Balance')
streamlit.text('Rrfresh Balance')



streamlit.text('Send money')
streamlit.text('Recipient')

streamlit.text('Request money')
streamlit.text('Requestee')


conn = st.experimental_connection('streamlit_bank', type='sql')

Customer = conn.query('select * from dbo.Customer')
st.dataframe(Customer)


