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

# tombol peringkas
text = ''
if st.button('Ringkas Teks'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        st.write(text)

# Fungsi peringkas teks
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Tampilkan hasil peringkasan
if st.button('Tampilkan Ringkasan'):
    if text:
        summary = summarize_text(text)
        st.write(summary)
    else:
        st.error('Silakan masukkan teks untuk diringkas.')
