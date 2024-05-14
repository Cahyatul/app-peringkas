import streamlit as st
from bs4 import BeautifulSoup
import requests
from transformers import pipeline


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus data dalam tanda kurung siku
    text = re.sub(r'\[.*?\]', '', text)
    # Menghapus spasi ekstra
    text = re.sub(r'\s+', ' ', text)
    return text

# Input URL
url_input = st.text_input("Masukkan URL artikel")

# tombol peringkas
text = ''
if st.button('Ringkas Teks'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        st.write(text)
