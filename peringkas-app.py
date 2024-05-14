import streamlit as st
from bs4 import BeautifulSoup
import requests


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')



# Input URL
url_input = st.text_input("Masukkan URL artikel")

# tombol peringkas
text = ''
if st.button('Lihat Teks'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        st.write(text) 

