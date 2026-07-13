
import pdfplumber

def read_pdf(path: str) -> str:
    """Extract text from a PDF file."""

    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_txt(path: str) -> str:
    """Read a text file."""

    with open(path, "r", encoding="utf-8") as file:
        return file.read()