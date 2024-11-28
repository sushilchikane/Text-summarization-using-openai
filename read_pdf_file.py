import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get the total number of pages in the PDF
        # num_pages = pdf_reader.numPages
        num_pages = len(pdf_reader.pages)

        # Read the content of each page
        content = ''
        for page_number in range(num_pages):
            # Get a specific page
            # page = pdf_reader.getPage(page_number)
            page = pdf_reader.pages[page_number]
            
            # Extract text from the page
            # content += page.extractText()
            content += page.extract_text()
        
        print(len(content.split()))
    return content

# Replace 'your_pdf_file.pdf' with the path to your PDF file
# pdf_file_path = '../Example 1 Intake Documentation.pdf'
# pdf_content = read_pdf(pdf_file_path)

# print(pdf_content)

# print(len(pdf_content.split()))
