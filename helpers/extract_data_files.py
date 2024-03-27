import os
import zipfile

# Path to the folder containing the zip archives
folder_path = input("Please enter the folde with archives:")

# Path to the folder where you want to extract the CSV files
extract_folder = input("Please enter the folder for extraction:")

# Create the extract folder if it doesn't exist
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".zip"):
        # Construct the full path to the zip archive
        zip_file_path = os.path.join(folder_path, file_name)
        
        # Extract the contents of the zip archive
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

print("Extraction completed successfully!")
