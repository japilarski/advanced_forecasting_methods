import pandas as pd
import glob

def merge_csv_files(input_pattern='data/*.csv', output_file='output/merged_output.csv'):
    csv_files = glob.glob(input_pattern)
    dataframes = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if 'TIME_PERIOD' not in df.columns:
                continue
            dataframes.append(df)
            print(f"Loaded {file}: {len(df)} rows, {len(df.columns)} columns")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    merged_df = dataframes[0]
    for df in dataframes[1:]:
        merged_df = pd.merge(merged_df, df, on='TIME_PERIOD', how='outer')

    merged_df = merged_df.sort_values('TIME_PERIOD')

    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    merge_csv_files('./output/*.csv', 'final_dataset.csv')

