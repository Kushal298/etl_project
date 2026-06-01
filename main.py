 from extract.extract_students import extract_students
from transform.transform_students import transform_students
from load.load_students import load_students

from extract.extract_courses import extract_courses
from transform.transform_courses import transform_courses
from load.load_courses import load_courses

from extract.extract_faculty import extract_faculty
from transform.transform_faculty import transform_faculty
from load.load_faculty import load_faculty

from extract.extract_enrollment import extract_enrollment
from transform.transform_enrollment import transform_enrollment
from load.load_enrollment import load_enrollment

def main():
    df_students = extract_students()
    df_students = transform_students(df_students)
    load_students(df_students)

    df_courses = extract_courses()
    df_courses = transform_courses(df_courses)
    load_courses(df_courses)

    df_faculty = extract_faculty()
    df_faculty = transform_faculty(df_faculty)
    load_faculty(df_faculty)

    df_enroll = extract_enrollment()
    df_enroll = transform_enrollment(df_enroll)
    load_enrollment(df_enroll)

if __name__ == '__main__':
    main()