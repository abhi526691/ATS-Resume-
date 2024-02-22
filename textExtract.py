from PyPDF2 import PdfReader


class extractText:
    text = ""

    def __init__(self):
        pass

    def extract_txt(self, pdf_file):
        reader = PdfReader(pdf_file)
        number_of_pages = len(reader.pages)
        for page in range(number_of_pages):
            self.text += reader.pages[page].extract_text()
        return self.text
