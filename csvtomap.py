import csv

def basic_noums(csv_file_path, file_name):
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
    py_file_path = file_name + '.py'
    with open(py_file_path, 'w') as pyfile:
        # Write the map definition
        pyfile.write(file_name + ' = ')
        pyfile.write(str(map_dict))
        pyfile.write('\n')

def timing(csv_file_path, file_name):
    # Initialize an empty dictionary to hold the map
    map_dict = {}
    
    # Open the CSV file and read its contents
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Extract required columns
            
            # key = row[0]  # First column as key
            key = row[0].encode('latin-1').decode('unicode_escape')
            value = [float(row[1]), int(row[2]), int(row[3])]  # Second to Fifth columns as value
            # Add to dictionary
            map_dict[key] = value
    
    # Write the map to a .py file
    py_file_path = file_name + '.py'
    with open(py_file_path, 'w') as pyfile:
        # Write the map definition
        pyfile.write(file_name + ' = ')
        pyfile.write(str(map_dict))
        pyfile.write('\n')

map_path = 'mapping.csv'
name = 'noums'

basic_noums(map_path, name)

map_path = 'timing.csv'
name = 'timings'

timing(map_path, name)