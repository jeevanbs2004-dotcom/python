frontend = {"Alice", "Bob", "Charlie", "Diana"}
backend = {"Charlie", "Diana", "Eve", "Frank"}

backend.add("Grace")
frontend.remove("Bob")

both_courses = frontend & backend
only_backend = backend - frontend
total_unique = len(frontend | backend)

course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in course_counts.items():
    print(course, count)

extended_courses = {k: v for k, v in course_counts.items()}
extended_courses["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]

print(both_courses)
print(only_backend)
print(total_unique)
print(extended_courses)
