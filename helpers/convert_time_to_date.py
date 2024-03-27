import pandas as pd

# Read the combined data CSV file into a DataFrame
file_name = input("Please enter path to a file:")
combined_data = pd.read_csv(file_name)

output_folder = input("Please enter the output folder:")

user_input = input("Enter a name for the combined CSV file: ")
output_filename = f"{user_input}USDT_combined_data_with_dates.csv"

# Convert the "open_time" column to datetime format
combined_data['open_time'] = pd.to_datetime(combined_data['open_time'], unit='ms')

# Print the first few rows to verify the conversion
print(combined_data.head())

# Save the updated DataFrame with date values to a new CSV file
combined_data.to_csv(output_filename, index=False)

print("Converted 'open_time' column to actual date and saved to combined_data_with_dates.csv")