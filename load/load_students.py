from config.db_config import get_connection

def load_students(df):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO students_table (student_id, full_name, age, major, year)
            VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (student_id) DO UPDATE
            SET full_name = EXCLUDED.full_name,
                age = EXCLUDED.age,
                major = EXCLUDED.major,
                year = EXCLUDED.year
        """, (row['student_id'], row['full_name'], row['age'], row['major'], row['year']))
    conn.commit()
    cur.close()
    conn.close()
    print("Loaded student data")