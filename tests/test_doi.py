from pathlib import Path
import pytest
from refcheck.doi import get_dois

EXPECTED_RESULT = ["10.1021/acssynbio.3c00662", "10.1021/acssynbio.4c00035"]


@pytest.mark.parametrize(
    "path,format",
    [
        (Path("tests") / "example.md", "markdown"),
        (Path("tests") / "example.tex", "latex"),
        (Path("tests") / "example.docx", "docx"),
    ],
)
def test_get_dois(path, format):
    assert get_dois(path, format) == EXPECTED_RESULT
