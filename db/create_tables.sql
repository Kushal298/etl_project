CREATE TABLE students_table (
    student_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    age INT,
    major VARCHAR(50),
    year INT
);

CREATE TABLE courses_table (
    course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100),
    department VARCHAR(50),
    credits INT
);

CREATE TABLE faculty_table (
    faculty_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    title VARCHAR(50)
);

CREATE TABLE enrollment_table (
    enrollment_id VARCHAR(10) PRIMARY KEY,
    student_id INT REFERENCES students_table(student_id),
    course_id VARCHAR(10) REFERENCES courses_table(course_id),
    semester VARCHAR(20),
    grade VARCHAR(2)
);