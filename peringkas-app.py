import streamlit as st
from summarizer import summarize_text, summarize_pdf, summarize_docx, summarize_url
import requests
from bs4 import BeautifulSoup


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')


st.title("Aplikasi Peringkas Artikel")

option = st.selectbox("Pilih sumber konten:", ("Upload file", "Input URL"))

if option == "Upload file":
    uploaded_file = st.file_uploader("Upload file (txt, pdf, docx)", type=["txt", "pdf", "docx"])

    if uploaded_file is not None:
        file_type = uploaded_file.type
        if file_type == "text/plain":
            text = uploaded_file.read().decode("utf-8")
            summary = summarize_text(text)
            st.subheader("Ringkasan Teks:")
            st.write(summary)
        elif file_type == "application/pdf":
            summary = summarize_pdf(uploaded_file)
            st.subheader("Ringkasan PDF:")
            st.write(summary)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            summary = summarize_docx(uploaded_file)
            st.subheader("Ringkasan DOCX:")
            st.write(summary)
        else:
            st.error("Format file tidak didukung.")
elif option == "Input URL":
    url = st.text_input("Masukkan URL:")
    if st.button("Ringkas URL"):
        if url:
            summary = summarize_url(url)
            st.subheader("Ringkasan URL:")
            st.write(summary)
        else:
            st.error("URL tidak valid.")
