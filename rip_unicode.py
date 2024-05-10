import PyPDF2
import re
import os
import helpers

def extract_special_unicode_chars(pdf_path):
    # Open the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    special_unicode_chars = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        # Iterate through each character and check if it's a special Unicode character
        for char in text:
            if char == '\uF068' and char in special_unicode_chars:
                return special_unicode_chars
            elif ord(char) > ord('\uE000'):  # \uE000 represents the bound of the EZ-Byzantine font 
                special_unicode_chars.append(char)
    return special_unicode_chars


    # Iterate through each page
    # print(f"Total pages: {pdf_reader._get_num_pages()}")

def get_tempo(pdf_path):
    tempo_marks = ['\uf041', '\uf061', '\uf063', '\uf073', '\uf07A', '\uf078', '\uf058', '\uf05A']
    tempo = 120
    # Open the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    # Iterate through each page
    print(f"Total pages: {pdf_reader._get_num_pages()}")
    for page in pdf_reader.pages:
        text = page.extract_text()
        found_special_char = False
        for char in text:
            if char in tempo_marks:  # Checks for tempo characters
                found_special_char = True
                # Use regex to find the next integer in text
                match = re.search(r'\d+', text[text.index(char):])
                if match:
                    tempo = int(match.group())  # Set tempo to the found integer
                    break
        if found_special_char:
            break
    return tempo

def ordered_special_characters(pdf_path):
    # Open the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    special_unicode_chars = []
    # Iterate through each page
    for page in pdf_reader.pages:
        text = page.extract_text()

        # Iterate through each character and check if it's a special Unicode character
        for char in text:
            if ord(char) >= '\uf020':  # ASCII range is up to 127, so anything above is special Unicode
                special_unicode_chars.append(char)
    special_unicode_chars.sort()
    special_unicode_chars = list(set(special_unicode_chars))
    special_unicode_chars.sort()
    return special_unicode_chars

# Path to the uploaded PDF file
# pdf_path = 'TrainingData/b5053.pdf'
pdf_path = 'TrainingData/b5109.pdf'
# pdf_path = 'TrainingData/b2925_Blessed_Brief.pdf'
# pdf_path = 'C:\Users\strid\Desktop\School\ByzantineTranslator\ByzantineTranslator\TrainingData\AprilB.pdf'
# pdf_path2 = 'TrainingData/EZ-CharacterTables.pdf'

def process_pdfs(directory):
    total_tone_chars = []
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            
            # Call your custom functions to process the PDF
            sp_chars = extract_special_unicode_chars(pdf_path)
            tone_chars = helpers.get_tone_marks(sp_chars)
            total_tone_chars.append(tone_chars)
    
    # Flatten the list of lists to a single-dimensional list
    flat_list = [item for sublist in total_tone_chars for item in sublist]
    flat_list = list(set(flat_list))
    print(flat_list)
    return flat_list


pdf_path = 'TrainingData/b5918.pdf'
sp_chars = extract_special_unicode_chars(pdf_path)
print(sp_chars)
# # osp_chars = ordered_special_characters(pdf_path2)
# print(get_tempo(pdf_path))
# print(sp_chars)
# path = 'TestBed/'
# process_pdfs(path)
# print(osp_chars)