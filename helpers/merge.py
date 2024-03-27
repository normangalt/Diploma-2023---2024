import os
import pandas as pd

def merge_files(directory, prefix):
    """
    Merge files with names starting with a specific prefix into a single DataFrame.

    Args:
        directory (str): Directory containing the files.
        prefix (str): Prefix of the file names.

    Returns:
        pandas.DataFrame: Merged DataFrame.
    """
    # Get list of files starting with the specified prefix
    files = [file for file in os.listdir(directory) if file.startswith(prefix)]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate over each file and read it into a DataFrame
    for file in files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    merged_df = pd.concat(dfs, ignore_index=True)

    return merged_df

# Directory containing the files
directory = r"C:\Users\Roman Kypybida\Desktop\Diploma\Data\FinBERT\chunks"

# Prefix of the file names
prefix = "FinBERT_chunk_"

# Merge files
merged_data = merge_files(directory, prefix)

# Save merged data to a new CSV file
output_file = "merged_data.csv"
merged_data.to_csv(output_file, index=False)