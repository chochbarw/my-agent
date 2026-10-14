import streamlit as st

st.title("우리 회사 챗봇")
st.title("만나서 만갑습니다. :)")
st.title("_우리 회사_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

st.badge("new")
st.markdown("*Streamlot* is **really** ***cool***.")

page_1 = st.Page("page_1.py")
page_2 = st.Page("page_2.py")
page_3 = st.Page("page_3.py")

pages = st.navigation([page_1, page_2, page_3], position = "top")

pages.run()
