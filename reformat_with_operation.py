import pandas as pd

def reformat_with_operation(input_file, output_file='timeseries_output.csv'):
    df = pd.read_csv(input_file, sep=';')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.dropna(axis=1, how='all')

    df['Column_Name'] = (
        df['TYPE'].str.strip() + ' - ' + 
        df['OPERATION'].str.strip() + ' - ' + 
        df['UNIT'].str.strip()
    ).str.lower()

    pivoted = df.pivot_table(
        index='TIME_PERIOD',
        columns='Column_Name',
        values='OBS_VALUE',
        aggfunc='first'  
    )

    pivoted = pivoted.reset_index()
    pivoted = pivoted.sort_values('TIME_PERIOD')
    pivoted.to_csv(output_file, index=False)


    return pivoted

if __name__ == "__main__":
    input_filename = 'Supply and transformation of solid fossil fuels - monthly data - cleanded.csv' 
    output_filename = 'timeseries_output_2.csv'

    result = reformat_with_operation(input_filename, output_filename)
