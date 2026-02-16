def transform_faculty(df):
    df['name'] = df['name'].str.title()
    df['department'] = df['department'].str.title()
    print("Transformed faculty data")
    return df