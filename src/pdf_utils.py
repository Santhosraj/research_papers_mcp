import PyPDF2
import base64
import io

def extract_pdf_text(encoded_content: str) -> str:
    try:
        # Decode base64 content from GitHub
        pdf_content = base64.b64decode(encoded_content)
        pdf_file = io.BytesIO(pdf_content)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"