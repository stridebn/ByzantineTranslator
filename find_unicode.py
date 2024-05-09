import fitz  # PyMuPDF
import imageio
import csv
from PIL import Image

def find_and_crop_char(pdf_path, unicode_char):
    # Open the provided PDF file
    doc = fitz.open(pdf_path)
    i = 0
    for page in doc:
        i += 1
        # Search for the character on each page
        text_instances = page.search_for(unicode_char)

        # Check if the character was found
        if text_instances:
            # Get the first instance of the character
            first_instance = text_instances[0]

            # Create a zoomed-in matrix for higher resolution
            zoom = 2  # Increase zoom for higher resolution images
            mat = fitz.Matrix(zoom, zoom)

            # Render page to an image
            pix = page.get_pixmap(matrix=mat)

            # Convert PyMuPDF pixmap to a PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Calculate the crop box dimensions and adjust if necessary
            x0, y0, x1, y1 = [int(coord * zoom) for coord in first_instance]
            x0 = max(x0-30, 0)
            y0 = max(y0-30, 0)
            x1 = min(x1 + 30, img.width)
            y1 = min(y1 + 30, img.height)
            print(f"Cropping parameters: x0={x0}, y0={y0}, x1={x1}, y1={y1}; Image dimensions: width={img.width}, height={img.height}")
            # cropped_img = img.crop((x0, y0, x1, y1))
            filename = f"u{ord(unicode_char):04x}_pg{i}.png"
            img.save("output.png")
            # Save or display the cropped image

            crop = imageio.imread("output.png")
            # Crop the image using numpy slicing
            cropped_img = crop[y0:y1, x0:x1]
            # Save the cropped image
            imageio.imwrite(f"UnicodeLocations/{filename}", cropped_img)
            break
    else:
        print("Character not found in the document.")

# pdf_path = 'TrainingData/EZ-CharacterTables.pdf'
# unicode_char = '\uf058'
# find_and_crop_char(pdf_path, unicode_char)

with open("counts_mapped.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Decode the Unicode character from the Character column
        unicode_char = chr(int(row['Character'][2:], 16))
        pdf_path = row['First Appearance']
        # Call the function with the decoded Unicode character and the fixed PDF path
        find_and_crop_char(pdf_path, unicode_char)