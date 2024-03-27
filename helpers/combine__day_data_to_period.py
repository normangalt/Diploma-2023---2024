import os
import pandas as pd

def combine_csv_files(input_folder, output_folder, output_filename):
    # List to store individual DataFrames
    dfs = []

    # Iterate over each file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            # Read the CSV file into a DataFrame
            file_path = os.path.join(input_folder, file_name)
            df = pd.read_csv(file_path)
            
            # Append the DataFrame to the list
            dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the combined DataFrame to a new CSV file
    output_file_path = os.path.join(output_folder, output_filename)

    combined_df['open_time'] = pd.to_datetime(combined_df['open_time'], unit='ms')
    combined_df.to_csv(output_file_path, index=False)

    print("Combined CSV file saved successfully!")

# Input folder containing CSV files
input_folder = input("Please enter the input folder:")

# Output folder to save the combined CSV file
output_folder = input("Please enter the output folder:")

# User-defined name for the combined CSV file (without the file extension)
user_input = input("Enter a name for the combined CSV file: ")
output_filename = f"{user_input}USDT_combined_data.csv"

# Combine CSV files and save to the specified output folder
combine_csv_files(input_folder, output_folder, output_filename)
