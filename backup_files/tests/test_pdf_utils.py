import pytest
from pdf_utils import extract_pdf_text
import base64

def test_extract_pdf_text():
    # Mock a simple PDF content (base64-encoded)
    sample_pdf = base64.b64encode(b"%PDF-1.4\nSample text").decode('utf-8')
    text = extract_pdf_text(sample_pdf)
    assert "Sample text" in text