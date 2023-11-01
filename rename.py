import csv
import os

# Path to the CSV file that contains old and new names
csv_file_path = "path/to/your/csv/file.csv"

# Path to the directory where image files are stored
image_dir = "path/to/image/directory/"

# Read CSV and rename files
with open(csv_file_path, mode ='r')as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        old_name = row['OLD']
        new_name = row['NEW']

        old_file_path = os.path.join(image_dir, old_name)
        new_file_path = os.path.join(image_dir, new_name)

        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
        else:
            print(f"File {old_name} not found.")

print("Renaming completed.")
