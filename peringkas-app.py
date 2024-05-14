import streamlit as st
import requests
from bs4 import BeautifulSoup


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')


option = st.text_input("Pilih sumber konten:", ("Input URL"))

elif option == "Input URL":
    url = st.text_input("Masukkan URL:")
    if st.button("Ringkas URL"):
        if url:
            summary = summarize_url(url)
            st.subheader("Ringkasan URL:")
            st.write(summary)
        else:
            st.error("URL tidak valid.")
