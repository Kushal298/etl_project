def transform_students(df):
    df['full_name'] = df['full_name'].str.title()
    df['age'] = df['age'].fillna(df['age'].mean())
    df['year'] = df['year'].astype(int)
    print("Transformed student data")
    return df