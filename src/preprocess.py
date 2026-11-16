import pandas as pd
import os

# Path to the downloaded series matrix file
data_path = "./data/GSE68801_series_matrix.txt.gz"

if not os.path.exists(data_path):
    print(f"Error: Could not find file at {data_path}")
else:
    print("Loading gene expression matrix...")
    
    # GEO series matrix files contain header metadata lines starting with '!'
    # We skip them using comment='!' and load the expression values table
    df = pd.read_csv(data_path, compression='gzip', sep='\t', comment='!', index_col=0)
    
    print("Dataset Loaded Successfully!")
    print(f"Matrix Shape (Genes x Samples): {df.shape}")
    print("\nFirst 5 rows and 5 columns of the matrix:")
    print(df.iloc[:5, :5])