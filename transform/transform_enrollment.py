def transform_enrollment(df):
    df['semester'] = df['semester'].str.title()
    df['grade'] = df['grade'].str.upper()
    print("Transformed enrollment data")
    return df