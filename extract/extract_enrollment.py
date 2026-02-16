import pandas as pd

def extract_enrollment(file_path='data/raw/enrollment.csv'):
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} enrollment records")
    return df