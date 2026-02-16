import pandas as pd

def extract_faculty(file_path='data/raw/faculty.csv'):
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} faculty records")
    return df