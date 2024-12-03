import tempfile
from pathlib import Path

import pymupdf
import streamlit as st

from refcheck.doi import get_dois, doi_to_url, fetch_doi_json

FORMAT_TO_EXT = {
    "markdown": "md",
    "docx": "docx",
    "latex": "tex",
    "pdf": "pdf",
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
    if format == "pdf":
        doc = pymupdf.open(path)
        text = (
            "".join(page.get_text() for page in doc).replace("\n", " ").encode("utf-8")
        )
        txt_path = path.with_suffix(".txt")
        with open(txt_path, "wb") as f:
            f.write(text)
        results = get_dois(txt_path, "rtf")
    else:
        results = get_dois(path, format)
    urls = [doi_to_url(doi) for doi in results]
    doi_jsons = [fetch_doi_json(url) for url in urls]
    st.write("Here are the dois in your document. Please check if they are correct!")
    for doi, url, doi_json in zip(results, urls, doi_jsons):
        title = f"*{doi_json["title"]}*"
        authors = ", ".join(f"{a["given"]} {a["family"]}" for a in doi_json["author"])
        st.write(f"[**{doi}**]({url}): {title}", unsafe_allow_html=True)
        st.write(authors)
        st.write("")
