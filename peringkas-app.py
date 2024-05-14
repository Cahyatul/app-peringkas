import streamlit as st
from bs4 import BeautifulSoup


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')

elif option == "Input URL":
    url = st.text_input("Masukkan URL:")
    if st.button("Ringkas URL"):
        if url:
            summary = summarize_url(url)
            st.subheader("Ringkasan URL:")
            st.write(summary)
        else:
            st.error("URL tidak valid.")
