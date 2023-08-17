from PyPDF2 import PdfWriter, PdfReader
import os

def readPdfText(pdf):
    if os.path.exists(f"./pdfs/{pdf}"):
        reader = PdfReader(f"./pdfs/{pdf}")
        pages = reader.pages[::]
        return pages.extract_text()

if __name__ == "__main__":
    print(readPdfText("./pdfs/example.pdf"))