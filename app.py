import streamlit as st

st.title('CampusX')

col1,col2=st.columns(2)

with col1:
    st.image('Sumit.jpg')
with col2:
    st.text('This side Sumit')

st.header('Courses')
st.subheader('Python')
st.subheader('SQL')