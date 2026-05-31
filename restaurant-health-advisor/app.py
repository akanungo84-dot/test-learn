import streamlit as st

st.set_page_config(page_title='Restaurant Health Advisor')

st.title('🍽️ Restaurant Health Advisor')
url = st.text_input('Restaurant Menu URL')

personas = st.multiselect(
    'Select Personas',
    ['Diabetes','High BP','Weight Loss','Heart Disease','CKD','High Protein/Fitness']
)

if st.button('Analyze'):
    st.info('Analysis engine coming in next commit.')
    st.write({'url': url, 'personas': personas})
