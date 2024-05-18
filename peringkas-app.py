import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

# Fungsi untuk meringkas teks
def summarize_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Membuat frekuensi kata
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
    
    # Menghitung skor kalimat
    sentences = sent_tokenize(text)
    sentence_value = dict()
    
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq
    
    # Menentukan panjang ringkasan
    summary_length = int(len(sentences) * 0.3)
    
    # Mendapatkan kalimat terpenting
    summary_sentences = nlargest(summary_length, sentence_value, key=sentence_value.get)
    
    summary = ' '.join(summary_sentences)
    return summary

# Aplikasi Streamlit
def main():
    st.title("Aplikasi Peringkas Teks")
    st.write("Masukkan teks di bawah ini untuk diringkas:")
    
    text = st.text_area("Teks Asli", "")
    
    if st.button("Ringkas Teks"):
        if text:
            summary = summarize_text(text)
            st.write("Ringkasan:")
            st.write(summary)
        else:
            st.write("Mohon masukkan teks untuk diringkas.")

if __name__ == "__main__":
    main()
