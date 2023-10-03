import pandas as pd
import os


current_directory = os.getcwd()
csv_files = [f for f in os.listdir(current_directory) if f.endswith('.csv')]
combined_df = pd.DataFrame()

for csv_file in csv_files:
    file_path = os.path.join(current_directory, csv_file)
    df = pd.read_csv(file_path, usecols=range(1, 7))
    combined_df = combined_df.append(df, ignore_index=True)

combined_df.to_csv('pairing_food_combined.csv', index=False)
