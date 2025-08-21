import PyPDF2
import streamlit as st

st.title("🔍 PDF Keyword Counter")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
tags_input = st.text_input("Enter keywords (separated by commas)", "methane, co2, emissions")

if uploaded_pdf and tags_input:
    tags = [kw.strip() for kw in tags_input.split(",")]
    reader = PyPDF2.PdfReader(uploaded_pdf)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    var = 0
    st.subheader("Results:")
    for tag in tags:
        counter = text.lower().count(tag.lower())
        st.write(f"Tag '{tag}' appeared {counter} times in text.")
        var += 1 if counter>0 else 0
    st.write(f"{var*100/len(tags):.2f}% of tags appeared in text.")