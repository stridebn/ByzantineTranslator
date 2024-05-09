import os
import PyPDF2
import matplotlib.pyplot as plt
import noums
import timings
import math
import csv
import ignore


first_appearance = {}

def extract_num_noums(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        special_unicode_chars = {}
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                for char in text:
                    if ord(char) > ord('\ue000'):  # Considering non-ASCII as special Unicode
                        escaped_char = f"\\u{ord(char):04x}"
                        if escaped_char in special_unicode_chars:
                            special_unicode_chars[escaped_char] += 1
                        else:
                            special_unicode_chars[escaped_char] = 1
    return special_unicode_chars

def save_to_csv(char_counts, file_path):
    # Sort the dictionary by count in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Write to CSV
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Character', 'Count'])  # Writing headers
        for char, count in sorted_char_counts:
            writer.writerow([char, count])

def aggregate_unicode_chars_in_pdfs(directory_path):
    total_unicode_char_counts = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing {filename}...")
            char_counts = extract_num_noums(file_path)
            for char, count in char_counts.items():
                if char in total_unicode_char_counts:
                    total_unicode_char_counts[char] += count
                else:
                    total_unicode_char_counts[char] = count
                    first_appearance[char] = file_path
    save_to_csv(total_unicode_char_counts, "counts.csv")
    return total_unicode_char_counts

def plot_counts(char_counts):
    chars = list(char_counts.keys())
    counts = list(char_counts.values())
    plt.figure(figsize=(10, 8))
    plt.barh(chars, counts, color='skyblue')
    plt.xlabel('Count of Special Unicode Characters')
    plt.ylabel('Unicode Characters')
    plt.title('Frequency of Special Unicode Characters Across PDF Files')
    plt.show()

def calc_percentage_in_map(csv_input_path, csv_output_path):
    # Initialize counts
    total_count = 0
    mapped_count = 0

    # Read the original CSV and prepare to write the new one
    with open(csv_input_path, newline='', encoding='utf-8') as infile, \
         open(csv_output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write headers for the new CSV
        writer.writerow(['Character', 'Count', 'Mapped','Raw','First Appearance'])
        
        next(reader)  # Skip the header of the original CSV
        for row in reader:
            char = row[0]
            char_esc = char.encode('utf-8').decode('unicode-escape')
            count = int(row[1])
            total_count += count
            ignored_count = 0
            # Check if the character is in the mapping
            if char_esc in noums.noums or char_esc in timings.timings:
                mapped_count += count
                writer.writerow([char, count, 'Yes', char_esc, first_appearance[char]])
            elif char_esc in ignore.ignored_symbols:
                ignored_count += count
                writer.writerow([char, count, 'I', char_esc, first_appearance[char]])
            else:
                writer.writerow([char, count, 'No',char_esc, first_appearance[char]])
    
    # Calculate the total percentage for mapped characters
    if total_count > 0:
        total_percentage = (mapped_count / (total_count - ignored_count)) * 100
    else:
        total_percentage = 0  # Avoid division by zero
    
    return total_percentage


def plot_from_csv(csv_path):
    # Initialize data storage
    characters = []
    counts = []
    colors = []
    
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            characters.append(row[0])  # Unicode character
            counts.append(math.log2(int(row[1])))  # Count of character
            # Set the color based on mapping (Yes -> Red, No -> Blue)
            if row[2] == 'Yes':
                colors.append('blue')
            elif row[2] == 'I':
                colors.append('grey')
            else:
                colors.append('red')
    
    # Plotting the data
    plt.figure(figsize=(10, 8))
    plt.bar(characters, counts, color=colors)
    plt.xlabel('Unicode Characters')
    plt.ylabel('Counts')
    plt.title('Counts (log for better visibility) of Unicode Characters Colored by Mapping Status')
    plt.xticks(rotation=45, ha='right')  # Rotate character labels for better visibility
    plt.tight_layout()  # Adjust layout to make room for label rotation
    plt.show()

# Usage
directory_path = 'TestBed/'
total_counts = aggregate_unicode_chars_in_pdfs(directory_path)
csv_path = 'counts.csv'
out_path = 'counts_mapped.csv'
total_percentage = calc_percentage_in_map(csv_path, out_path)
print(f"Total percentage of mapped characters: {total_percentage:.2f}%")
plot_from_csv(out_path)
