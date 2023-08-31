from PyPDF2 import PdfWriter, PdfReader
import os
import io

def readPdfText(pdf):
    if os.path.exists(f"./pdfs/{pdf}"):
        reader = PdfReader(f"./pdfs/{pdf}")
        pages = reader.pages[::]
        return pages.extract_text()

def bytesToPdf(pdfBytes, pdfName:str, path: os.path = os.path("./pdfs/")):

    pdf = io.BytesIO(pdfBytes) 
    pdf = PdfReader(pdf)

    outputPdf = PdfWriter()
    
    for page in pdf:
        outputPdf.add_page(page)
    
    with open(path+pdfName, "wb") as output_path:
        outputPdf.write(output_path)

def delPdf(pdfName:str, path:os.path = os.path("./pdfs/")):
    if os.path.exists(path+pdfName):
        os.remove(path+pdfName)
    else:
        raise Exception("The pdf was not found, during process")
        
if __name__ == "__main__":
    print(readPdfText("./pdfs/example.pdf"))