import pandas as pd

def extract_students(file_path='data/raw/students.csv'):
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} student records")
    return df