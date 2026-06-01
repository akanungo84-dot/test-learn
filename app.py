import streamlit as st

st.set_page_config(page_title='Hello Streamlit', page_icon='👋')

st.title('👋 Hello Streamlit')
st.write('Welcome to your first Streamlit app running from GitHub.')

name = st.text_input('What is your name?')
if name:
    st.success(f'Hello, {name}!')
