from config.db_config import get_connection

def load_courses(df):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO courses_table (course_id, course_name, department, credits)
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (course_id) DO UPDATE
            SET course_name = EXCLUDED.course_name,
                department = EXCLUDED.department,
                credits = EXCLUDED.credits
        """, (row['course_id'], row['course_name'], row['department'], row['credits']))
    conn.commit()
    cur.close()
    conn.close()
    print("Loaded course data")