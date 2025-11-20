import pandas as pd
import glob

# Get all sensor data CSV files
csv_files = sorted(glob.glob('sensor_data_2025-03-*.csv'))

# Read and concatenate all CSV files
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)
    print(f"Loaded {file}: {len(df)} rows")

# Merge all dataframes
merged_df = pd.concat(dfs, ignore_index=True)

# Save to merged file
output_file = 'sensor_data_merged.csv'
merged_df.to_csv(output_file, index=False)

print(f"\nMerged {len(csv_files)} files into {output_file}")
print(f"Total rows: {len(merged_df)}")
