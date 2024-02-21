import csv

def basic_noums(csv_file_path, py_file_path):
    # Initialize an empty dictionary to hold the map
    map_dict = {}
    
    # Open the CSV file and read its contents
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Extract required columns
            
            # key = row[0]  # First column as key
            key = row[0].encode('latin-1').decode('unicode_escape')
            value = [row[1], int(row[2]), row[3], row[4], row[5]]  # Second to Fifth columns as value
            # Add to dictionary
            map_dict[key] = value
    
    # Write the map to a .py file
    with open(py_file_path, 'w') as pyfile:
        # Write the map definition
        pyfile.write('my_map = ')
        pyfile.write(str(map_dict))
        pyfile.write('\n')

map_path = 'mapping.csv'
py_path = 'mappings.py'

basic_noums(map_path, py_path)
