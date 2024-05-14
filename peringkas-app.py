import streamlit as st
from bs4 import BeautifulSoup


st.title('Welcome to Text Summary')
st.header('ringkas artikel dengan mudah dan cepat')

option = st.selectbox("Pilih sumber konten:", ("Upload file", "Input URL"))

if option == "Upload file":
    uploaded_file = st.file_uploader("Upload file (txt, pdf, docx)", type=["txt", "pdf", "docx"])


elif option == "Input URL":
    url = st.text_input("Masukkan URL:")
    if st.button("Ringkas URL"):
        if url:
            summary = summarize_url(url)
            st.subheader("Ringkasan URL:")
            st.write(summary)
        else:
            st.error("URL tidak valid.")
