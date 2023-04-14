import streamlit as st

st.title('CampusX')

def first_run():
    return 'mast mai'

col1,col2=st.columns(2)

with col1:
    st.image('Sumit.jpg')
with col2:
    st.text('This side Sumit')

st.header('Courses')
st.subheader('Python')
st.subheader('SQL')
text_first=first_run()
st.text(text_first)