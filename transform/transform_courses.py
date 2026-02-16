def transform_courses(df):
    df['course_name'] = df['course_name'].str.title()
    df['department'] = df['department'].str.title()
    print("Transformed course data")
    return df