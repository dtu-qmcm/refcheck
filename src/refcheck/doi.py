import re
from pathlib import Path

import pypandoc

DOI_REGEX = "10.\\d{4,9}/[-._;()/:a-z0-9A-Z]+"


def get_dois(path: Path, format) -> list[str]:
    txt = pypandoc.convert_file(path, "plain", format=format)
    matches = re.findall(DOI_REGEX, txt)
    return [r if not r.endswith(".") else r[:-1] for r in matches]


def doi_to_url(doi: str) -> str:
    return "http://dx.doi.org/" + doi
