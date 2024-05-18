import streamlit as st
from bs4 import BeautifulSoup
import requests
from transformers import pipeline
import re
import nltk
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Mengunduh tokenizer untuk bahasa Inggris (yang dapat digunakan untuk teks Indonesia)
nltk.download('punkt')

st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')


# Fungsi untuk mengambil teks dari URL
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

# Fungsi untuk pembersihan teks
def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)  # Menghapus teks dalam tanda kurung
    text = re.sub(r'\s+', ' ', text)  # Menghapus spasi berlebih
    text = text.lower()  # Mengubah teks menjadi huruf kecil
    return text

# Fungsi untuk menghapus stopwords
def remove_stopwords(text):
    factory = StopWordRemoverFactory()
    stopword_remover = factory.create_stop_word_remover()
    return stopword_remover.remove(text)

# Fungsi untuk memisahkan teks menjadi kalimat-kalimat
def split_sentences(text):
    return nltk.sent_tokenize(text)

# Fungsi untuk tokenisasi teks
def tokenize_text(sentences):
    return [nltk.word_tokenize(sentence) for sentence in sentences]

# Fungsi untuk meringkas teks menggunakan TextRank
def summarize_text(text):
    parser = PlaintextParser.from_string(text, SumyTokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 3)  # Merangkum menjadi 3 kalimat
    return ' '.join([str(sentence) for sentence in summary])

# Input URL
url_input = st.text_input("Masukkan URL artikel")

user_input = st.text_input("masukkan teks")

# Tombol untuk menampilkan teks
if st.button('Lihat Teks'):
    text = ''
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
       
  
