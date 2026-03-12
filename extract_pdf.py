import os
import sys

try:
    import PyPDF2
    print("PyPDF2 is available")
except ImportError:
    print("PyPDF2 not available, trying to install...")
    os.system("pip install PyPDF2")
    import PyPDF2

def extract_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

if __name__ == "__main__":
    pdf_path = "ICICI_Bank_Investment_Report.pdf"
    if os.path.exists(pdf_path):
        text = extract_pdf_text(pdf_path)
        print("Extracted text length:", len(text))
        print("First 1000 characters:")
        print(text[:1000])
        
        # Save to text file
        with open("icici_report_extracted.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Text saved to icici_report_extracted.txt")
    else:
        print(f"File {pdf_path} not found")
