python_students = {"Alice", "Bob", "Charlie"}
data_science_students = {"Bob", "Diana", "Eve"}

python_students.add("Frank")
data_science_students.remove("Eve")

both_courses = python_students & data_science_students
only_python = python_students - data_science_students
all_students = python_students | data_science_students

course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

growth_projection = {course: count * 2 for course, count in course_counts.items()}

print(both_courses)
print(only_python)
print(all_students)
print(growth_projection)
