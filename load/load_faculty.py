from config.db_config import get_connection

def load_faculty(df):
    conn = get_connection()
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO faculty_table (faculty_id, name, department, title)
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (faculty_id) DO UPDATE
            SET name = EXCLUDED.name,
                department = EXCLUDED.department,
                title = EXCLUDED.title
        """, (row['faculty_id'], row['name'], row['department'], row['title']))
    conn.commit()
    cur.close()
    conn.close()
    print("Loaded faculty data")