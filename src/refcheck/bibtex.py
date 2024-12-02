import requests


def fetch_bibtex(doi_url: str) -> str | None:
    headers = {"accept": "application/x-bibtex"}
    r = requests.get(doi_url, headers=headers)
    return r.text if r is not None else None
