import tempfile
from pathlib import Path

import streamlit as st

from refcheck.doi import get_dois, doi_to_url
from refcheck.bibtex import fetch_bibtex

DOI_REGEX = "10.\\d{4,9}/[-._;()/:a-z0-9A-Z]+"
FORMAT_TO_EXT = {
    "markdown": "md",
    "docx": "docx",
    "latex": "tex",
}


st.title("Reference Checker")

st.write("Get a clickable list of the dois in your document.")

format = st.selectbox("Choose a file format", options=FORMAT_TO_EXT.keys())
ext = FORMAT_TO_EXT[format]

uploaded_file = st.file_uploader("Upload a file", type=ext)
results = []
if uploaded_file is not None:
    temp_dir = tempfile.mkdtemp()
    path = Path(temp_dir) / uploaded_file.name
    with open(path, "wb") as f:
        f.write(uploaded_file.getvalue())
    results = get_dois(path, format)
    urls = [doi_to_url(doi) for doi in results]
    bibtexes = [fetch_bibtex(url) for url in urls]

    st.write("Here are the dois in your document. Please check if they are correct!")
    for doi, url, bibtex in zip(results, urls, bibtexes):
        st.write(f"[**{doi}**]({url}):", bibtex)
        st.write("")
