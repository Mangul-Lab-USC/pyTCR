import pandas as pd
import glob 
import os 

path = "samples/*.tsv"
for filename in glob.glob(path):
    df = pd.read_csv(filename, sep="\t", engine="c", low_memory=False)

    # Enter the column names from your data that represent the required pyTCR columns
    required_columns = ['sample_name','frequency', 'templates','amino_acid', 'rearrangement', 'v_resolved' , 'd_resolved', 'j_resolved']

    optional_columns = ['hospitalized']

    df_new = df.filter(required_columns + optional_columns)

    # Rename the columns to pyTCR standard names
    df_new.columns = ['sample','freq', '#count', 'cdr3aa','cdr3nt', 'v', 'd', 'j'] + optional_columns

    df_new.to_csv(f'./{filename}.csv', na_rep='.', index=False)

# Combine all csv files
globbed_files = glob.glob("samples/*.csv")

data = []

for csv in globbed_files:
    dataframe = pd.read_csv(csv)
    dataframe['sample'] = os.path.basename(csv.split('.')[0])
    data.append(dataframe)
    combined_data = pd.concat(data)

combined_data.to_csv("combined_data.csv", index=False)