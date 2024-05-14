import streamlit as st
from bs4 import BeautifulSoup
import requests


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')

def get_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            article_text = ' '.join(p.get_text() for p in paragraphs)
            return article_text
        else:
            return f"Error: Status code {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"

# Input URL
url_input = st.text_input("Masukkan URL artikel")


text = ''
if st.button('Lihat Teks'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        st.write(text) 

