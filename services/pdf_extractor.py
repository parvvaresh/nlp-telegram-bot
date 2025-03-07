import PyPDF2

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    try:
         with open(file_path, "rb") as f:
             reader = PyPDF2.PdfReader(f)
             for page in reader.pages:
                 extracted = page.extract_text()
                 if extracted:
                     text += extracted
         return text if text else "متنی یافت نشد."
    except Exception as e:
         return "خطا در استخراج متن: " + str(e)
