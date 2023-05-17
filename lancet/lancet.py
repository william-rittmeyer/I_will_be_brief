import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        text = ''
        for page in range(num_pages):
            page_obj = reader.pages[page]
            text += page_obj.extract_text()

        return text

# Provide the path to the PDF file you want to read
pdf_file_path = 'file.pdf'

# Call the read_pdf function with the file path
pdf_text = read_pdf(pdf_file_path)

# Print the extracted text
print(pdf_text)
