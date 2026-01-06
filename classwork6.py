attendance = [18, 20, 19, 15, 21]

full_days = 0
total_attendance = 0

for students in attendance:
    if students >= 20:
        print("class was full")
        full_days += 1
    else:
        print("not full")

    total_attendance += students

print("full days:", full_days)
print("total attendance:", total_attendance)
