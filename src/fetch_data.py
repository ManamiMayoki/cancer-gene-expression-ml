import os
import GEOparse
import pandas as pd

def download_and_extract_geo(geo_id="GSE68801", data_dir="./data"):
    os.makedirs(data_dir, exist_ok=True)
    print(f"Fetching {geo_id} from NCBI GEO...")
    
    # Download SOFT family file locally
    gse = GEOparse.get_GEO(geo=geo_id, destdir=data_dir)
    
    # Extract expression matrix
    expression_matrix = gse.pivot_samples('VALUE')
    output_path = os.path.join(data_dir, f"{geo_id}_expression_matrix.csv")
    expression_matrix.to_csv(output_path)
    print(f"Success! Expression matrix shape: {expression_matrix.shape}")
    print(f"Saved locally to {output_path}")

if __name__ == "__main__":
    download_and_extract_geo()