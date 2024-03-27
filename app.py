import streamlit as st

x = st.slide("select a value")
st.wirte(x, 'is a square', x * x)

st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this si the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
