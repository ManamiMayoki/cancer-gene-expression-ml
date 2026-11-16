import os
import GEOparse

def download_and_extract_geo(geo_id="GSE68801", data_dir="./data"):
    os.makedirs(data_dir, exist_ok=True)
    print(f"Fetching {geo_id} metadata and soft file...")
    
    try:
        # Attempt download with GEOparse
        gse = GEOparse.get_GEO(geo=geo_id, destdir=data_dir, annotate_gpl=False)
        expression_matrix = gse.pivot_samples('VALUE')
        output_path = os.path.join(data_dir, f"{geo_id}_expression_matrix.csv")
        expression_matrix.to_csv(output_path)
        print(f"Success! Saved locally to {output_path}")
    except Exception as e:
        print(f"FTP/Download encountered an issue: {e}")
        print("Tip: You can manually download the Series Matrix file (.txt.gz) from the NCBI GEO website for your ID and place it in the ./data/ folder.")

if __name__ == "__main__":
    download_and_extract_geo()