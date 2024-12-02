# Refcheck

![Tests](https://github.com/dtu-qmcm/refcheck/.github/workflows/run_tests.yml/badge.svg)

This repository contains the source code for a tiny  web app that extracts the DOIs from a document and presents them in a clickable list.

You might want to do this to check if your grant application contains any incorrect DOI links, or if the links don't match the references as they are supposed to.

Check out the app here: <https://dtu-qmcm-refcheck-app-myspwb.streamlit.app/>.

Refcheck uses [pypandoc](https://github.com/JessicaTegner/pypandoc) to convert document formats and is written and hosted using [Streamlit](https://streamlit.io/).
