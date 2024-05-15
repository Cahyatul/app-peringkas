import streamlit as st
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
import re


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
url_input = st.text_input("Masukkan URL")

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus data dalam tanda kurung siku
    text = re.sub(r'\[.*?\]', '', text)
    # Menghapus spasi ekstra
    text = re.sub(r'\s+', ' ', text)
    return text



# Fungsi peringkas teks
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# tombol peringkas
text = ''
if st.button('Ringkas Teks'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        if 'text' in st.session_state:
        summary = summarize_text(st.session_state.text)
        st.write(summary)
