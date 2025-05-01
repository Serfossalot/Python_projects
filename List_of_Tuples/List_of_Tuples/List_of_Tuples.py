def calc_average(scores):
    return sum(scores) / len(scores)
def student_avg(student):
    scores = student[2]
    return calc_average(scores)
students = [
    ("Alan Turing", "S12345", (85, 92, 88)),
    ("John von Neumann", "S23456", (78, 82, 91)),
    ("Charles Babbage", "S34567", (92, 87, 85)),
    ("Ada Lovelace", "S45678", (91, 94, 90)),
    ("Tim Berners-Lee", "S38071", (99,89,85))
    ]
sorted_students = sorted(students, key=student_avg, reverse=True)
print('Descending list by average: ')
for student in sorted_students:
    avg = student_avg(student)
    print(f"Name: {student[0]}, ID: {student[1]}, Average Score: {avg:.2f}")