import pandas as pd

# Function to change the date format
def change_date_format(date_series):
    return pd.to_datetime(date_series).dt.strftime('%m/%d/%Y %H:%M:%S')

# Function to filter rows based on affid column criteria
def filter_affid(df):
    df['affid'] = df['affid'].astype(str)
    mask = df['affid'].apply(lambda x: len(x) == 32 and x.islower())
    valid_rows = df[mask]
    invalid_rows = df[~mask]
    return valid_rows, invalid_rows

input_file = 'rokt_report_20240807.csv'
df = pd.read_csv(input_file)

df['conversionDate'] = change_date_format(df['conversionDate'])

valid_df, invalid_df = filter_affid(df)

output_file = 'rokt_report_20240807_edit.csv'
valid_df.to_csv(output_file, index=False)

invalid_output_file = 'rokt_report_20240807_invalid.csv'
invalid_df.to_csv(invalid_output_file, index=False)

print(f"Valid rows saved to '{output_file}'")
print(f"Invalid rows saved to '{invalid_output_file}'")