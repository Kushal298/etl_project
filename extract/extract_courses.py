import pandas as pd

def extract_courses(file_path='data/raw/courses.csv'):
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} course records")
    return df

