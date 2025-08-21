CREATE TABLE student_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age VARCHAR(100) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES student_groups(id)
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE enrollments(
    student_id INT,
    course_id INT,
    grade VARCHAR(50) NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Вставка данных

INSERT INTO student_groups (group_name) VALUES
('python'),
('sql'),
('pascal'),
('C#'),
('java');

INSERT INTO teachers (name) VALUES
('Инна Вячеславовна'),
('Лилия Николаевна'),
('Людмила Вениаминовна'),
('Сергей Павлович'),
('Александр Шамильевич');

INSERT INTO students (name, age, group_id) VALUES
('Иван Иванов', 16, 1),
('Анна Смирнова', 21, 2),
('Максим Мотаев', 19, 4),
('Егор Васильев', 18, 4),
('Света умарова', 22, 1);

INSERT INTO courses (course_name, teacher_id) VALUES
('русский', 5),
('английский', 2),
('технология', 3),
('физ-ра', 4),
('математика', 1);

INSERT INTO enrollments (student_id, course_id, grade) VALUES
(1, 1, 100),
(2, 2, 90),
(3, 3, 80),
(4, 4, 70),
(5, 5, 60);

SELECT students.name AS student_name, student_groups.group_name
FROM students
JOIN student_groups ON students.group_id = student_groups.id;

SELECT name, age
FROM students
WHERE CAST(age AS UNSIGNED) > 20;

SELECT courses.course_name, teachers.name AS teacher_name
FROM courses
JOIN teachers ON courses.teacher_id = teachers.id;

SELECT students.name AS student_name, enrollments.grade
FROM students
JOIN enrollments ON students.id = enrollments.student_id
WHERE CAST(enrollments.grade AS UNSIGNED) > 85;

SELECT 
    student_groups.group_name,
    AVG(CAST(students.age AS UNSIGNED)) AS average_age
FROM students
JOIN student_groups ON students.group_id = student_groups.id
GROUP BY student_groups.group_name;

SELECT courses.course_name
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.course_id
WHERE enrollments.student_id IS NULL;

SELECT students.name AS student_name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
WHERE enrollments.grade IS NULL;

SELECT 
    students.name AS student_name,
    AVG(CAST(enrollments.grade AS DECIMAL(5,2))) AS average_grade
FROM students
JOIN enrollments ON students.id = enrollments.student_id
GROUP BY students.id, students.name
ORDER BY average_grade DESC
LIMIT 3;

SELECT 
    courses.course_name,
    COUNT(DISTINCT enrollments.student_id) AS student_count
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.course_id
GROUP BY courses.id, courses.course_name;

SELECT 
    teachers.name AS teacher_name,
    COUNT(courses.id) AS course_count
FROM teachers
JOIN courses ON teachers.id = courses.teacher_id
GROUP BY teachers.id, teachers.name
HAVING COUNT(courses.id) > 1;
