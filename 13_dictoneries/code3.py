student_attendance = {"Rolf" : 96, "Adam" : 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

attend = student_attendance.values()
print(sum(attend)/len(attend))