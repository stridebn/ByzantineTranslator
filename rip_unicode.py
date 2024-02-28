import PyPDF2

def extract_special_unicode_chars(pdf_path):
    # Open the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    special_unicode_chars = []
    # Iterate through each page
    for page in pdf_reader.pages:
        text = page.extract_text()

        # Iterate through each character and check if it's a special Unicode character
        for char in text:
            if ord(char) >= ord('\uf020'):  # ASCII range is up to 127, so anything above is special Unicode
                special_unicode_chars.append(char)

    return special_unicode_chars

def ordered_special_characters(pdf_path):
    # Open the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    special_unicode_chars = []
    # Iterate through each page
    for page in pdf_reader.pages:
        text = page.extract_text()

        # Iterate through each character and check if it's a special Unicode character
        for char in text:
            if ord(char) > 127:  # ASCII range is up to 127, so anything above is special Unicode
                special_unicode_chars.append(char)
    special_unicode_chars.sort()
    special_unicode_chars = list(set(special_unicode_chars))
    special_unicode_chars.sort()
    return special_unicode_chars

# Path to the uploaded PDF file
pdf_path = 'TrainingData/AprilB.pdf'
# pdf_path = 'C:\Users\strid\Desktop\School\ByzantineTranslator\ByzantineTranslator\TrainingData\AprilB.pdf'
# pdf_path2 = 'TrainingData/EZ-CharacterTables.pdf'

sp_chars = extract_special_unicode_chars(pdf_path)
# osp_chars = ordered_special_characters(pdf_path2)
print(sp_chars)
# print(osp_chars)