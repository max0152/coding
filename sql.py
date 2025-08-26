import sqlite3
import random

conn = sqlite3.connect("university.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS readers")
cur.execute("DROP TABLE IF EXISTS books")

cur.execute("""
CREATE TABLE students  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

cur.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    team_lead TEXT NOT NULL
)
""")

courses = [
    ("python", "Pavel"),
    ("Youtube", "Pewdiepie"),
    ("Yandex", "Litvin"),
    ("Graphical design", "Artem Popov"),
    ("VK", "Pavel Durov"),
]
cur.executemany("INSERT INTO courses (name, team_lead) VALUES (?, ?)", courses)

students = ["Максим", "Богдан", "Лера", "Ильдар", "Крафил", "Булат", "Павел", "Аделина"]
for _ in range(20):
    name = random.choice(students)
    age = random.randint(15, 30)
    course_id = random.randint(1, len(courses))
    cur.execute("INSERT INTO students (name, age, course_id ) VALUES (?, ?, ?)",(name, age, course_id))

conn.commit()

print("\nСредний возраст Студентов:")
for row in cur.execute("SELECT AVG(age) FROM students"):
    print(round(row[0], 1))

print("\nСколько Студентов на каждом курсе:")
for row in cur.execute("""
SELECT courses.name, COUNT(students.id)
FROM courses
LEFT JOIN students ON courses.id = students.course_id
GROUP BY courses.id
"""):
    print(f"Курс: {row[0]}, Студентов: {row[1]}")

conn.close()
