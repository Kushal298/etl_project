from config.db_config import get_connection

def load_enrollment(df):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO enrollment_table (enrollment_id, student_id, course_id, semester, grade)
            VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (enrollment_id) DO UPDATE
            SET student_id = EXCLUDED.student_id,
                course_id = EXCLUDED.course_id,
                semester = EXCLUDED.semester,
                grade = EXCLUDED.grade
        """, (row['enrollment_id'], row['student_id'], row['course_id'], row['semester'], row['grade']))
    conn.commit()
    cur.close()
    conn.close()
    print("Loaded enrollment data")